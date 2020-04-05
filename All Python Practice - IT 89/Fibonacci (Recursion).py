#!/usr/bin/python

#-------------------------------
#  Name: Fibonacci (Recursion).py
#  Coded by Majid Roohi
#-------------------------------

def Fibonacci(m) :

    if m == 0 or m == 1 : return m
    else : return Fibonacci(m-1) + Fibonacci(m-2)
