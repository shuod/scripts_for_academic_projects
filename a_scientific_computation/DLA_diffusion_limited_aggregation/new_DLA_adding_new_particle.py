# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:39:08 2016

@author: Odysseus
"""
import numpy as np
import random
from matplotlib import pyplot as plt
import matplotlib as mpl


def new_DLA_adding_new_particle(substrate_surface,x_Grid,y_Grid,l_max_length):

    """
    :param substrate_surface:
    :param x_Grid:
    :param y_Grid:
    :param l_current_length:
    :return:

    """


    """
    step4
    Allow the new particle to diffuse. Choose randomly a vector from the four cardinal directions (1,0), (-1,0),(0,1),(0,-1) and move the partcle the distance that the vector indicates.
    That is the array element where the particle used to be is now 0 and the new position is now 1
    """

    """
    step5
    repeat step4 until:
    condition a) The particle height ly rises above the maximum height of the cluster. if this occurs, set the array element to 0 andintroduce a new particle by performing step 3 again.
    condition b) The particle height hits the floor of the cluster(ly=0). if this occurs, set the array element (lx,1) to 1 and return to step3
    condition c) The particle occupies any position adjacent to the first particle. That is, when the moving particle is touching the set particle then it is frozen there. Note that the array can have a maximum height of 2 now.

    """

    """
    step 4 let a new particle to diffuse by choosing a direction
    step 5 repeat 4 until conditons a,b,c satisfied
    
    counter = # of moves
    growth = 1: this run lead to grow; 0 : no growth in this run    
    
    """



#    Introduce a new particle at an empty position

    lx = random.randint(2, x_Grid-1)
    ly = l_max_length

    while (substrate_surface[lx,ly]==1):
        lx = random.randint(2, x_Grid-1)
        ly = l_max_length

    #print(lx,ly)
    counter=0
    growth=0
    l_current_length = l_max_length
    substrate_surface = substrate_surface


#   Check if the particle is born at the edge of an existing crystal. If so, the new particle will stay.


    """
    if lx == x_Grid -1:
        if  substrate_surface[lx,ly-1]==1 or substrate_surface[lx,ly+1]==1 or substrate_surface[lx-1,ly]==1:
                substrate_surface[lx,ly]=1
                growth=1
                l_current_length=l_current_length if l_current_length > ly else ly
                print ("Stay because of the upper boundary.")
                return(l_current_length,growth,substrate_surface)
            
    elif lx == 0:
        if  (substrate_surface[lx,ly-1] ==1 or substrate_surface[lx,ly+1] ==1 or substrate_surface[lx+1,ly] ==1 ):
                substrate_surface[lx,ly]=1
                growth=1
                l_current_length = l_current_length if l_current_length > ly else ly
                print("Stay because of the lower boundary.")
                return(counter,lx, ly, l_current_length,growth,substrate_surface)

    elif 0 < lx < x_Grid-1:
        if  substrate_surface[lx-1,ly]==1 or substrate_surface[lx+1,ly]==1 or substrate_surface[lx,ly+1]==1 or substrate_surface[lx,ly-1]==1:
                substrate_surface[lx,ly]=1
                growth=1
                l_current_length = l_current_length if l_current_length > ly else ly
                print("Stay because of the in substrate boundary.")
                return(l_current_length,growth,substrate_surface)
    """




# Now the particle is going to diffuse within the substrate
    while(lx < x_Grid and lx > 0 and ly <y_Grid and ly >0):
            
# moving a step on a random direction
# 1 = (1,0) = move to right <==> ly=ly+1
# 2 = (-1,0) = move to left <==> ly=ly-1
# 3 = (0,1) = move upward  <==> lx=lx+1
# 4 = (0,-1) = move downward <==> lx=lx-1


        directions = random.randint(1,4)
        counter= counter + 1


        if directions ==1:
            ly=ly+1

        if directions ==2:
            ly=ly-1
    
        if directions ==3:
            lx=lx+1

        if directions ==4:
            lx=lx-1

# if the new move is out of the surface, ignore this run and re-pick another number to move

        if lx > x_Grid-1 or ly > y_Grid-2:
            growth = 0
            print("killed because of out of surface")
            l_current_length = l_max_length - 1
            return (l_current_length, growth, substrate_surface)

# condition a) The particle height ly rises above the maximum height of the cluster. if this occurs, set the array element to 0 and introduce a new particle by performing step 3 again.

        if (ly > l_current_length):
            growth=0
            l_current_length = l_max_length - 1
            print("killed because of condition a")
            return (l_current_length, growth, substrate_surface)



#  condition c) The particle occupies any position adjacent to the first particle. That is, when the moving particle is touching the set particle then it is frozen there. Note that the array can have a maximum height of 2 now.

        if lx == x_Grid - 1:
            if substrate_surface[lx, ly - 1] == 1 or substrate_surface[lx, ly + 1] == 1 or substrate_surface[lx - 1, ly] == 1:
                substrate_surface[lx, ly] = 1
                growth = 1
                l_current_length = l_max_length -1 if l_max_length > ly else ly
                print("stayed because of condition c1")
                return(l_current_length,growth,substrate_surface)

        elif lx == 0:
            if substrate_surface[lx, ly-1] == 1 or substrate_surface[lx, ly+1] == 1 or substrate_surface[lx+1, ly] == 1:
                substrate_surface[lx, ly] = 1
                growth = 1
                l_current_length = l_max_length -1 if l_max_length > ly else ly
                print("stayed because of condition c2")
                return(l_current_length,growth,substrate_surface)

        elif 0 < lx < x_Grid - 1:
            if substrate_surface[lx - 1, ly] == 1 or substrate_surface[lx + 1, ly] == 1 or substrate_surface[lx, ly + 1] == 1 or \
                    substrate_surface[lx, ly - 1] == 1:
                substrate_surface[lx, ly] = 1
                growth = 1
                l_current_length = l_max_length -1 if l_max_length > ly else ly
                print("stayed because of condition c3")
                return(l_current_length,growth,substrate_surface)



# condition b) The particle height hits the floor of the cluster(ly=0). if this occurs, set the array element (lx,1) to 1 and return to step3

        if ly == 0:
            substrate_surface[lx, 0] = 1
            growth = 1
            l_current_length = l_max_length - 1
            print("stayed because of condition b")
            return (l_current_length, growth, substrate_surface)


    return (l_current_length, growth, substrate_surface)

if __name__ == "__main__":    

    """
    step1
    Generate the substrate, a 200x599 array of integers and initialize all elements to 0
    """
    x_Grid=200
    y_Grid=600
    substrate_surface=np.zeros((x_Grid, y_Grid))


    """
    step2
    Introduce a particle at site(100,0). This means set the array element (100,0) to 1. The cluster has now a height of 1
    """


    # first_lx = int((x_Grid-1)/2)
    first_lx = 100
    substrate_surface[first_lx,0] = 1
    l_current_length = 1


    """
    step3
    Introduce a new particle at height 1. here, you will choose a random number lx and set (lx,0) to 1;
    lx != 100 not to overlap with the first particle.
    """

    lx = first_lx
    while (lx == first_lx):
        lx = random.randint(0, x_Grid-1)
    substrate_surface[lx, 0] = 1


    """
    step4 and step5 call function
    """
    l_max_length = 1
    l_current_length = 1
    number_of_particles = 2


    while (number_of_particles < 4001):
        l_current_length, growth, substrate_surface = new_DLA_adding_new_particle(substrate_surface, x_Grid, y_Grid, l_max_length)

        if (growth == 1):
            l_max_length = l_current_length + 1


        print ("The maximum length:", l_max_length)

        if l_current_length > y_Grid -1:
            print("reach the boundary of the substrate_surface at ", lx,l_current_length)
            break

        number_of_particles = number_of_particles + growth
        print ("number of particles:", number_of_particles)



    """
    plot
    """
    
    fig, ax = plt.subplots()
#black and white
    heatmap = ax.pcolor(substrate_surface, cmap= mpl.cm.binary )

#red on blue background
#    heatmap = ax.pcolor(substrate_surface)


    # ax.set_xticks(np.arange(substrate_surface.shape[1]) + 0.5, minor=False)
    # ax.set_yticks(np.arange(substrate_surface.shape[0]) + 0.5, minor=False)

    plt.show()



    
    
    
    
    
    
    