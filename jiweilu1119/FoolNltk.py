import fool
#fool里有初始定义文件：init.py: ["load_model", "cut", "pos_cut", "ner", "analysis", "load_userdict", "delete_userdict"]
#load_model（）: 加载分词训练模型


text = "一个傻子在北京"
print(fool.cut(text))




#用户可自定义辞典，词的权重越高，词的长度越长就越越可能出现,　权重值请大于1
fool.load_userdict('/Users/jiweilu/Desktop/1.txt')
text = ["我在北京天安门看你难受香菇", "我在北京晒太阳你在非洲看雪"]

print(fool.cut(text))

fool.load_userdict('/Users/jiweilu/Desktop/1.txt')
text = ["我在北京天安门看你难受香菇", "我在北京晒太阳你在非洲看雪"]
print(fool.cut(text))

fool.load_userdict('/Users/jiweilu/Desktop/2.txt')
text = ["我在北京天安门看你难受香菇", "我在北京晒太阳你在非洲看雪"]
#[['我', '在', '北京天安门', '看', '你', '难受', '香菇'],
# ['我', '在', '北京', '晒太阳', '你', '在', '非洲', '看', '雪']]
print(fool.cut(text))


text = ["一个傻子在北京"]
print(fool.pos_cut(text))


text = ["一个傻子在北京","你好啊"]
words,ners = fool.analysis(text)
print(ners)

ners = fool.ner(text)
print("ners:", ners)

words=fool.cut(text, ignore=True)
words[:6]
print(words)



#[[(5, 8, 'location', '北京')]]

#5 8 表示北京在字符串5-8位置之间，即6和7，见lexial.py的ner函数定义


#删除自定义字典；
fool.delete_userdict();
