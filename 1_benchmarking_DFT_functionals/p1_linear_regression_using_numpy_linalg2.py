# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:54:57 2016

Function: read data from an excel file and make a linear regression figure

@author: Shuo Dai
"""
import numpy as np
from matplotlib import pyplot as plt
import read_a_cell_in_excel2013

# load data file
workbook_name="E:\\cloud\\Dropbox\\9_data\\20150706_Fbench\\log_Fbench_values_used_v2.xlsx"
    
sheet_name='HOMO'

exp_value=[]

B3LYP_value=[]

# read data and make them into an array

col_list = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']

row_list = ['7']

for row_name in row_list:
    for col_name in col_list:
        exp_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (exp_value)
    
col_list = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']

row_list = ['9']

for row_name in row_list:
    for col_name in col_list:
        B3LYP_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (B3LYP_value)

# prepare the input to np.linalg.lstsq

n=len(B3LYP_value)
print (n)

B=np.array(exp_value)
A=np.array(([[B3LYP_value[j], 1] for j in range(n)]))


# solve the equations
X=np.linalg.lstsq(A,B)[0]
k=X[0]; b=X[1]
print ("Line is: y=",k,"x+",b)
T=np.arctan2(B3LYP_value,exp_value)


#plot the scatter figure
plt.figure(figsize=(9,6))

# changing color marker
# plt.scatter(B3LYP_value,exp_value, c=T, s=25, alpha=0.4, marker='o')

# single color marker
plt.scatter(B3LYP_value,exp_value, c='r', s=25, alpha=0.4, marker='o')

#plot the fitting curve

start=[min(B3LYP_value),max(B3LYP_value)]

end=[min(B3LYP_value)*k+b,max(B3LYP_value)*k+b]

plt.plot(start,end,'b',linewidth=2.0, alpha=0.4)

plt.xlim(-6.5,-4.5)
plt.ylim(-6.5,-4.5)

plt.xlabel("Predicted HOMO values (eV)")
plt.ylabel("Experimental HOMO values (eV)")


# To make figure to be square
plt.axis('scaled')
plt.show()

plt.savefig("linear_regression_using_numpy_linalg2.jpg")