# modified from https://github.com/justdark/pytorch-poetry-gen

#coding:utf-8
import sys
import os
import json
import re

def ParseRawData(author = None, constrain = None):
    rst = []

    def SentenceParse(para):
        # para = "-181-村橋路不端，數里就迴湍。積壤連涇脉，高林上笋竿。早嘗甘蔗淡，生摘琵琶酸。（「琵琶」，嚴壽澄校《張祜詩集》云：疑「枇杷」之誤。）好是去塵俗，煙花長一欄。"
        result, number = re.subn("（.*）", "", para)
        result, number = re.subn("（.*）", "", para)
        result, number = re.subn("{.*}", "", result)
        result, number = re.subn("《.*》", "", result)
        result, number = re.subn("《.*》", "", result)
        result, number = re.subn("[\]\[]", "", result)
        r = ""
        for s in result:
            if s not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
                r += s;
        r, number = re.subn("。。", "。", r)
        return r

    def HandleJson(file):
        # print file
        rst = []
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f, )
            for poetry in data:
#                 print(poetry)
                pdata = ""
                if (author!=None and poetry.get("author")!=author):
                    continue
                p = poetry.get("paragraphs")
                flag = False
                for s in p:
                    sp = re.split("[，！。]", s)
                    for tr in sp:
                        if constrain != None and len(tr) != constrain and len(tr)!=0:
                            flag = True
                            break
                        if flag:
                            break
                if flag:
                    continue
                for sentence in poetry.get("paragraphs"):
                    pdata += sentence
                pdata = SentenceParse(pdata)
                if pdata!="":
                    rst.append(pdata)
            return rst
        # print SentenceParse("")
    data = []
    src = '../chinese-poetry/json/'
    for filename in os.listdir(src):
        if filename.startswith("poet.tang"):
            data.extend(HandleJson(src+filename))
    return data



# if __name__=='__main__':
#     print parseRawData.sentenceParse("熱暖將來賓鐵文，暫時不動聚白雲。撥卻白雲見青天，掇頭裏許便乘仙。（見影宋蜀刻本《李太白文集》卷二十三。）（以上繆氏本《太白集》）-362-。")
#