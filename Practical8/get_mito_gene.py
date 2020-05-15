# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:44:51 2020

@author: hp
"""

xfile = open('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
data={}
initialdata=''
sign = False
n= 0
for line in xfile:
    line = line.rstrip()
    if not 'R64-1-1:Mito' in line:
        if sign == False:
         continue
        elif '>' in line:
            sign = False
            data[str(n)]=initialdata
            initialdata = ''
            continue
    else:
        sign = True
        n = n+1
    initialdata=initialdata+line
import re
genename=''
temseq=''
noseq=0
genelength=0
finalseq=''
for i in range(1,n+1):
    temseq=data[str(i)]
    genename=re.search(r'gene:(\w+)',temseq)
    genename=genename.group(0)
    for m in range(0,len(temseq)):
        if temseq[m]==']':
            noseq = m+1
    genelength = len(temseq) - noseq
    for h in range(noseq,len(temseq)):
        finalseq=finalseq+temseq[h]
    data[str(i)]= '>Gene:'+ genename+' Length:'+str(genelength)+'bp'+'\n'+finalseq
    genename=''
    temseq=''
    noseq=0
    genelength=0
    finalseq=''
yfile=open('mito_gene.fa','w')
for i in range(1,n+1):
    line=data[str(i)]
    yfile.write(line+'\n')
yfile.close()
zfile=open('mito_gene.fa','r')
for line in zfile:
    line=line.rstrip()
    print (line[:-1])