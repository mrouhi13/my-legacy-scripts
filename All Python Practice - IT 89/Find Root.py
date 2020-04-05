#!/usr/bin/python

#-------------------------------
#  Name: FindRoot.py
#  Coded by Majid Roohi
#-------------------------------

def FindRoot(a,b,eps):

        i = 0
        xn = a+b/2
        fa = f(a)
        fx = f(xn)

        while i <= 100 and abs(fx) >= eps :

                xn = a+b/2
                fa = f(a)
                fx = f(xn)

                if  fa*fx > 0 : a = xn
                elif fa*fx < 0 : b = xn
                else : print 'root =',xn

                i += 1

def f(x) : return x**3+x-1
