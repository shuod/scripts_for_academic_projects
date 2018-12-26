# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:03:00 2015

Dependency: read_a_cell_in_excel2013, openpyxl

Function: Wrapper for openpyxl;Read a range of data from the excel file

@author: Odysseus
"""

import read_a_cell_in_excel2013
import openpyxl
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

workbook_name="D:\\cloud\\Dropbox\\0_paper\\3_bm\\results\\log_Fbench_values_used_v4.xlsx"
    
sheet_name='HOMO'
    
#print (get_column_letter(30))


# read the row 1
    
col_list = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']

row_list = ['6']

exp_value=[]

B3LYP_value=[]

"""
for row_name in row_list:
    for col_name in col_list:
        exp_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (exp_value)
"""
        
"""
col_list = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']
row_list = ['9']

for row_name in row_list:
    for col_name in col_list:
        B3LYP_value.append(read_a_cell_in_excel2013.read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name))
print (B3LYP_value)
"""

wb=openpyxl.load_workbook(workbook_name)
sheet=wb.get_sheet_by_name(sheet_name)

"""
for cellObj in sheet.columns[1]:
    print(cellObj.value)
"""

for cellObj in sheet.rows[8]:
    print(cellObj.value)
        
        