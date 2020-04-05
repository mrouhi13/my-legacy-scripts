#!/usr/bin/python

#------------------------------------------------------
#  Name: ps3b.py
#  Coded by Majid Roohi
#  Last Modified: 24/12/2010 , 02:30 PM
#  Description: -
#------------------------------------------------------

def subStringMatchExact(target,key) :

        allans = ()

        for i in range(0,len(target)) :

                if target[i:i+len(key)] == key :

                        allans += i,

        print 'In this points find "',key,'":',allans,'\n'
