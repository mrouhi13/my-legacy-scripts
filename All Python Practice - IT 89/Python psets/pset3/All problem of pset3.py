#!/usr/bin/python

#------------------------------------------------------
#  Name: All problem of pset3.py
#  Coded by Majid Roohi
#  Last Modified: 24/12/2010 , 06:45 PM
#  Description: -
#------------------------------------------------------

def subStringMatchOneSub(key,target):

    allAnswers = ()
    for miss in range(0,len(key)):

        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2

        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)

        filtered = constrainedMatchPair(len(key1),match1,match2)
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

def subStringMatchExact(target,key) :

    Temp = str()
    count  = 0
    allans = ()

    for i in range(0,len(target)) :

        Temp = target[i:i+len(key)]

        if Temp == key :

            count += 1
            allans += i,
    return allans

def constrainedMatchPair(lenoffs,rspftfs = (),rspftss = ()) :

    allans = ()

    for i in range(0,len(rspftfs)) :
        for j in range(0,len(rspftss)) :
            if rspftfs[i]+lenoffs+1 == rspftss[j] :
                allans += rspftfs[i],

    return allans
