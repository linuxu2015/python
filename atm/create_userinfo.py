#!/usr/bin/env python
import pickle
userinfofile = open('H:\\python\\atm\\userinfo.pkl','wb')
user_dic = {'xielan':15000,'xulibao':15000}
pickle.dump(user_dic,userinfofile)
userinfofile.close()
userinfofile = open('H:\\python\\atm\\userinfo.pkl','rb')
dic1 = pickle.load(userinfofile)
print dic1

