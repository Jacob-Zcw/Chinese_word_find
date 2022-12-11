# -*- coding: utf-8 -*-
from dataPreprocess import dataProcess
from fileSplit import fileSplit

import os
from gensim.models import word2vec


def modelTrain():
    if os.path.exists("word2vec.model"):
        return word2vec.Word2Vec.load("word2vec.model")
    
    # 中文预料处理
    sentences = word2vec.PathLineSentences("./tmp_data/")

    # vector_size是神经网络的隐藏层单元数，也就是后续每个词向量的维度，默认为100
    model = word2vec.Word2Vec(sentences, vector_size = 100, min_count = 1, workers = 5)
    
    if os.path.exists("./word2vec.model") == False:
        model.save("word2vec.model")
    
    return model

if __name__ == "__main__":
    # csv文件分割
    fileSplit('./oringin_datasets/ChnSentiCorp_htl_all.csv')
    
    # 数据预处理
    dataProcess()
    
    # word2vec模型训练与保存
    model = modelTrain()

    # 输入关键字，例如：价格
    keyword = input("Please enter the keyword: ")

    # 查找语料库中，意思与keyword，相似度最高的3个词
    print(model.wv.most_similar([keyword], topn=3))

