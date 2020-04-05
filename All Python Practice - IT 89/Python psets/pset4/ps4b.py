#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3a.py
#  Coded by Majid Roohi
#  Last Modified: 26/12/2010 , 04:41 PM
#  Description: -
#------------------------------------------------------

def nestEggVariable(salary,save,growthRates = []) :

    print

    F = []
    F.append(salary*save*0.01)

    for i in range(1,len(growthRates)) :

        F.append(F[i-1]*(1+0.01*growthRates[i])+salary*save*0.01)

    for j in range(0,len(F)) :
        
        print 'Your retirement account at the end of year',j+1,':',F[j]

    print
