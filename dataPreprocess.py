# -*- coding: utf-8 -*-
import re
import os
import jieba


def dataClean(content, filename):
    # 清洗文本数据-用正则表达式删去数字、字母、标点符号、特殊符号等
    symbols = "[A-Za-z0-9\!\%\[\]\,\。\.\，\、\~\?\(\)\（\）\？\！\“\”\:\：\;\"\"\；\……&\-\_\|\．\Ａ．Ｂ．Ｃ\*\^]"
    comments = re.sub(symbols, '', content)

    # jieba分词
    comments_list = jieba.cut(comments)              # 精确模式
    x_train = ' '.join([x for x in comments_list])   # 用空格连接分好的词

    # 保存数据
    with open('./tmp_data/' + filename, 'w', encoding='utf8') as f:
        f.write(x_train)


def dataProcess():
    if len(os.listdir("./tmp_data")) != 0:
        return
    for filename in os.listdir("./data"):
        with open("./data/" + filename, "r", encoding = "utf-8") as f:
            dataClean(f.read(), filename)

