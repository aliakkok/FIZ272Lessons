#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:58:44 2020

@author: aliko
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi,sinh,pi
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
def pendulum(t,v):
    dv=np.zeros(v.size,dtype=type(y_in[0]))
    dv[0]=v[1]
    dv[1]=-sin(v[0])
    return dv
theta_max=pi/3.
y_in=np.array([theta_max,0.0])
(vt,res)=euler(pendulum,0.0,1.8*pi,y_in,6000)
plt.plot(vt[::10],res[0][::10],vt[::10],res[1,::10],'--')
bo=res[1]>0.0
plt.ylabel('$\\theta$')
plt.xlabel('$t/\sqrt{l/g}$')
plt.show()
print('continuous curve is the angle between vertical direction and the pendulum')
print(' broken curve is the angular velocity')
positive_vt=vt[bo]
T0=2.*pi#unperturbed period

print('half period=',positive_vt.min(),' analytic approximation=',T0/2.*(1.+theta_max**2/16.))