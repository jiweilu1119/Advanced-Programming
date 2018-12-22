
# coding: utf-8

# In[ ]:


'''对词计算频数'''
class BaseProb(object):

    def __init__(self):
        self.d = {}#用来存储分词和分词的个数，键是分词，值是分词的个数
        self.total = 0.0#计数总共的词个数
        self.none = 0

    def exists(self, key):#判断字典self.d中是否存在这个词key
        return key in self.d

    def getsum(self):#返回语self.d中存储的词的总数
        return self.total

    def get(self, key):#判断字典中是否存在这个词key,并且返回这分词的词个数
        if not self.exists(key):
            return False, self.none
        return True, self.d[key]

    def freq(self, key):#计算词key的频率
        return float(self.get(key)[1])/self.total

    def samples(self):#返回字典的键，其实就是返回所有的分词，以列表形式
        return self.d.keys()


class NormalProb(BaseProb):

    def add(self, key, value):
        if not self.exists(key):
            self.d[key] = 0
        self.d[key] += value
        self.total += value


'''对词计数'''
class AddOneProb(BaseProb):#继承BaseProb类，所以BaseProb类中的属性和函数都能用。

    def __init__(self):
        self.d = {}
        self.total = 0.0
        self.none = 1

    def add(self, key, value):
        self.total += value#计算总词数
        if not self.exists(key):#如果这个词key不在self.d中的话，那么在字典中加上这个词，即键为此，并且给这个词计数1，同时总的词数量total加1.
            self.d[key] = 1
            self.total += 1#感觉不应该再加1了，上面都已经计算过总数了？？？？说是后面预测要用到，可能是要平滑
        self.d[key] += value#如果字典已经有这个词了的话，那么给这个词数量加1

