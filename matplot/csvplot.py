#!/usr/bin/python

import sys, pylab as pl, numpy as np

cols = sys.argv[1]
files = sys.argv[2:]
n = len(files)

nc, nr = [1, n]
if (n > 2):
   nc = int(pl.ceil(pl.sqrt(n)))
   nr = int(pl.ceil(1.0 * n / nc))

pl.rcParams.update({'font.size': 8})

for idx, file in enumerate(files): 
  pl.subplot(nr,nc,idx+1)
  data = np.loadtxt(file, delimiter=',')
  x = data[:,0]
  for yi in cols.split():
    y = data[:,yi]
    pl.plot(x,y, lw = 0.5)

pl.legend(cols.split())
pl.show()

