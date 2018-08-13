# -*-  coding:utf-8 -*-
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    elif len(L)==1:
        return (L[0],L[0])
    else:
        max=L[0]
        min=L[0]
        for x in L:
            if max<x:
                max=x
            if min>x:
                min=x
        return (min,max)
