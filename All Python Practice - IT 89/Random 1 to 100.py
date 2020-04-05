#!/usr/bin/python

#-------------------------------
#  Name: Random 1 to 100.py
#  Coded by Majid Roohi
#-------------------------------

def Random() :

        import random

        m = int(random.choice(range(0,101)))

        for i in range(0,10) :

                a = int(raw_input('Enter a number (0-100): '))

                if a == m :

                        print '\nYour guess is correct.\n'
                        break

                if a < m : print '\nYour guess is lowest than current number.\n'
                if a > m : print '\nYour guess is greatest than current number.\n'
