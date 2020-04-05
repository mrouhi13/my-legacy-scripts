#!/usr/bin/python

#-------------------------------
#  Name: thethx.py
#  Coded by Majid Roohi
#-------------------------------

def thethx() :

        print 'Pleas enter parameters of first equation: '

        a1 = float(raw_input('a1: '))
        b1 = float(raw_input('b1: '))
        c1 = float(raw_input('c1: '))
        m1 = float(raw_input('m1: '))

        print 'Pleas enter parameters of second equation: '

        a2 = float(raw_input('a2: '))
        b2 = float(raw_input('b2: '))
        c2 = float(raw_input('c2: '))
        m2 = float(raw_input('m2: '))

        print 'Pleas enter parameters of third equation: '

        a3 = float(raw_input('a3: '))
        b3 = float(raw_input('b3: '))
        c3 = float(raw_input('c3: '))
        m3 = float(raw_input('m3: '))

        Determinant = a1*b2*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1 - a2*b1*c3 - a1*b3*c2
        X = (m1*b2*c3 + m2*b3*c1 + m3*b1*c2 - m3*b2*c1 - m2*b1*c3 - m1*b3*c2) / Determinant
        Y = (a1*m2*c3 + a2*m3*c1 + a3*m1*c2 - a3*b2*c1 - a2*m1*c3 - a1*c3*c2) / Determinant
        Z = (a1*b2*m3 + a2*b3*m1 + a3*b1*m2 - a3*b2*m1 - a2*b1*m3 - a1*b3*m2) / Determinant

        print X
        print Y
        print Z
