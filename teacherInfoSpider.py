#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
f = open('result.txt','w')
url = 'http://faculty.bjtu.edu.cn/'
for i in range(1,10000):
    strhtml = requests.get(url+str(i))
    if strhtml.status_code == 404:
        continue
    soup=BeautifulSoup(strhtml.text,'lxml')
    data1 = soup.select('div.content1>h1')
    data2 = soup.select('div.main_left>div.mainleft_box')   
    first = True
    for j in data2:
        if j.get_text().find('研究方向') != -1:
            if first:
                if len(data1)>0:
                    f.write(data1[0].get_text())
                    f.write('    '+url+str(i)+'\n')
                    first = False
            f.write(j.get_text())
    f.write('\n\n\n')
print('finish')

