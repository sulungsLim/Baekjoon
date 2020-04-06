# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 03:02:55 2020

@author: USER
"""

a,b=map(int,input().split())
ls=[]

for i in range(b):
    ls.append(input().split())
    print(ls)
    hi=[ls[0]]
c=0
for sum in range(b):
    for k in range(2):    
        if ls[sum][k] in hi[c]:
            hi[c] += ls[sum]
            hi[c] = list(set(hi[c]))
            print(hi)
            pass
            ## 망했다
        elif ls[sum][k] not in hi[c]:
            hi.append(ls[sum])
            c += 1
            hi[c] = list(set(hi[c]))
            print(hi)
            break
        

print(len(hi))
