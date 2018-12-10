# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Function: Extract HOMO and LUMO values from a single file; provide basic function for "extract_homolumo_folder_difflevels.py"
@author: Shuo Dai
Created on Thu Sep 24 17:57:15 2015
"""

import sys

def extract_homolumo_singlefile(filename):
    block='Population'
    eigen='eigenvalues'
    occst='occ'
    virst='vir'
    sepst='--'
    f=open(filename,'r')
    print (filename)
    txt=f.read().splitlines()
    f.close()

    for line in txt :
        if line.find(block) > -1 or line.find(eigen) > -1 :
            if line.find(block) > -1 :
                eocc=[]
                evir=[]
            elif line.find(occst) > -1 :
                data=line.split(sepst)[1]
                eocc=eocc+[float(i) for i in data.split()]
            elif line.find(virst) > -1 :
                data=line.split(sepst)[1]
                evir=evir+[float(i) for i in data.split()]
                
    if len(eocc) > 0 : 
        homo_value=max(eocc)*27.212        
#        print ("  HOMO : %3.2f " % homo_value)
    if len(evir) > 0 : 
        lumo_value=min(evir)*27.212        
#        print ("  LUMO : %3.2f " % lumo_value)
    
    return (homo_value, lumo_value)
    
if __name__ == "__main__":    
    
    
    filename='D:\\cloud\\Dropbox\\9_data\\20150706_Fbench\\M1\\S1\\cfmu\\M1_S1_cfmu_B1B95.out'
    
    homo_value,lumo_value=extract_homolumo_singlefile(filename)
          
    print ("  HOMO : %3.2f " % homo_value)
    print ("  LUMO : %3.2f " % lumo_value)
