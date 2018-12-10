"""
Function: Generate heatmap from the data 
@author: Shuo Dai
Version Created on Thu Apr 4 13:10:23 2018

"""
import os
import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.axes_style({'font.family': ['Helvetica'],
                'font.sans-serif': ['Helvetica']
                })


plt.rcParams['figure.figsize']=(8,8)



df=pd.DataFrame()
df = pd.read_excel("E:\\cloud\\Dropbox\\0_paper\\5_helix_melanin\\result\\tetramer_stakcing_energies.xlsx",sheetname="rot0pyplot")

print(df)



# vmin is the minimum, vmax is the maximum, you need to divide by 100 in the input if percetile is wanted
ax = sns.heatmap(df, cmap=plt.cm.Blues,vmin=-50, vmax=-200,cbar_kws={'label': 'kJ/mol'})


# the rotation sets the yticks "upright" with 0, as opposed to sideways with 90.
ax.set_yticklabels(ax.get_yticklabels(), rotation = 0,fontsize=24)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 0,fontsize=24)

# for the label
plt.xlabel('x-direction shift',fontname="Helvetica",fontsize=24)
plt.ylabel('y-direction shift',fontname="Helvetica",fontsize=24)





print("Saving to a file.")

plt.savefig('heatmap_of_interaction_rot0.eps', format='eps', dpi=1000)

print("Done.")