#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:57:16 2020

@author: aliko
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath
from numpy.linalg import solve

#j=np.imag
M = np.zeros((2,2), dtype = complex)

L = 0.5 #H
C = 1.25 #mikroF
R = 400 #ohm

#w1 ve w2 hesapla

w1 = (complex(0,R) + cmath.sqrt(-R**2. + 4. * (L/C))) / (2.*L)
w2 = (complex(0,R) - cmath.sqrt(-R**2. + 4. * (L/C))) / (2.*L)

#print(w1,w2)

y = np.array([0.0,1/L])
M[0,0] = 1.
M[0,1] = 1.  

def free_osc(w,t):
    exp = np.exp(1.0j * w *t)
    return (exp,1.0*w*exp)

(fr1, dfr1) = free_osc(w1,0)
(fr2, dfr2) = free_osc(w2,0)
M[1,0] = dfr1
M[1,1] = dfr2

x= solve(M,y)
print(x)