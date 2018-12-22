
# coding: utf-8

# In[ ]:



from __future__ import unicode_literals

import os
import codecs

from .. import normal
from .. import seg
from ..classification.bayes import Bayes

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'sentiment.marshal')


class Sentiment(object):

    def __init__(self):# 实例化Bayes()类作为属性，下面的很多方法都是调用的Bayes()的方法完成的
        self.classifier = Bayes()

    def save(self, fname, iszip=True):# 保存最终的模型
        self.classifier.save(fname, iszip)

    def load(self, fname=data_path, iszip=True):
        self.classifier.load(fname, iszip)# 加载贝叶斯模型

    # 分词以及去停用词的操作
    def handle(self, doc):
        words = seg.seg(doc)# 分词
        words = normal.filter_stop(words)# 去停用词
        return words# 返回分词后的结果，是一个list列表

    def train(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:# 读入负样本
            data.append([self.handle(sent), 'neg'])
            # 所以可以看出进入bayes（）的训练的数据data格式是[[[第一行分词],类别],
            #                                             [[第二行分词], 类别]，
            #                                             [[第n行分词],类别]
            #                                                              ]
        for sent in pos_docs: # 读入正样本
            data.append([self.handle(sent), 'pos'])
        self.classifier.train(data)  # 调用的是Bayes模型的训练方法train()

    def classify(self, sent):
        ret, prob = self.classifier.classify(self.handle(sent))#得到分类结果和概率
        if ret == 'pos':#默认返回的是pos('正面'），否则就是负面
            return prob
        return 1-prob


classifier = Sentiment()#实例化Sentiment()对象
classifier.load()


def train(neg_file, pos_file):
    #读取正负语料库文本
    neg_docs = codecs.open(neg_file, 'r', 'utf-8').readlines()
    pos_docs = codecs.open(pos_file, 'r', 'utf-8').readlines()
    global classifier#声明classifier为全局变量，下面重新赋值，虽然值仍然是Sentiment()函数
    classifier = Sentiment()
    classifier.train(neg_docs, pos_docs)#调用Sentment()模块里的train（）方法


def save(fname, iszip=True):
    classifier.save(fname, iszip)


def load(fname, iszip=True):
    classifier.load(fname, iszip)


def classify(sent):
    return classifier.classify(sent)

