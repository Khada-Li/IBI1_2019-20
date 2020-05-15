# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:28:59 2020

@author: hp
"""

# inout the DNA sequence
seq = 'ATGCGACTACGATCGAGGGCCAT'
re = seq[::-1]
reverse_seq = ''
for i in re:
    if i == 'A':
        reverse_seq+='T'
    elif i =='T':
        reverse_seq+='A'
    elif i =='C':
        reverse_seq+='G'
    elif i =='G':
        reverse_seq+='C'
print('The reverse complementary sequence is',reverse_seq)