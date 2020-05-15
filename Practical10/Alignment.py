# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:36:48 2020

@author: hp
"""

# import the file
import pandas as pd
human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
matrix=pd.read_csv("BLOSUM62 matrix.csv")
protein='ARNDCQEGHILKMFPSTWYVBZX'
# distances between the three genes
edit_distance1=0
edit_distance2=0
edit_distance3=0
for i in range(len(human)):
    if mouse[i]!=human[i]:
        edit_distance1+=1
    if random[i]!=human[i]:
        edit_distance2+=1
for i in range(len(mouse)):
    if random[i]!=mouse[i]:
        edit_distance3+=1
print('the distance between mouse and human'+":"+str(edit_distance1))
print('the distance between random and human'+":"+str(edit_distance2))
print('the distance between mouse and random'+":"+str(edit_distance3))
# the final score
score1=0
score2=0
score3=0
sum1=0
sum2=0
sum3=0
for i in range(len(human)):
    row=protein.index(human[i])+1
    column=protein.index(mouse[i])+1
    sum1+=matrix.iloc[row,column]
    if human[i]==mouse[i]:
        score1+=1
print(mouse+''+' '+str(sum1))
percentage=score1/len(human)*100
print('percentage between mouse and human'+":"+str(percentage)+'%')
for i in range(len(human)):
    row=protein.index(human[i])+1
    column=protein.index(random[i])+1
    sum2+=matrix.iloc[row,column]
    if human[i]==random[i]:
        score2+=1
print(random+''+' '+str(sum2))
percentage=score2/len(human)*100
print('percentage between random and human'+":"+str(percentage)+'%')
for i in range(len(random)):
    row=protein.index(random[i])+1
    column=protein.index(mouse[i])+1
    sum3+=matrix.iloc[row,column]
    if random[i]==mouse[i]:
        score3+=1
print(mouse+''+' '+str(sum3))
percentage=score3/len(random)*100
print('percentage between mouse and random'+":"+str(percentage)+'%')









