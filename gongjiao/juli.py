import math
def circle(x,y):
#       global x
#       global y
        lat_b= 37.466839
        lng_b = 121.444287
        pk = 180 / 3.14
        lat_a = float(x)
        lng_a = float(y)
        a1 = lat_a / pk
        a2 = lng_a / pk
        b1 = lat_b / pk
        b2 = lng_b / pk
        t1 = math.cos(a1) * math.cos(a2) * math.cos(b1) * math.cos(b2)
        t2 = math.cos(a1) * math.sin(a2) * math.cos(b1) * math.sin(b2)
        t3 = math.sin(a1) * math.sin(b1)
        tt = math.acos(t1 + t2 + t3)
        dis =  6366000 * tt
        #return dis
        print dis
circle(37.466825,121.444283)

