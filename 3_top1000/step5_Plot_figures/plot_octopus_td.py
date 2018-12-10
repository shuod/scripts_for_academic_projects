# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 16:05:29 2014

@author: Odysseus
"""


import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl
import os,sys
import fileinput
import re
import linecache
import prettyplotlib as ppl

import matplotlib as mpl
mpl.rc('font',family='Times New Roman')

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors


data_dir='F:\\data_1000\\avg_absorption'
fig_dir='F:\\data_1000\\abs_graph'

def plot_octopus_spectrum (data_dir, data_name, fig_dir, fig_name):
    x=[]
    y=[]
    datafile=os.path.join(data_dir,data_name)
    for lines in fileinput.input(datafile):
        x.append (lines.split(" ")[0])
        y.append (lines.split(" ")[1])
    color = set2[1]
    fig, ax = plt.subplots(1)
    ax.set_xlabel('Energy/[eV]')
    ax.set_ylabel('Strength Function/[1/eV]')
    ax.set_xlim([0,4.5])
    ax.set_ylim([0,10])


# p1a=ax.scatter(x, y, label=str(names), color=color,alpha=0.5,facecolor=color,edgecolor='black',linewidth=0.15)
    p1a=plt.plot(x,y,'k',label="ID "+data_name.split(".")[0],linewidth=0.75)






# Now add the legend with some customizations.
    legend = ax.legend(loc='upper center', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

# Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
        
        
    output_file=os.path.join (fig_dir,fig_name)
    fig.savefig(output_file)
    plt.close()
    
for root, dirs, files in os.walk(data_dir):
    for names in files:
        data_name=names
        fig_name=names+'abs.png'
        plot_octopus_spectrum(data_dir,data_name,fig_dir,fig_name)
