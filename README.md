# chinese_poetry_generator 唐诗生成器
Chinese poetry generator using deep learning models (LSTM CharRNN)

基于PyTorch的LSTM CharRNN模型，给定第一句五个字，自动生成五言唐诗。


## Data
Training data are obtained from https://github.com/chinese-poetry/chinese-poetry
I select only Tang Poetries and only those that are 5 character lines. (五言绝句，五言律诗，etc）

## Data Processing
Original data is in traditional Chinese are converted into Simplified Chinese using `zhconv`.
Data is processed such that each time the input to the model is 6 characters and model will predict the next character.

## Model
For the first attempt, a very simple LSTM model is used. It has only __one LSTM layer__ with __256 hidden units__.

Model is implemented in PyTorch.

## Results
A total of 30379 poetries were used in training and the output from just one epoch is not bad.
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

可以看出，模型学习到了一些上下句中基本的对仗（e.g. 三-八，山-云，无-有）。但要做到押韵则可能需要更长的sequence（目前只是input前6个字）。


