# -*- coding: utf-8 -*-
import re
import os
import pandas as pd
import jieba


def dataPreprocess():
    if os.path.exists("./datasets/train.txt"):
        return
    
    # 得到文本数据
    raw_data = pd.read_csv('./datasets/ChnSentiCorp_htl_all.csv')
    text = []
    for i in range(raw_data.shape[0]):
        text.append(str(raw_data.review[i]))
    comment = '\n'.join(text)

    # 清洗文本数据-用正则表达式删去数字、字母、标点符号、特殊符号等
    symbols = "[A-Za-z0-9\!\%\[\]\,\。\.\，\、\~\?\(\)\（\）\？\！\“\”\:\：\;\"\"\；\……&\-\_\|\．\Ａ．Ｂ．Ｃ\*\^]"
    comments = re.sub(symbols, '', comment)

    # jieba分词
    comments_list = jieba.cut(comments)              # 精确模式
    x_train = ' '.join([x for x in comments_list])   # 用空格连接分好的词

    # 保存数据
    with open('./datasets/train.txt', 'w', encoding='utf8') as f:
        f.write(x_train)

