#!/usr/bin/python

#-------------------------------
#  Name: Passport.py
#  Coded by Majid Roohi
#-------------------------------

def Passport():
    
    passid = raw_input('Enter your passport id: ')
    
    a = passid[len(passid)-4:]
    a = int (a)
    
    if 1900 <= a <= 2011 :
        if passid[len(passid)-9:len(passid)-4] == '<<<<<' :
            if passid[0:len(passid)-9] != '' :
                print '\nYour id is valid.'
            else : print '\nYour id is invalid.'
        else : print '\nYour id is invalid.'
    else : print '\nYour id is invalid.'
