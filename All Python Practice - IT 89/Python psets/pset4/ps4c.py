#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3a.py
#  Coded by Majid Roohi
#  Last Modified: 26/12/2010 , 05:12 PM
#  Description: -
#------------------------------------------------------

def postRetirement(savings,expenses,growthRates = []) :

    print

    F = []
    F.append(savings*(1+0.01*growthRates[0])-expenses)

    for i in range(1,len(growthRates)) :

        F.append(F[i-1]*(1+0.01*growthRates[i])-expenses)

    for j in range(0,len(F)) :
        
        print 'Your fund sizes after year',j+1,':',F[j]

    print

