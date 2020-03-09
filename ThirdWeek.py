#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:56:35 2020

@author: aliko
"""

#thirdweek


import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi,sinh
def Euler_stepper(vf,t,v_in,h):
    vdt_v=vf(t,v_in)
    return v_in+h*vdt_v
def euler(f,t_initial,t_final,y_in,Nsteps):
    vt=np.linspace(t_initial,t_final,Nsteps)
    h=vt[1]-vt[0]
    res=np.zeros((y_in.size,Nsteps),dtype=type(y_in[0]))
    res[:,0]=y_in[:]
    for k in range(1,Nsteps):
        res[:,k]=Euler_stepper(f,vt[k-1],res[:,k-1],h)
    return (vt,res)
def analytic(t,v_init):
    return v_init*sinh(t)
def inverted_pendulum(t,y):
    res=np.zeros(2,dtype=float)
    res[0]=y[1]
    res[1]=sin(y[0])
    return res
v_init=0.1
y_in=np.array([0.0,v_init])
(vt,res)=euler(inverted_pendulum,0.0,2*pi,y_in,6000)
plt.plot(vt[::10],res[0,::10],vt[::10],v_init*np.sinh(vt[::10]),'--')
plt.show()
