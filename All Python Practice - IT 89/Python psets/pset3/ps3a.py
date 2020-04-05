#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3a.py
#  Coded by Majid Roohi
#  Last Modified: 24/12/2010 , 02:00 PM
#  Description: -
#------------------------------------------------------

def countSubStringMatch(target,key) :

        count  = 0
        
        for i in range(0,len(target)) :

                if target[i:i+len(key)] == key :

                        count += 1

        print '\n',count,key,'exist in current text.\n'

def countSubStringMatchRecursive(target,key) :

        if len(target) == 0 : return False
        elif target[len(target)-len(key):] == key : return True
        else : return countSubStringMatchRecursive(target[0:len(target)-1],key)
