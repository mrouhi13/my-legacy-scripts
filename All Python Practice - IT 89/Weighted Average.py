#!/usr/bin/python

#-------------------------------
#  Name: Weighted Average.py
#  Coded by Majid Roohi
#-------------------------------

def WeightedAverage() :

    n = input('\nWant some value to calculate weighted average? ')
    m = float()
    a = float()

    for i in range(0,n) :

        x = input('\nEnter values of the quantity: ')
        w = input('Enter values of the corresponding weights: ')
        m += x*w
        a += w

    j = m/a

    print '\nWeighted Average: ',j,'\n'
