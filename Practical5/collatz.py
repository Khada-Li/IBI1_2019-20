# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:14:26 2020

@author: hp
"""

n=input('Enter a positive integer number:')
def collatz(number):
    r = int(number) % 2
    if r == 0:
        return int(number) // 2
    else:
        return 3 * int(number) + 1
while n !=1:
    print(collatz(n))
    n = collatz(n)