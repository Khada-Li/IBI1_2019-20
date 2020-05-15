# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:27:16 2020

@author: hp
"""

# import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Input 'full_data.csv'
os.chdir("C:\Li\IBI1_2019-20\Practical7")
print (os.getcwd())
print (os.listdir())  # check the process
covid_data = pd.read_csv("full_data.csv")
print (covid_data.head(8))  # the number of rows with data
covid_data.info()
print (covid_data.describe())
print (covid_data.iloc[0:15:3,:])
# show “total cases” for all rows corresponding to Afghanistan
date_one = covid_data.iloc[:,1]
Boolean_list=[]
for i in range(0,7996):
    if date_one[i]=='Afghanistan':
        Boolean_list.append(True)
    else:
        Boolean_list.append(False)
for n in range(i+1, 7996):
    Boolean_list.append (False)
print (covid_data.loc[Boolean_list, 'total_cases'])
A=[]
for j in range(0,7996):
    if date_one[j]=='World':
        A.append(j)
    else:
        continue
world_dates=covid_data.loc[A,'date']
world_new_cases=covid_data.loc[A,'new_cases']
median_new_cases=np.median(world_new_cases)
mean_new_cases=np.mean(world_new_cases)
# get the mean and median of new cases for the entire world
print('The mean of new cases for the entire world is',mean_new_cases)
print('The median of new cases for the entire world is',median_new_cases)
# make a boxplot
plt.boxplot(world_new_cases,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False)
plt.title('new cases worldwide')
plt.show()
# make boxplots of new cases and new deaths worldwide
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('new cases')
plt.ylabel('Number')
plt.show()
world_new_deaths=covid_data.loc[A,'new_deaths']
plt.plot(world_dates,world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('new deaths')
plt.ylabel('Number')
plt.show()
# answer the question
B=[]
for i in range(0,7996):
    if covid_data.iloc[i,4]<=10 and covid_data.iloc[i,0]=='2020-03-31':
        B.append(True)
    else:
        B.append(False)
print(covid_data.loc[B,'location'])