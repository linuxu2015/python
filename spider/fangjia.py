#!/usr/bin/env python3
from  pyquery  import PyQuery as pq
import requests
url = 'http://yantai.fangjia.com/xiaoqu/pn1/#pagelist'
#for i in 
key = '.hover_m'
r = requests.get(url)
p = pq(r.text).find(key)
for i in p:
    q = pq(i).text()
    print(q) 
    #print 'https://www.zhihu.com'+pq(i).attr('href')
