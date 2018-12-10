# -*- coding: utf-8 -*-
"""
Function: Extract HOMO and LUMO values from the Gaussian09 output files in a folder 
Dependency: Call "extract_homolumo_singlefile.py"
@author: Shuo Dai
Created on Thu Sep 24 18:13:05 2015

"""

import extract_homolumo_singlefile
import os
import os.path

# use "\\" instead of the "\" in the path!!
start_dir="F:\\3_Melanin\\20170829_M7_B3LYP_paper2_used"

for parent,dirnames,filenames in os.walk(start_dir):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.out':
#            print("filename with full path:"+ os.path.join(parent,filename))
            file_with_fullpath=os.path.join(parent,filename)
            homo_value,lumo_value=extract_homolumo_singlefile.extract_homolumo_singlefile(file_with_fullpath)
            print ("  HOMO : %3.2f " % homo_value)
            print ("  LUMO : %3.2f " % lumo_value)
            