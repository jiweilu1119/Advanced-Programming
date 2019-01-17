
# coding: utf-8

# In[1]:


import requests
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


# In[2]:


from pyquery import PyQuery as pq


# In[3]:


r= requests.get('http://www.guoxuedashi.com/shici/')
r.status_code


# In[4]:


html = r.content


# In[5]:


doc = pq(html)


# In[6]:


doc('dl.clearfix')
pq_cf= doc('dl.clearfix')
# encoding=utf8 
#编写目录
with open('/Users/jiweilu/Desktop/shici/content.txt','a') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
    f.write("诗词宝典共有"+str(len(pq_cf))+"个朝代的诗词"+"\n")
    pq_cf1= doc('.info_content.zj.clearfix')
    items_1=pq(pq_cf1)
    value_c_1 = items_1.text()
    f.write(value_c_1+"\n")
#打印个数


# In[7]:


for pqcf in pq_cf:
    #获取每一个朝代div(目标内容）
    pq_cf_2=pq(pqcf)
    a_hrefs=pq_cf_2('a')
    a_name=pq_cf_2('dt')#获取朝代名称
    
    for a_href in a_hrefs: #某个朝代的类别
        doc1=pq(a_href)('a').attr('href')#当前元素的url
        r2= requests.get('http://www.guoxuedashi.com'+doc1)
        #进入例如：诗经页的内容
        html_2= r2.content
        doc2 = pq(html_2)
        pq_cf2= doc2('.info_txt2.clearfix')+doc2('.info_cate.clearfix')
        items=pq(pq_cf2)
        #获取第二层页面文本
        href1=pq(a_href)
        value_c = items.text()

        if(value_c != ""):
            #print(value_c)
            filename='/Users/jiweilu/Desktop/shici/'+a_name.text()+href1.text()+'.txt'
            with open(filename,'a') as f: 
                f.write(value_c)
            #爬取第二层（诗词目录页）至第三层（诗词具体内容页面）的链接
            pq_cf2('a')
            a2_hrefs=pq_cf2('a')
            #获取每一首诗的具体内容
            for a2_href in a2_hrefs:
                doc2=pq(a2_href)('a').attr('href')
                r3= requests.get('http://www.guoxuedashi.com'+doc2)
                html_3= r3.content
                doc3 = pq(html_3)
                pq_cf3_1= doc3('.info_txt2.clearfix')
                items_3=pq(pq_cf3_1)
                #获取第3层页面文本上半部分(具体的诗词)
                value_c3 = items_3.text()
                if(value_c3 != ""):
                    with open(filename,'a') as f: 
                        f.write("\n"+value_c3)
                else:
                    f.write("\n")
        else:
            f.write("\n")
            
        




    
        
        



# In[44]:


#获取其他部分
pq_cf3_2= doc3('.info_cate.clearfix')
items_3_2=pq(pq_cf3_2)
print(len(items_3_2))

