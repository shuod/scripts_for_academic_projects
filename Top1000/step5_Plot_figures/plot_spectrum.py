# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 16:05:29 2014

@author: Shuo Dai
"""


import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl
import os,sys
import fileinput
import re
import linecache
import prettyplotlib as ppl
# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors


#data_dir='F:\\melanin\\avg_absorption'
#fig_dir='F:\\abs_graph'

#data_name='avg_absorption_absorption.txt'
#fig_name=data_name+'abs.png'



data_dir='F:\\data_1000\\avg_absorption'
fig_dir='F:\\data_1000\\abs_graph_indv'

data_name='211_C17H8N4OS2_absorption.txt'
fig_name=data_name+'abs.png'


x=[]
y=[]

datafile=os.path.join(data_dir,data_name)
for lines in fileinput.input(datafile):
    x.append (lines.split()[0])
    y.append (lines.split()[1])
color = set2[1]
fig, ax = plt.subplots(1)
ax.set_xlabel('Energy/[eV]')
ax.set_ylabel('Strength Function/[1/eV]')
ax.set_xlim([4.5,0])
ax.set_ylim([0,5])

# ax.scatter(x, y, label=str(names), color=color,alpha=0.5,facecolor=color,edgecolor='black',linewidth=0.15)
p1a=plt.plot(x,y,label=str("ID "+data_name.split("_")[0]+": "+data_name.split("_")[1]),linewidth=0.75)
#plt.legend(str('ID '+names.split("_")[0]+": "+names.split("_")[1]))
plt.legend()
output_file=os.path.join (fig_dir,fig_name)
fig.savefig(output_file)
    

        
        