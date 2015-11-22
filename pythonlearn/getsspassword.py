#coding:utf-8
'''linux系统下须事先安装meow,
因为网页上的密码是6小时替换一次，
所以获取之后自动替换rc中的密码，
使用crontab每6小时更换一次'''
import urllib
import sys
import re
import os
addr = 'HK2.ISS.TF:8989'
## 获取页面
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
##正则获取页面中的含有密码的串
def getInfo(html):
    reg = r'密码.*'
    infogre = re.compile(reg)
    infolist = re.findall(infogre,html)
    return infolist
html = getHtml("http://www.ishadowsocks.com/")
##取出数字密码
reg = r'\d+'
passgre = re.compile(reg)
passwd1 = re.findall(passgre,getInfo(html)[0])
passwd2 = re.findall(passgre,getInfo(html)[2])
rc = open('/root/.meow/rc','w')
rc.write('listen = http://0.0.0.0:4411\nproxy = ss://aes-256-cfb:%s@%s\nlogFile = /var/log/meow.log' %(passwd2[0],addr))
rc.close()
os.system('killall MEOW')
os.system('/usr/local/meow/MEOW &')
