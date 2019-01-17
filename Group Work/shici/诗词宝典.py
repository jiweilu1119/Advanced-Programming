from bs4 import BeautifulSoup
import urllib
import sys
import re
import requests
import lxml

reload(sys)
sys.setdefaultencoding('utf8')


#通过类文件对象创建BeautifulSoup对象
def get_html1():
    url = "http://www.guoxuedashi.com/shici/"
    page = urllib.urlopen(url)
    #Urllib库用urlopen()返回的就是一个类文件对象
    soup = BeautifulSoup(page,"html.parser")
    return soup

def get_data(soup):
    with open('/Users/jiweilu/Desktop/sc/content.txt','a') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
        f.write("诗词宝典共有"+str(len(soup.select('dl.clearfix')))+"个朝代的诗词"+"\n")
        for dl in soup.select('dl.clearfix'):
            f.write(dl.get_text()+"\n")

    for chaodai in soup.select('dl.clearfix'):
    #获取每一个朝代div(目标内容）
        a_hrefs=chaodai.find_all("a")
        a_name=chaodai.find('dt')#获取朝代名称

        for a_href in a_hrefs: #遍历朝代具体目录  秦：诗经、先秦无名、屈原。。。。。。
            href=a_href.get("href")#当前元素的url
            #接下来进入例如：诗经页的内容
            url ="http://www.guoxuedashi.com"+href
            page = urllib.urlopen(url)
            Soup = BeautifulSoup(page,"html.parser")
            filename='/Users/jiweilu/Desktop/sc/shici/'+a_name.get_text()+a_href.get_text()+'.txt'
            with open(filename,'a') as f:
                    #爬取第二层（诗词目录页）至第三层（诗词具体内容页面）的链接
                    mulu=Soup.find('div',{'class':'info_cate clearfix'}).find_all('a')
                    #获取每一首诗的具体内容
                    for mulu_href in mulu:
                        url ='http://www.guoxuedashi.com'+mulu_href.get("href")
                        page = urllib.urlopen(url)
                        shici_soup=BeautifulSoup(page,"html.parser")
                        shici=shici_soup.find('div',{'class':'info_txt2 clearfix'})
                        if(shici.get_text() != ""):
                            f.write("\n"+shici.get_text()+"\n")
                        else:
                            f.write("无该诗词内容")

get_data(get_html1())
