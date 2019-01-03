# -*- coding: utf-8 -*-
"""
Function: Place the calculated PCE point on the Sharber model contour map;
          Keep x_gap, y_LUMO the same as in Scharber's paper

Created on Tue Aug 29 03:13:14 2017

@author: Odysseus
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


# read in wavelength <==> short circuit current conversion
df1 = pd.read_csv('Jsc_ASCII.csv')
Jsc=df1['Jsc'].tolist()

df2 = pd.read_csv('M7_HSE06_orbital_energy_to_place_on_pce_map.csv')
Mol_coordinates_X=df2['scaled HSE06 GAP'].tolist()
Mol_coordinates_Y=df2['LUMO'].tolist()


plt.gca().set_aspect('equal', adjustable='box')
plt.rcParams["font.family"] = "Helvetica"


# number of grid intervals
n = 20

y_lumo_lower_limit = -3
y_lumo_higher_limit = -4.1
y_lumo = np.linspace(y_lumo_lower_limit, y_lumo_higher_limit, n)

x_gap_lower_limit = 3
x_gap_higher_limit = 1.4
x_gap = np.linspace(x_gap_lower_limit, x_gap_higher_limit, n)
print(x_gap)
X,Y = np.meshgrid(x_gap, y_lumo)


def f(x_gap,y_lumo):
    """
    Calculate the PCE
    :param x: calculated gap from HSE06 before scaling
    :param y: calculated HOMO from HSE06 before scaling
    :return:
    """

    # Scharber model formula:
    # if x: gap and y:LUMO :
    # abs(y-x) is donor's HOMO, -4.3 is Acceptor's LUMO, 0.65 is the filling factor
    #return ((abs(y-x) - abs(-4.3) -0.3) * par * 0.65/1000)

    # if x:homo and y: gap; return x means x%
    print("LUMO:",y_lumo)
    pce=((abs(abs(y_lumo - x_gap) -abs(-4.3))-0.3) * Current(x_gap_lower_limit, x_gap_higher_limit,n ) * 0.65/1000)*1000
    print("PCE:", pce)
    return(pce)

def Current(x_lower_limit ,x_higher_limit,n):
    """
    return the short circuit current
    :param wn: input the wavelength
    :return: a list of short circuit current value, length = n
    """
    sc=[]

    print("eV:",x_lower_limit)
    print("eV:",x_higher_limit)
    print("=====")

    for wn in np.linspace(x_gap_lower_limit, x_gap_higher_limit, n):
        # 1240/wn to convert between eV and wavelength
        print("wavelength:", 1240 / wn)

        # in the table, the row number and the wavelength have a correspondence: wavelength=rownumber+278
        print("table row number:",1240/wn-278)
        row_number=1240/wn-278
        row_number=round(row_number)

        # to convert numpy.float64  to int, to use as an index for list
        row_number = int(row_number)
        print("value",Jsc[row_number])
        sc.append(Jsc[row_number])
    print(sc)
    return(sc)



# use plt.contourf to filling contours
# X, Y and value for the (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)


# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# adding label
plt.clabel(C, inline=True, fontsize=10)
plt.xlabel('Donor Bandgap (eV)',fontname="Helvetica",fontsize=14)
plt.ylabel('Donor LUMO (eV)',fontname="Helvetica", fontsize=14)
plt.xlim(x_gap_lower_limit,x_gap_higher_limit)
plt.ylim(y_lumo_lower_limit,y_lumo_higher_limit)

#Add points for all moleclues to the PCE contour
#for (x,y) in zip(Mol_coordinates_X,Mol_coordinates_Y):
#    plt.scatter(x,y,c='b')

#Add O2N_M7_NO2 to the PCE contour
plt.scatter([2.0],[-4.0],c='b')

plt.show()


