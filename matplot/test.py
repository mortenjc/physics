#!/usr/bin/python

from pylab import *

t = np.arange(0.0, np.pi*2, 0.01)
s = sin(t)

for i in range(1,21):
  subplot(5,4,i)
  s = s + np.sin(i*t)
  plot(t, s)

show()
