# _*_coding=utf-8 _*_
def pt(*argv):
    #'''将表头定义为一个列表，表头对应的元素'''
    from prettytable import PrettyTable
    l = []
    a = PrettyTable()
    a.align[1] = 'l'
    a.padding_width = 1
    for i in argv:
        l.append(i)
    a.add_row(l)
    print a
#t = ['tt','1','2','3','4','5','6','7',9]
#for x in [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)]:
#    pt(t,x)