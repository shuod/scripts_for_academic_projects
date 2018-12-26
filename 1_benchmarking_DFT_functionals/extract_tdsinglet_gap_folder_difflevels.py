# -*- coding: utf-8 -*-
"""
Function: Extract energy gap values from the Gaussian09 output files in a folder 
Dependency: Call "extract_homolumo_singlefile.py"
@author: Shuo Dai
Version: Created on Thu Sep 25 9:03:10 2015

"""

import extract_tdsinglet_gap_singlefile
import os
import os.path

# use "\\" instead of the "\" in the path!!

start_dir="F:\\3_Melanin\\20170829_M7_B3LYP_paper2_used\\td"

for parent,dirnames,filenames in os.walk(start_dir):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.out':
#            print("filename with full path:"+ os.path.join(parent,filename))
            file_with_fullpath=os.path.join(parent,filename)
            gap_value,strength_value=extract_tdsinglet_gap_singlefile.extract_tdsinglet_gap_singlefile(file_with_fullpath)
            print ("  Gap : %3.2f " % gap_value)
            print ("  Strength : %3.2f " % strength_value)
            
            