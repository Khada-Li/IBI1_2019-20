# -*- coding: utf-8 -*-
"""
Created on Thu May 14 06:04:46 2020

@author: hp
"""

# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
N = 10000 # the total number of people in the population
β = 0.3 # infection constant
γ = 0.05 # recovered constant
t = 1000
p = [0]
sus = [9999] # susceptible number
inf = [1] # infected number
rec = [0] # recovered number
# deﬁne an array using square brackets 
result1 = []
result2 = []
for i in range(0,t):
    result1 = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/N),β*(inf[i]/N)])
    result2 = np.random.choice(range(2),inf[i],p=[1-γ,γ])
    n1 = np.sum(result1 == 1)
    n2 = np.sum(result2 == 1)
# add elements to array
    sus.append(sus[i]-n1)
    inf.append(inf[i]+n1-n2)
    rec.append(rec[i]+n2)
    p.append(i)
# make the plot
y1=sus
y2=inf
y3=rec
plt.plot(p, y1, label='susceptible')
plt.plot(p, y2, label='infected')
plt.plot(p, y3, label='recovered')
plt.title('SIR model',fontsize=20)
plt.xlabel('time',fontsize=12)
plt.ylabel('number of people',fontsize=12)
plt.tick_params(axis='both',labelsize=10)
plt.legend(loc='upper right')
plt.figure(figsize=(6,4),dpi=150)
plt.savefig(r'C:\Li\Practical13\figure.png',type='png')

