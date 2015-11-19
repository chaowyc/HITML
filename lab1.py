# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 00:23:28 2015

@author: chaowyc
"""
from random import Random
import math
import matplotlib.pyplot as plt 
from numpy import *
import numpy as np 
from decimal import Decimal
#create the data set
def create_data(A, xrangel, xranger, xstep, biasvalue, matsize):
    y = [0]
    x = [0]
    length = int(xranger / xstep) 
    print length
    Mat = np.zeros((Decimal(length), Decimal(matsize + 1)))
    xtmp = xrangel
    counter = 1
    while counter < length:
        ytmp = A * math.sin(8 * xtmp)
        ytmp = ytmp + random.normal(0, 1)
        y.append(ytmp)
        xtmp += xstep
        x.append(xtmp)
        counter += 1
    for i in range(0, length):
       Mat[i, 0] = 1
    for j in range(1, matsize):
        Mat[:, j] = np.power(x, j)
    Mat[:, j + 1] = y
    return Mat
#plot the data
def draw_plt(x, y):    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y)
    plt.show()   

def computecost(x, y, theta):
    pre = np.dot(x, theta)
    loss = pre - y
    m = len(y)
    return np.sum(loss ** 2) / (2 * m)

def grendientdescent(x, y, theta, alpha, iterations, history):
    
    xtran = x.transpose()
    m = len(y)
    for itera in range(iterations):
        pre = np.dot(x, theta)
        loss = pre - y
        cost = Decimal(np.sum(loss ** 2) / (2 * m))
        #print("Iteration %d | Cost: %f" % (itera, cost))
        grendient = np.dot(xtran, loss)
        theta = theta - (alpha / m) * grendient
        history[itera] = cost
    return theta
 
# Some gradient descent settings
iterations = 150
alpha = 0.01
J_history = np.zeros((Decimal(iterations), Decimal(1)))

print "end of 0"
size = 1.0
#while size != 0:
left = 0.0
right = size
step = 0.1
A = 3
bias = A * 1
matsize = 10
mat = create_data(A, left, right, step, bias, matsize)
xsize = 5
x = mat[:, 0:xsize]
y = mat[:, matsize:matsize + 1]
theta = np.zeros((xsize, 1))
theta = grendientdescent(x, y, theta, alpha, iterations, J_history)

plt.figure(1)
plt.title("cost funtion")
costx = range(len(J_history))
plt.plot(costx, J_history)
    
plt.figure(2)
plt.title("fiting")
draw_plt(mat[:, 1], mat[:, matsize])
fitx = np.arange(0, size, 0.01)
fity = 0
fity2 = 0
for i in range(xsize):
    fity += np.power(fitx, i) * theta[i]
 #np.power(fitx, 6) * theta[6] + np.power(fitx, 5) * theta[5] + np.power(fitx, 4) * theta[4] + np.power(fitx, 3) * theta[3] + np.power(fitx, 2) * theta[2] + np.power(fitx, 1) * theta[1] + np.power(fitx, 0) * theta[0]

#fity2 = np.power(fitx, 2) * theta[2] + np.power(fitx, 1) * theta[1] + np.power(fitx, 0) * theta[0]
plt.plot(fitx,fity)

plt.margins(0.2)
plt.show()

coeffs = np.polyfit(mat[:, 1], mat[:, matsize], 5)
print coeffs
plt.figure(3)
draw_plt(mat[:, 1], mat[:, matsize])
p = np.poly1d(coeffs)
plt.plot(fitx, p(fitx))

