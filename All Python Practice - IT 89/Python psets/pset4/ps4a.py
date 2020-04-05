#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3a.py
#  Coded by Majid Roohi
#  Last Modified: 26/12/2010 , 04:00 PM
#  Description: -
#------------------------------------------------------

def nestEggFixed(salary,save,growthRate,years) :

    print
    
    F = []
    F.append(salary*save*0.01)

    for i in range(0,years) :

        F.append(F[i]*(1+0.01*growthRate)+salary*save*0.01)

    for j in range(0,years) :
        
        print 'Your retirement account at the end of year',j+1,':',F[j]

    print
