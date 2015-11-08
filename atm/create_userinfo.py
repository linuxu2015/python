#!/usr/bin/env python
import pickle
userinfofile = open('/opt/python/userinfo.pkl','wb')
user_dic = {'xielan':15000,'xulibao':15000}
pickle.dump(user_dic,userinfofile)
userinfofile.close()
userinfofile = open('/opt/python/userinfo.pkl','rb')
dic1 = pickle.load(userinfofile)
print dic1

