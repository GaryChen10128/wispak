# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:26:28 2019

@author: 180218
"""

import requests
from bs4 import BeautifulSoup
from package.WebCrawler import *
out=np.array(['白爛貓☆隨你填貼圖☆初登場','白爛貓☆隨你填貼圖☆初登場'])
Writer.figure(path='test.csv',encoding='utf-8-sig')
Writer.appendstring(out) 
Writer.close()
#import sys
#sys.getdefaultencoding 
#default_encoding = 'gbk'
#if sys.getdefaultencoding != default_encoding:
#    reload(sys)
#    sys.setdefaultencoding(default_encoding)

