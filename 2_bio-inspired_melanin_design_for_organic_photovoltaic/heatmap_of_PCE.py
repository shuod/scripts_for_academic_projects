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
df = pd.read_excel("E:\\cloud\\Dropbox\\0_paper\\2\\0_NewResults\\M7_pce.xlsx",sheetname="2D_EWG_H_EDG")

print(df)




ax = sns.heatmap(df, cmap=plt.cm.Blues,vmin=0, vmax=10,cbar_kws={'label': 'PCE (%)'})



ax.set_yticklabels(ax.get_yticklabels(), rotation = 0,fontsize=10)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90,fontsize=11)

plt.xlabel('Side group Ry',fontname="Helvetica",fontsize=12)
plt.ylabel('Side group Rx',fontname="Helvetica",fontsize=10)




print("Saving to a file.")

plt.savefig('heatmap_of_PCE2.eps', format='eps', dpi=1000)

print("Done.")