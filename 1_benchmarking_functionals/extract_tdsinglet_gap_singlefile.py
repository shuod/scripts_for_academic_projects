# -*- coding: utf-8 -*-
"""
Function: Extract energy gap values from a single Gaussian09 output file 
@author: Shuo Dai
Version: Created on Thu Sep 25 8:20:17 2015

"""

def extract_tdsinglet_gap_singlefile(filename):
    keyword1='Excited State   1:'
   
    data_file=open(filename,'r')
    print (filename)
    txt=data_file.read().splitlines()
    data_file.close()

    for line in txt :
        if line.find(keyword1) > 0:                    
#result : Excited State   1:      Singlet-A      2.8956 eV  428.18 nm  f=1.1095  <S**2>=0.000

            gap = line.split('    ')[2] 
#result :  2.8956 eV  428.18 nm  f=1.1095  <S**2>=0.000           
            
            gap_value= float(gap.split('eV')[0])
#result :  2.8956
            
#            print (gap_value)
            strength=gap.split('f=')[1]
            
            strength_value=float(strength.split(' ')[0])
                
    return (gap_value,strength_value)
    
if __name__ == "__main__":    
    
# use "\\" instead of the "\" in the path!!    
    filename='D:\\cloud\\Dropbox\\9_data\\paper2\\11_H_M7_H_td.out'
    
    gap_value,strength_value=extract_tdsinglet_gap_singlefile(filename)
    
    print ("  Gap : %3.2f " % gap_value)
    print ("  Strength : %3.2f " % strength_value)