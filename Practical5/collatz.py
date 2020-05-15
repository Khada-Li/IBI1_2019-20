# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:14:26 2020

@author: hp
"""

n=100

for i in range(40):
    
    if n%2==0:
        n=n/2
        print(n)
    elif n%2==1:
        n=n*3+1
        print(n)