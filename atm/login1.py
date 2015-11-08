#!/usr/bin/env python
import sys
import pickle
from  menu import menu_show
pkl_path = 'H:\\python\\atm\\userinfo.pkl'
account = file('H:\\python\\atm\\userlist')
account_dict = {}
global user
global left
for line in account.readlines():
    new_line = line.split()
    account_dict[new_line[0]] = new_line[1]
# print account_dict
while True:
    user = raw_input('plz input your name:')
    if user == 'q' or user == 'quit':
        exit()
    while account_dict.has_key(user):
        while True:
            password = raw_input('plz input your password:')
            if password == account_dict[user]:
                print 'welcome to atm'
                userinfofile = open(pkl_path, 'rb')
                userinfo_dic = pickle.load(userinfofile)
                userinfofile.close()
                left = userinfo_dic.get(user)
                # left = 15000
                while True:
                    print 'your money is %s' % left
                    left = menu_show(user, left)
                    userinfo_dic[user] = left
                    userinfofile = open('H:\\python\\atm\\userinfo.pkl', 'wb')
                    pickle.dump(userinfo_dic, userinfofile)
                #		    print type(left)
            else:
                print 'your password is wrong,input again'
        break
    else:
        print 'no this user'
