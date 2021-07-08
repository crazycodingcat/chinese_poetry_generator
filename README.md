# chinese_poetry_generator 唐诗生成器
Chinese poetry generator using deep learning models (LSTM CharRNN) in PyTorch

基于PyTorch的LSTM CharRNN模型，给定第一句五个字，自动生成五言唐诗。

## Environment
torch==1.7.1  
zhconv==1.4.1  
Model trained on Dell laptop with GeForce GTX 1050 GPU.

## Data
Training data are obtained from https://github.com/chinese-poetry/chinese-poetry
I select only Tang Poetries and only those that are 5 character lines. (五言绝句，五言律诗，etc). That gives us a total of __30379 poetries__.

Dataset is big so I implemented a PyTorch `Dataset` class for looping over the data.

## Data Processing
Original data is in traditional Chinese are converted into Simplified Chinese using `zhconv`.
Data is processed such that each time the input to the model is n characters and model will predict the next character.


## Model 1
For the first attempt, a very simple LSTM model is used. It has only __one LSTM layer__ with __256 hidden units__.

Model is implemented in PyTorch.

## Results
 and the output from just one epoch is not bad.
```
generated = generate_poem(trained_model, "我有紫霞想，", output_length=18, temperature=0.2)
print(generated)
```
何人理白云。朝廷风云外，主人不可知。

Output after 2 epochs:
```
generated = generate_poem(trained_model, "明月几时有，", output_length=18, temperature=0.2)
print(generated)
```
清风吹不闻。今来一何事，自有一生心。

```
generated = generate_poem(trained_model, "八月湖水平，", output_length=18, temperature=0.2)
print(generated)
```
三南真得归。山川无处处，云瀛有时时。

## 分析：
从最开始的jibberish,模型很快（大概1000个step之后）就学会了基本的格式（五个字一句，如何加标点等）。   
学习了更多的数据后，可以看出模型渐渐get到了一些上下句中基本的对仗（e.g. 三-八，山-云，无-有）。但要做到押韵则可能需要更长的sequence（目前只是input前6个字）。


## Model 2:
This time, I set input length to 12 chars. For each poem, 6 padding characters are added to the beginning of the sequence. 
I also used a bigger model, bigger vocab size, and added embedding and dropout layer.
The model architecture is:

PoemGenerationModel(    
  (embedding): Embedding(5196, 256)  
  (lstm): LSTM(256, 256, num_layers=2, batch_first=True)  
  (dropout): Dropout(p=0.2, inplace=False)  
  (linear): Linear(in_features=256, out_features=5196, bias=True)  
) 

## Results:
使用更长的sequence后，随着训练的进行，可以看到逐渐有些押韵了：
```
Loss at epoch 4 step 12000: 4.235178470611572

----- Generating text:
Generating with seed: 青柳映红颜，黄云蔽紫关。
----- temperature: 0.2
不知春色后，不是一年间。
----- temperature: 0.5
衰华一顾意，归去五湖还。
----- temperature: 0.7
人随鹓鹭没，身到树寒青。
----- temperature: 1.0
投书燕小骥，向路困巢颜。
Generating with seed: OOOOOO青柳映红颜，
----- temperature: 0.2
黄花落曙春。不知山水客，何事是春人。
----- temperature: 0.5
华山白日心。闻君同所思，谁能是君心。
----- temperature: 0.7
升沈不得闲。柳孤尘外晚，愁向野乡还。
----- temperature: 1.0
萦云蝉上时。浦门秋浪阔，乡国夜钟迟。
```
对比同样输入的结果：
```
generated = generate_poem(trained_model, "我有紫霞想，", output_length=18, temperature=0.2)
print(generated)
```
不如山水闲。松萝垂绿水，草色拂青山。

```
generated = generate_poem(trained_model, "明月几时有，", output_length=18, temperature=0.2)
print(generated)
```
此夜独悠悠。白日无人见，青山一曲流。
```
generated = generate_poem(trained_model, "八月湖水平，", output_length=18, temperature=0.2)
print(generated)
```
一望青云端。高风吹寒色，远水连秋湍。

## Conclusion 
Overall, I am quite happy with the results, given that the model is not very big and trained on my own laptop for only a few epochs. The model is able to learn the basic structure of Chinese Tang poetry and produce reasonably looking poetries (Definitely much better than what I could do!)

I'll be intested to try out attention model in the future.



