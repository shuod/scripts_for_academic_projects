# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:54:57 2016

@author: Odysseus
"""
import numpy as np
from matplotlib import pyplot as plt
import read_a_cell_in_excel2013
from scipy import stats

# load data file
workbook_name="D:\\cloud\\Dropbox\\9_data\\20150706_Fbench\\log_Fbench_values_used.xlsx"
    
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

row_list = ['19']

for row_name in row_list:
    for col_name in col_list:
        B3LYP_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (B3LYP_value)

# prepare the input to np.linalg.lstsq

n=len(B3LYP_value)
print (n)

B=np.array(exp_value)
A=np.array(B3LYP_value)


# solve the equations
slope, intercept, r_value, p_value, std_err=stats.linregress(A,B)

k=slope
b=intercept


#plot the points figure


plt.figure(figsize=(6,6))
plt.scatter(B3LYP_value,exp_value,s=25,alpha=0.4,marker='o')

#plot the fitting curve
start=[min(B3LYP_value)+0.05*min(B3LYP_value),max(B3LYP_value)-0.05*max(B3LYP_value)]
end=[(min(B3LYP_value)+0.05*min(B3LYP_value))*k+b,(max(B3LYP_value)-0.05*max(B3LYP_value))*k+b]

plt.plot(start,end,'r',linewidth=2.0)
plt.plot([-2.51,-8.49],[-2.51,-8.49],'b',linewidth=2.0)

plt.ylabel('Experimental HOMOs')  
plt.xlabel('Predicted HOMOs from KMLYP')

plt.text(-6.8,-7.0,'y='+str(k)+'x'+str(b),color='black',ha='left') 
plt.text(-6.8,-7.5,'std='+str(std_err),color='black',ha='left') 
plt.text(-6.8,-8.0,'corr='+str(r_value),color='black',ha='left')


plt.xlim(-8.5,-2.5)
plt.ylim(-8.5,-2.5)
plt.show()
