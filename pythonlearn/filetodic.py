# -*- coding: cp936 -*-
##登录
def filetodic1(dicname,path):
    dicname = {}
    listfile = file(path)
    for line in listfile.readlines():
        new_line = line.split()
        dicname[new_line[0]] = new_line[1]
if __name__ == '__main__':
    filetodic(dicname,path)
