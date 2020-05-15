# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:48:36 2020

@author: hp
"""

seq=input('DNA sequence:')   
#count the number of bases in the sequence
A=seq.count('A')
T=seq.count('T')
C=seq.count('C')
G=seq.count('G')
# make the dictionary of bases
dic={'A':A,'T':T,'C':C,'G':G}
print('The frequency dictionary :',dic)


# make the pie
import matplotlib.pyplot as plt
labels = 'A','T','C','G'
sizes = (A,T,C,G)
colors = ('purple','gold','red','green')
explode = (0, 0, 0, 0)
plt.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True, startangle=100)
plt.axis('equal')
plt.title('A pie from the frequency table')
plt.show()
