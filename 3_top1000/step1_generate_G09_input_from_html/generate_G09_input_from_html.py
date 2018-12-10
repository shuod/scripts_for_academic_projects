#
#Function: extract SMILE code from local html file and generate the gaussian input file (in the folders named after the Stoichiometric formula.)
#Usage: Put this program and the html downloaded from CEPDB website together. After running (no input needed), folders and input files will be created.
#
#Version: 20131228; 20140105
#Author: Shuo Dai
#
#Environment: win7-64bit with Python 2.7 
#
#Others: This program for Top-1000 calculation and used as step1. 
#

import fileinput
import re
import pybel
import os

G09_command="#B3LYP/6-31++G(d,p) opt scf=direct freq test"

#CHANGE HERE 1/2; This is for dealing with the html containing rank 1-100 or 101-200 or 201-300 etc 
#rank1-100: offset=1; rank101-200: offset=101; rank 201-300: offset=201 etc
input_file="CEP Top 1000 molecules   The Harvard Clean Energy Project Database_501-600.htm"
offset=501


#CHANGE HERE 2/2: where to put the input file folders
chk_path="/scratch/shuo/600/ing"


SMILE_counter=0
Stoichiometric_counter=0
URL_counter=0

SMILE=[]
Stoichiometric=[]
URL=[]


#define top_molecules to be dictionary type
#key of the dictionary is SMILE code, which is unique
#vaule of the dictionary is a tuple, which contains the ranking, URL, filename of the image, power conversion coefficient, e(HOMO), e(LUMO), e(GAP), VOC,JSC

top_molecules={}

#each of the molecule is saved in a folder, which contains:
#a data file (1st line: URL, 2nd line: SMILE code), 
#a PNG file downloaded from the CEPDB website,
#a xyz file (using SMILE code as filename), 
#a opt_xyz file (use Gaussian09 to opt),
#a subfolder: Gaussian09 input and output,
#a subfolder: Octopus gs calculations,
#a subfolder: Octopus td calculations,
#a avg_absorption file (energy and strength function),



for line in fileinput.input(input_file):

#	restults: 200. Duipliacation is from differete table cells
#	feature1=re.search("<a href=\"https://cepdb.molecularspace.org/single/",line)
	
	
#search for Stoichiometric formula
#which is used as the input filename for Gaussian09 together with the ranking
	
	feature1=re.search("class=\"center\">C",line)
	
	if feature1:
#		print line.split()[1][15:-5]
		Stoichiometric.append(line.split()[1][15:-5])
		print Stoichiometric[Stoichiometric_counter]
		Stoichiometric_counter=Stoichiometric_counter+1

#search for the SMILE code
#which is used as the comments and filename of PNG from CEPDB

	feature2=re.search("smile:",line)
	if feature2:
		print ("start")
		#works for later Rankds
		print(line.split()[11][23:-5])
		SMILE.append(line.split()[11][23:-5])
		
		
		#works for Rank.100-200
		#print (line.split()[12][8:-5])		
		#SMILE.append(line.split()[12][8:-5])
		
		print(SMILE)
		SMILE_counter=SMILE_counter+1
		print ("stop")
#search for the website of the molecule
#which is used as the comments 

	feature3=re.search("Details...",line)
	if feature3:
#		print (line.split()[1][6:-28])
		URL.append(line.split()[1][6:-28])
		print (URL[URL_counter])
		URL_counter=URL_counter+1
		print ("\n")
		


#Generate the Gaussian input file
#command and comments
print(len(SMILE))
print(SMILE)

counter=0
for counter in range(len(SMILE)):
	print ("Generating the input file for Rank."+str(counter+offset)+" molecule")
	G09_input_filename=str(counter+offset)+"_"+Stoichiometric[counter]+".gjf"
	G09_chk_filename=str(counter+offset)+"_"+Stoichiometric[counter]+".chk"
	G09_comment="Geom opt of Rank."+str(counter+offset)+" candidate from the CEPDB database with SMILE code of "+SMILE[counter]+", HPC, 20131227, Shuo Dai, Gaussian09. The website for this molecule: "+URL[counter]
			

	
#convert SMILE code into coordinate using pybel library
	print ("The smile code: "+SMILE[counter])
	molecule=pybel.readstring("SMI",SMILE[counter])
# forcefield available:  ['gaff', 'ghemical', 'mmff94', 'mmff94s', 'uff']
#	print(pybel.forcefields)
#generate 3D coordinate



#	molecule.make3D()
	
	molecule.make3D(forcefield='mmff94',steps=10000)
	
	
#	molecule_descent=molecule.calcdesc()
#	molecule.data.update(molecule_descent)
	
#set up a folder and write to the file
# *.gjf file generated from the pybel libary has extra words at the beginning.
# we jump over this part and converted  the result with only cartesain part left
			
	path=str(counter+offset)+"_"+Stoichiometric[counter]+'\\'+'G09'
	if not os.path.isdir(path):
		os.makedirs(path)
		
		output=open(".\\"+path+"\\"+G09_input_filename,"w")
		output.write("%chk="+chk_path+"/"+str(counter+offset)+"_"+Stoichiometric[counter]+"/G09/"+G09_chk_filename)
		output.write("\n")
		output.write("%NProcShared=12")
		output.write("\n")
		output.write("%Mem=8000MB")
		output.write("\n")
		output.write(G09_command)
		output.write("\n")
		output.write("\n")
		output.write(G09_comment)
		output.write("\n")
		output.write("\n")
		print("\n")
		print("Gaussian input file content:\n")
		print(molecule.write("gjf")[55:])
		output.write(molecule.write("gjf")[55:])
		output.write("\n")
		output.write("\n")
		output.close()
	
	counter=counter+1
	

		
			
		
		
		