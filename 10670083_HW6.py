# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:07:49 2024

@author: 32535
"""

from bs4 import BeautifulSoup
import requests
List=list()
for page in range(1,75):
    url=f"https://www.lotto-8.com/listltobigbbk.asp?indexpage={page}"
    html = requests.get(url)
    html.encoding='utf-8'
    sp = BeautifulSoup(html.text, 'html.parser')
    sp1 = sp.find("table", "auto-style4")
    sp2 = sp1.find_all("tr")
    for j in range(1,len(sp2)):
        sp3 = sp2[j].find_all("td")
        data = sp3[0].text.replace("\xa0,\xa0", ",").split(",")
        data2 = sp3[1].text.replace("\xa0,\xa0", ",").split(",")
        List.append(data[0])
        List.append(data2)
        print("日期:", data[0])
        print("中獎號碼:")
        for i in range(0,len(data2)):
            print(data2[i], end=" ")
        print("\n特別號: ", sp3[2].text)
        print("=====分隔線=====")
        
