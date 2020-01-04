# -*- coding: utf-8 -*-
# geometric probability - approximate pi

"""
Created on Mon Nov 12 19:34:33 2012

@author: Ramanathan
"""
#clear screen
import os
os.system('cls')


import numpy as np
import pylab as py

n_samples = 10000
saved_pts=[]
j=0


a=np.random.rand(n_samples)-0.5
b=np.random.rand(n_samples)-0.5

for i in xrange(1,n_samples):
    if a[i]**2+b[i]**2>0.5**2:
        j=j+1
    else:
        saved_pts.append(i)

print('An estimate of pi='+str(4*(1-1.0*j/n_samples)))

py.figure(1, figsize=(4, 3))
py.xlabel('X')
py.ylabel('Y')
py.scatter(a,b)
for k in saved_pts:
    py.scatter(a[k],b[k],c='r')
py.show()