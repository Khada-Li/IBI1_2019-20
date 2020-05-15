# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:37:29 2020

@author: hp
"""

# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
# make array of all susceptible population 
population = np. zeros ( (100 , 100) )
# choose outbreak point
outbreak = np.random. choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# make the plot
plt.figure(figsize=(6,4),dpi=150) 
plt.imshow(population,cmap='viridis',interpolation='nearest') # big purple square (all susceptible people) with only one small dot at a random position representing the one infected person (in yellow)
# define basic variables
β = 0.3
γ = 0.05
for t in range(0,101):   
    infected = np.where(population==1)
# get x, y coordinates 
    for i in range(len(infected[0])):
        x = infected[0][i]
        y = infected[1][i]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
    infected = np.where(population==1)
    for i in range(len(infected[0])):
        x = infected[0][i]
        y = infected[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-γ,γ])[0]+1 
# make the plot
    plt.figure (figsize=(6,4),dpi=150) 
    plt.imshow(population,cmap='viridis',interpolation='nearest')
