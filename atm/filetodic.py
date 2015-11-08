#!/usr/bin/env python
def filetodic(dicname,path):
    userlist = file(path)
    #print userlist
#    dicname = {}
    for line in userlist.readlines():
#	print line
	new_line = line.split()
#	print new_line
#	print new_line[1],new_line[0]
	dicname[new_line[0]] = new_line[1]
    print dicname
if __name__ == '__main__':
	filetodic()
