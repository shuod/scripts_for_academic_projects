# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:45:48 2015

Dependency: openpyxl

Function: A wrapper for openpyxl to read arbitrary cell if (row, column) coordinates is given.

@author: Odysseus
"""

def read_a_cell_in_excel(workbook_name,sheet_name,col_name,row_name):

    """
    param: excel file name; column; row
    return: value of the cell
    """

    from openpyxl import load_workbook

    wb = load_workbook(filename = workbook_name) 

    sheet_ranges = wb[sheet_name]

    cell_coordinates = col_name + row_name

#    print (sheet_ranges[cell_coordinates].value)

    return sheet_ranges[cell_coordinates].value

if __name__ == "__main__":    
    
    workbook_name="D:\\cloud\\Dropbox\\9_data\\20150706_Fbench\\log_Fbench.xlsx"
    
    sheet_name='homo from DFT'
    
    col_name1='D'
    
    row_name1='18'
    
    cell = read_a_cell_in_excel(workbook_name,sheet_name,col_name1,row_name1)
    
    print (cell)
    
    