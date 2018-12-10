# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:54:57 2016

@author: Odysseus
"""
import numpy as np
from matplotlib import pyplot as plt
import read_a_cell_in_excel2013


workbook_name="D:\\cloud\\Dropbox\\9_data\\20150706_Fbench\\log_Fbench_values_used.xlsx"
    
sheet_name='HOMO'

col_list = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']

row_list = ['6']

exp_value=[]

B3LYP_value=[]

for row_name in row_list:
    for col_name in col_list:
        exp_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (exp_value)
    

for row_name in row_list:
    for col_name in col_list:
        B3LYP_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (B3LYP_value)


x_d = B3LYP_value
y_d = exp_value
n=len(x_d)

print (x_d)
print (y_d)

B=np.array(y_d)
A=np.array(([[x_d[j], 1] for j in range(n)]))
X=np.linalg.lstsq(A,B)[0]
a=X[0]; b=X[1]
print ("Line is: y=",a,"x+",b)
T=np.arctan2(x_d,y_d)

plt.figure(figsize=(9,6))
plt.scatter(x_d,y_d,c=T,s=25,alpha=0.4,marker='o')
plt.show()
