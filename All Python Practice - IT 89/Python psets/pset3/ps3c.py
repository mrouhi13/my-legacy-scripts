#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3c.py
#  Coded by Majid Roohi
#  Last Modified: 24/12/2010 , 03:30 PM
#  Description: -
#------------------------------------------------------

def constrainedMatchPair(lenoffs,rspftfs = (),rspftss = ()) :

    allans = ()

    for i in range(0,len(rspftfs)) :

        if rspftfs[i]+lenoffs+1 == rspftss[i] :

            allans += rspftfs[i],

    return allans
