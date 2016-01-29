#!/usr/bin/env python
from  pyquery  import PyQuery as pq
import requests
url = 'http://www.zhihu.com/topic/19552832'
key = '.question_link'
r = requests.get(url)
p = pq(r.text).find(key)
for i in p:
    q = pq(i).text()
    print q 
    print 'https://www.zhihu.com'+pq(i).attr('href')
