#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3d.py
#  Coded by Majid Roohi
#  Last Modified: 24/12/2010 , 06:30 PM
#  Description: -
#------------------------------------------------------

def subStringMatchExactlyOneSub(target,key) :

    print
    
    for miss in range(0,len(key)):

        key1 = key[:miss]
        key2 = key[miss+1:]
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        
        print 'In this points find "',key1,key2,'":',constrainedMatchPair(len(key1),match1,match2),'\n'

def subStringMatchExact(target,key) :

    allans = ()

    for i in range(0,len(target)) :

        if target[i:i+len(key)] == key :

            allans += i,

    return allans

def constrainedMatchPair(lenoffs,rspftfs = (),rspftss = ()) :

    allans = ()

    for i in range(0,len(rspftfs)) :
        for j in range(0,len(rspftss)) :
            if rspftfs[i]+lenoffs+1 == rspftss[j] :
                allans += rspftfs[i],

    return allans
