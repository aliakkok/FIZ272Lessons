#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:01:26 2020

@author: aliko
"""

import numpy as np
import matplotlib.pyplot as plt

coeff=1.6

times = np.linspace(0,3.5,100)
tstep = (max(times)-min(times))/len(times)

no_drag_velocities = 9.8*times

a=0
v=0
drag_velocities = []
for i in times:
    drag_velocities.append(v)
    a=9.8-coeff*v**2*tstep
    v=v+a*tstep

plt.plot(times,no_drag_velocities,label="Sürtünmesiz") 
plt.plot(times,drag_velocities,"--",label="Sürtünmeli" )
plt.xlabel("Zaman [s]")
plt.ylabel("Hız [m/s]")
plt.legend(loc="upper right")
plt.show()