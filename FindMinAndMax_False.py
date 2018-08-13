# -*- coding:UTF-8 -*-
def findMinAndMax(L):

    s=()
    if len(L)==0:
        s[0]=None
        s[1]=None
        return s
    elif len(L)==1:
        for i in L:
            s[0]=i
            s[1]=i
        return s
    else:
        for i in range(len(L)-1):
            if(L[i]>=L[i+1]):
                s[0]=L[i]
            else:
                s[0]=L[i+1]
        
        for i in range(len(L)-1):
            if(L[i]<=L[i+1]):
                s[1]=L[i]
            else:
                s[1]=L[i+1]
        return s
