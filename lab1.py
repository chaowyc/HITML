# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 00:23:28 2015

@author: Understand
"""
import random
import math
import matplotlib.pyplot as plt 
from numpy import *
import numpy as np 

def create_data(xrangel, xranger, xstep, biasvalue):
    y = [0]
    x = [0]
    length = ((xranger - xrangel) / xstep) 
    print length
    Mat = zeros((length + 2, 3))
    xtmp = xrangel
    while xtmp <= xranger:
        ytmp = math.cos(xtmp)
        bias = random.random()
        if bias > biasvalue:
            ytmp = ytmp - (bias - biasvalue)
        y.append(ytmp)
        xtmp += xstep
        x.append(xtmp)
    for i in range(0, int(length) + 2):
       Mat[i, 0] = 1
    Mat[:, 1] = x
    Mat[:, 2] = y
    return Mat

def draw_plt(x, y):    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y)
    plt.show()   

mat = create_data(0.0, 9.0, 0.2, 0.5)
x = mat[:, 0:2]
y = mat[:, 2]
draw_plt(x[:, 1], y)

'''
多项式拟合
y = a0 + a1x + a2x2 + a3x3 +...
代价函数
    平方误差函数
'''

def computer_cost(x, y, m, theta):
    pre = np.dot(x, theta)
    s =0
    for i in range(m):
        s += (pre[i] - y[i]) ** 2
    j = (1 / (2 * m)) * s
    return j
    
m = len(y)
theta = zeros((2, 1))
j = computer_cost(x, y, m, theta)
print j

    




