#!/usr/bin/env python3
from  pyquery  import PyQuery as pq
import requests
import json
import pickle
urls = []
preurl = [] 
postedurl = []
f = open('site.txt','rb')
geturl = 'http://www.linuxu.top/sitemap.xml'
key = 'loc'
r = requests.get(geturl)
p = pq(r.content,parser='html').find(key)
posturl = 'http://data.zz.baidu.com/urls?site=www.linuxu.top&token=Z5j08vXcUXaWpMAa&type=original'
for i in p:
    q = pq(i).text()
    urls.append(q)
preurl = pickle.load(f)
f.close()
for data in urls:
    if data in preurl:
        continue
    else:
        post = requests.post(posturl,data)
        result = json.loads(post.text)
        print(result)
    if result['success'] == 1:
            postedurl.append(data)
f = open('site.txt','ab')
pickle.dump(postedurl,f)
f.close()
