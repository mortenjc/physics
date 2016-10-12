#!/usr/bin/python

from math import *
import scipy.special as spl 

def bessel():
  for i in range(1,360):
    x = i / 6.28
    y1 = spl.jv(1,x)
    y2 = spl.yv(1,x)
    y3 = spl.jv(3,x)
    
    print("%7.3f, %7.3f, %7.3f, %7.3f" % (x, y1, y2, y3))



def csv1():
  for i in range(1,360):
    x = i / 6.28
    y1 = sin(x)
    y2 = cos(x)
    y3 = y1 * y2 / x
    print("%7.3f, %7.3f, %7.3f, %7.3f" % (x, y1, y2, y3))

def csv2():
  for i in range(1,360):
    x = i / 6.28
    y2 = log(x)
    y3 = sqrt(x)
    y1 = log(x) * sqrt(x) 
    print("%7.3f, %7.3f, %7.3f, %7.3f" % (x, y1, y2, y3))


#csv2()
bessel()
