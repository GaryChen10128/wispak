# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:01:32 2019

@author: 180218
"""

import requests
from bs4 import BeautifulSoup
from package.WebCrawler import *

#url='https://store.line.me/stickershop/showcase/top/zh-Hant?category=1&page=2'
#result=[]
## 下載 Yahoo 首頁內容
#r = requests.get(url)
#r.encoding='utf-8' #显式地指定网页编码，一般情况可以不用
## 確認是否下載成功
#if r.status_code == requests.codes.ok:
#  # 以 BeautifulSoup 解析 HTML 程式碼
#  soup = BeautifulSoup(r.text, 'html.parser')
#  stories = soup.find_all('p',class_='mdCMN05Ttl')
#  for s in stories:
##     print(s.text)
#     result.append(s.text)
#
#


        
#WebCrawler.figure(url=url,config=True,rule='D:/iii/exp_data/webcraw/tarot/config.txt')
#out=WebCrawler.soup()
Reader.clr()

url_c_list=np.arange(0,100000)
#url_c_list=np.array(out,dtype=str)
#url_m='https://store.line.me/stickershop/showcase/top/zh-Hant?category='
url_m='https://store.line.me/stickershop/showcase/top/zh-Hant?page='


#url_m+url_c_list[0][0]
#Writer.figure(path='testcp950.csv',encoding='cp950')
Writer.figure(path='final.csv',encoding='utf-8-sig')
d=True
for url_c in url_c_list:

    if d:
#        for page in range(1,50):
#            url=url_m+str(url_c)+'&page='+str(page)
            url=url_m+str(url_c)

            print('surfing...',url)
            WebCrawler.figure(url=url,config=True,rule='D:/iii/exp_data/webcraw/line/config.txt',class_='mdCMN05Ttl')
            out=WebCrawler.soup()
            out=np.array(out)
#            for i in range(len(out)):
#                out[i]=str(out[i])
#            out2=[]
#            for i in range(len(out)):
#                out2.append(str(out[i]).encode('utf-8').decode('utf-8'))
#            out=np.array(out2)
#            temp=np.array([url_c]).flatten()
#            out=np.hstack((temp,out))
#            Writer.appendstring(out) 
            if len(out)==0:
                continue
            # Writer.appendstring(out) 
#            try:
#                Writer.appendstring(out) 
#                print('write success')
#            except:
#                Writer.appendstring(np.array([url_c,'error'])) 
            
#        break
                
Writer.close()
