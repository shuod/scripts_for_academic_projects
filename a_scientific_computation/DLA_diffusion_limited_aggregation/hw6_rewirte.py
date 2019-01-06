# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:17:39 2017

@author: Odysseus
"""

# -*- coding: utf-8 -*-
import new_DLA_adding_new_particle
import os
import numpy as np
from matplotlib import pyplot as plt
import DLA_adding_new_particle



"""
step1
Generate the substrate surface to play with.
"""
x_Grid=50
y_Grid=100
substrate_surface = np.zeros((x_Grid,y_Grid))
ParticlesOnSurface = 0

data_filename = "DLA_200x600_3000p.dat"

"""
step2
Put a particle in the middle of the left edge on the surface.
"""
substrate_surface[int((x_Grid-1)/2),0] = 1
l_current_length=1
    

#np.save("DLA_200x600_3000p", substrate_surface)


while (ParticlesOnSurface < 20) :
    
    #substrate_surface=np.load(data_filename)
    while (l_current_length < y_Grid - 1):
        l_current_length, growth,substrate_surface = new_DLA_adding_new_particle.new_DLA_adding_new_particle(substrate_surface,x_Grid,y_Grid,l_current_length)
    #os.remove(data_filename)
    #np.save("DLA_200x600_3000p", substrate_surface)



# count how many particles are there on the surface now
    if growth:
        ParticlesOnSurface = ParticlesOnSurface + 1
        
    print (l_max_height)

    
# plot the result
    
# np.save("DLA_200x600_3000p", substrate_surface)



fig, ax = plt.subplots()
heatmap = ax.pcolor(substrate_surface)

#ax.set_xticks(np.arange(substrate_surface.shape[1]) + 0.5, minor=False)
#ax.set_yticks(np.arange(substrate_surface.shape[0]) + 0.5, minor=False)

plt.show()
