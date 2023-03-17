#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:07:37 2023

@author: shannu
"""

# Projectile motion simulation.
from matplotlib import pyplot as pp
import math

def updatePosition(initialposition,initialspeed,acceleration,time):
    newposition = initialposition+initialspeed*time+.5*acceleration*time**2
    return newposition

g = 9.81 #gravity at Earth's surface
x0 = 0  #initial x position, m
y0 = 10 #inital height, m
acceleration_x = 0
acceleration_y = -g

#muzzle velocity, m/s
v0 = 20
launchAngle = 30

v0_x = v0 * math.cos(math.radians(launchAngle))
v0_y = v0 * math.sin(math.radians(launchAngle))


x = [x0]
y = [y0]

time = [0] #list for storing the elapsed time
dt = 0.1 #time step
while y[-1] >= 0:
    # Update x, y, and time variables
    x.append(updatePosition(x0, v0_x, acceleration_x, time[-1] + dt))
    y.append(updatePosition(y0, v0_y, acceleration_y, time[-1] + dt))
    time.append(time[-1] + dt)


#plot the projectile!
pp.plot(x,y)
pp.xlabel('x (m)')
pp.ylabel('height (m)')
pp.savefig('plot.png')