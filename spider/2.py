#!/usr/bin/env python3
from  pyquery  import PyQuery as pq
import requests
url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.6.2.X5ymZ2&st_edtime=1&q=ipadmini2&ist=0'
#for i in 
key = ['.item-title','.item-title a','.item-description','.price em']
#key = ['.item-title a']
#key = ['.price em']
r = requests.get(url)
for k in key:
    p = pq(r.text).find(k)
    for i in p:
        q = pq(i).text()
        if k == '.item-title a':
            print('https:'+pq(i).attr('href'))
        else:
            print(q)
