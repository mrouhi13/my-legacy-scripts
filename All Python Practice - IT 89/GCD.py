#!/usr/bin/python

#-------------------------------
#  Name: GCD.py
#  Coded by Majid Roohi
#-------------------------------

def GCD(m,a):
    if a==0 : return m
    else : return gcd(a,m%a)
