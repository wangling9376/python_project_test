#!/bin/python
#- * - coding:utf-8 - * -

'''
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angele)
    ny = y - step * math.cos(angele)
    return nx,ny
'''

L = []
x=1
HALFL = []
while x<=100 :
    L.append(x)
    x = x+2
print L,len(L)

n=0
while n < len(L)/2:
    HALFL.append(L[n])
    n = n + 1
print HALFL,len(HALFL)