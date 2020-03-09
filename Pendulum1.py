#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:55:40 2020

@author: aliko
"""

#pendulum

import numpy as np
import matplotlib.pyplot as plt
def stepper_pendulum(t,vtheta,h):
    vdt_theta=np.zeros(vtheta.size,dtype=float)
    vdt_theta[0]=vtheta[1]
    vdt_theta[1]=vtheta[0]
    return(vtheta*vdt_theta)
N=2000
mat=np.zeros((2,N),dtype=float)
vtheta_initial=np.array([0.0,0.1])
vtime=np.linspace(0.,20,N) 
mat[:,0]=vtheta_initial[:]
h=vtime[1]-vtime[0]
for k in range (1,N):
    vtheta_initial = stepper_pendulum(vtime[k-1],vtheta_initial,h)
    plt.plot(vtime,mat[0],vtime,0.1*np.sinh(vt))
    plt.grid()
    plt.show()   
