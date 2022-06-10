# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:29:39 2019

@author: L
"""

import requests
from bs4 import BeautifulSoup
from package.file import *

url='http://mst168.idv.tw/tarot/TAROS/zhougong.asp?jiemong=權杖王后'
result=[]
# 下載 Yahoo 首頁內容
r = requests.get(url)
r.encoding='utf-8' #显式地指定网页编码，一般情况可以不用
# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')
  stories = soup.find_all('p')
  for s in stories:
#     print(s.text)
     result.append(s.text)
       
index=[12,13,14,15,16,24,25,26,27,31]
result[17]
T = [result[i].replace('\n','').replace(' ','') for i in index]

#T[6]
#T[7]
#T[8]
#T[9]
from package.WebCrawler import *
import os.path

#WebCrawler.figure(url=url,config=True,rule='D:/iii/exp_data/webcraw/tarot/config.txt')
#out=WebCrawler.soup()
Reader.clr()
#Reader.figure(path='D:\gg.csv')
pathway=Reader.get_UpperPath('.')+'/190709github_package_data/tarot.txt'
Reader.figure(path=pathway,config=True)

#Reader.figure(path=out+'/190709github_package190709github_package_data/tarot.txt',config=True)

#Reader.figure(path='D:/iii/Algorithm/MARG Filter/python../190709github_package/tarot.txt',config=True)
#Reader.figure(path='./bb.txt',config=True)
url_c_list=Reader.export()

#url_c_list=np.array(out,dtype=str)
url_m='http://mst168.idv.tw/tarot/TAROS/zhougong.asp?jiemong='
#url_m+url_c_list[0][0]
Writer.figure(path='bb.csv')
d=False
for url_c in url_c_list:
    if url_c=='權杖王后':
        d=True
        continue
    if d:
        url=url_m+url_c[0]
        
        print('surfing...',url)
        WebCrawler.figure(url=url,config=True,rule='D:/iii/exp_data/webcraw/tarot/config.txt')
        out=WebCrawler.soup()
        out=np.array(out)
        temp=np.array([url_c]).flatten()
        out=np.hstack((temp,out))
        try:
            Writer.appendstring(out) 
        except:
            Writer.appendstring(np.array([url_c,'error'])) 
            
Writer.close()
#Writer.figure(path='out.csv')
#a=np.array(['dsaf','dsf'])
#Writer.appendfile(a)
#
#x=np.linspace(0,100,1000)
#x
#str(tuple(x.reshape(1, -1)[0])).replace('(','').replace(')','\n')

#x=''
#for i in range(len(T)):
#    x=x+T[i]+', '


#x=''
#for i in range(len(T)):
#    x=x+T[i]+', '
#x.replace('\n','')
#x.replace(':',', ')
#x
