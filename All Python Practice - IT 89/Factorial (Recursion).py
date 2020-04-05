#!/usr/bin/python

#-------------------------------
#  Name: Factorial (Recursion).py
#  Coded by Majid Roohi
#-------------------------------

def Factorial(m) :

        if m == 0 or m == 1 : return 1
        else : return Factorial(m-1) * m