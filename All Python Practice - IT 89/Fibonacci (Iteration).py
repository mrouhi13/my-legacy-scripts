#!/usr/bin/python

#-------------------------------
#  Name: Fibonacci (Iteration).py
#  Coded by Majid Roohi
#-------------------------------

def Fibonacci(m) :

    i = 1
    Temp1 = 1
    Temp2 = 0

    while i <= m :

        Fib = Temp1 + Temp2
        Temp1 = Temp2
        Temp2 = Fib
        i += 1

    print Fib
