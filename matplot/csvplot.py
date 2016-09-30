#!/usr/bin/python

import sys
from pylab import *
import numpy as np

y = []
def main():
   cols = sys.argv[1]
   files = sys.argv[2:]

   c = cols.split() 
   n = len(files)

   if (n <= 2):
      cols = 1
      rows = n
   else:
      cols = int(ceil(sqrt(n)))
      rows = int(ceil(1.0*n/cols))

   rcParams.update({'font.size': 8})

   pi = 1
   for f in files: 
     subplot(rows,cols,pi)
     data = np.loadtxt(f, delimiter=',', skiprows=0)
     x = data[:,0]
     for yi in c:
       y = data[:,yi]
       plot(x,y, lw = 0.5)
     pi = pi + 1
   show()

if __name__ == "__main__":
    main()
