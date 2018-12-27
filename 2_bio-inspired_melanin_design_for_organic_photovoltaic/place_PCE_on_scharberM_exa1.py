# -*- coding: utf-8 -*-
"""
Function: Place the calculated PCE point on the Sharber model contour map

Created on Tue Aug 29 03:13:14 2017

@author: Odysseus
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv('Jsc_ASCII.csv')

Jsc=df['Jsc'].tolist()

par=[0.89,1.01,1.11,1.24,1.37,
     1.5,1.65,1.78,1.93,2.13,
     2.34,2.56,2.79,3.01,3.29,
     3.53,3.8,4.08,4.36,4.69,
     4.97,5.3,5.65,6.03,6.39,
     6.79,7.18,7.63,8.09,8.54,
     9.01,9.52,10.03,10.61,11.17,
     11.8,12.44,13.03,13.73,14.35,
     15.06,15.83,16.43,17.23,18.05,
     18.84,19.70,20.6,21.54,22.33,
     22.96,23.44,24.4,25.5,26.64,
     27.73,28.05,28.05,28.05,28.05]
print(par)
#print(Jsc)
plt.gca().set_aspect('equal', adjustable='box')
plt.rcParams["font.family"] = "Helvetica"

counter=0
def Current(wn):
    Jsc_acc=[]
    for i in wn: 
        for element in i:
            id=int(element)

            #Jsc_acc.append(Jsc[id])

    return(Jsc_acc)

def f(x,y):
    # the height function
    print(x)
    print(len(x))
    return ((abs(y-x) - abs(-4.3) -0.3) * par * 0.65/1000)

n = 60
x = np.linspace(3.1, 1, n)
y = np.linspace(-3, -4, n)
X,Y = np.meshgrid(x, y)
print (1240/x)
# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)
plt.xlabel('Donor Bandgap (eV)',fontname="Helvetica",fontsize=14)
plt.ylabel('Donor LUMO (eV)',fontname="Helvetica", fontsize=14)
plt.xlim(3,1)
plt.ylim(-3,-4)



plt.show()


