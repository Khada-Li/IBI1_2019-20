# -*- coding: utf-8 -*-
"""
Created on Thu May 14 05:03:08 2020

@author: hp
"""

num = input(r"Please input numbers to compute 24 (use ',' to divide them): ")
number = []
for value in num.split(","):
   number.append(float(value))
   flag = False
while flag == False:
    flag = True  
    for value in number:
       if value > 23 or value < 1:
         flag = False
         print("Error!" + str(value) + "The numbers should be between 1 to 23 in integer.")
         num = input(r"Please input numbers to compute 24: (use ',' to divide them): ")
         number = []
         for value in num.split(","):
            number.append(float(value))
         break
def f(l: int):
   a = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             a.append([i, j, k])
   return (a)
num_x = [[], []]
for i in range(2, len(number) + 1):
   num_x.append(f(i))
num_y = []
num_z = []
for i in range(len(number)):
   num_z.append(num_x[len(number) - i])
   
def t(l: list):
   l_copy = l.copy()
   if len(l_copy) == len(num_z) - 1:
      num_y.append(l_copy)
   for value in num_z[len(l)]:
      l.append(value)
      t(l)
      l.pop()
t([])

# Select one equation from the combination 
def y(i:int, j:int, k:int, l:list):
    fin = 0 
    if k == 0:
        fin = l[i] + l[j]
    elif k == 1:
        fin = l[i] - l[j]
    elif k == 2:
        fin = l[j] - l[i]
    elif k == 3:
        fin = l[i] * l[j]
    elif l[j] != 0 and l[i] != 0 :
        if k == 4:
            fin = l[i] / l[j]
        else:
            fin = l[j] / l[i]
    if fin == 24:
        return (0)
    else:
        l[i] = op
        l.pop(j)       
 
# Prepare for the output
q = 0   
n = 1
for value in num_y:
     number_copy=number.copy()
     for m in value:
         if y(m[0], m[1], m[2], number_copy) ==0 and q == 0:
            print("Yes")
            print("Recursion Times: " + str(n))
            q = 1
         else:
            n = n + 1
if q == 0:
    print("No")
