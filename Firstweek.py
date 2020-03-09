#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:53:48 2020

@author: aliko
"""

#firstweek

import numpy as np
import matplotlib.pyplot as plt
def dif(t,v):
    return 1-v**2
def euler_scalar(f,t_initial,t_final,y_in,N):
    vt=np.linspace(t_initial,t_final,N)
    res = np.zeros(N,dtype=type(y_in))
    h=vt[1]-vt[0]
    res[0] = y_in
    for k in range(1,N):
        res[k] = res[k-1]+h*f(vt[k-1],res[k-1])
    return (vt,res)
(vt,res) = euler_scalar(dif,0.0,4.0,0.0,5000)
plt.plot(vt,res,vt,np.tanh(vt),'--')
plt.grid()
plt.show()
