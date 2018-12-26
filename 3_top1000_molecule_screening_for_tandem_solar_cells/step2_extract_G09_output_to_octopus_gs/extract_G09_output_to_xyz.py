#
#Function: extract the opimized geometry from Gaussian09 output file to generate the *.xyz coordinate file for octopus input file to call (in the folders named after the Stoichiometric formula.)
#Usage: Put this program together with the html downloaded from CEPDB website and the folders from the G09 calculations (should be ~100 folders) and the octopus template file. After running (no input needed), input files will be created.
#
#Version: 20131231
#Author: Shuo Dai
#
#Environment: win7-64bit with Python 2.7 
#
#Others: This program for Top-1000 calculation and used as step2. 
#

import fileinput
import re
import pybel
import os


base_dir="C:\\Users\\Sapience\\Dropbox\\3_IT\\KLab\\python\\extract_G09_output_to_octopus_gs\\100"
topdown=True

processed_log=open("processed_file_list.txt",'w')

for root, dirs, files in os.walk(base_dir,topdown):
	for name in files:
#		print (name)
		if (name[-3:]=="out"):
			os.path.join(root, name)
#			Gaussian_output=open(os.path.join(root, name),"r")
#			print(Gaussian_output.read())
			output=os.popen("d:\dir").read()
			print (output)
			
			
#		open(".\\"+str(base)+"\\"+str(dir)+"\\"+str(name)+".out","w")
#		processed_log.write(os.path.join(root,name)+'\n')
		
	
