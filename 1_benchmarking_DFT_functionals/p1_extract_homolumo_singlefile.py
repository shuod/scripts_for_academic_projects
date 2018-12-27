# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Function: Extract HOMO and LUMO values from a single file; provide basic function for "extract_homolumo_folder_difflevels.py"
@author: Shuo Dai
Created on Thu Sep 24 17:57:15 2015
"""

import sys

def extract_homolumo_singlefile(filename):
    '''

    :param: Gaussian09 output filename:
    :return: HOMO and LUMO values
    '''

    #looking for the keywords:
    block='Population'
    eigen='eigenvalues'
    occst='occ'
    virst='vir'
    sepst='--'

    #open the data file
    with open(filename,'r') as f:
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
        # unit convertion to eV
        homo_value=max(eocc)*27.212        
#       print ("  HOMO : %3.2f " % homo_value)

    if len(evir) > 0 :
        # unit convertion to eV
        lumo_value=min(evir)*27.212        
#       print ("  LUMO : %3.2f " % lumo_value)
    
    return (homo_value, lumo_value)
    
if __name__ == "__main__":    
    
    # location of the data file
    filename='pphr_frag_HSEh1PBE.out'
    
    homo_value,lumo_value = extract_homolumo_singlefile(filename)
          
    print ("  HOMO : %3.2f " % homo_value, "eV")
    print ("  LUMO : %3.2f " % lumo_value, "eV")
