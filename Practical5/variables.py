# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:17:57 2020

@author: hp
"""

a=857
b=857857
c=b/7
print("c=",c)
d=c/11
print("d=",d)
e=d/13
print("e=",e)

if a>e:
    print("a is greater than e")
elif a==e:
    print("a is equal to e")
else:
    print("e is greater than a")

# boolean
X=eval(input('(Please enter True or False) X='))
Y=eval(input('(please enter True or False which is different from X) Y='))
Z=(X and not Y) or (Y and not X)
W= (X!=Y)
if X==True and Y==False:
    print('Is Z True or False? Z=',Z)
elif X==False and Y== True:
    print('Is Z True or False? Z=',Z)
if Z==W:
    print('W and Z are the same')
else:
    print('W and Z are not the same')
