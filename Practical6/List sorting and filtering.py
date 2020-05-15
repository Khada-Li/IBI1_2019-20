# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:30:24 2020

@author: hp
"""

# Input the list of 10 values
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981] 
gene_lengths.sort()
#  remove the two most extreme genes 
del(gene_lengths[0])
del(gene_lengths[len(gene_lengths)-1])
# get the truncated list
print ('The truncated list is :', gene_lengths)
import matplotlib.pyplot as plt
# make the boxplot
plt.boxplot(gene_lengths,
            sym=None,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,showmeans = True,
            showbox = True,
            showfliers = True,
            notch = False,
            boxprops = {'color':'cyan','facecolor':'red'}
            )
plt.title('Boxplot of gene_lengths')
plt.show()