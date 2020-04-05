#!/usr/bin/python

#----------------------------------------
#  Name: ps2a.py
#  Coded by Majid Roohi
#  Last Modified: 03/12/2010 , 03:28 PM
#  Description: -
#----------------------------------------

def Diophantine() :

        '''Program take number of McNuggets from the user and test 0 to N (number of McNuggets) with iterative. if A=False namely N McNuggets can
	be bought in exact quantity, else N=N-1 and once again repeat this steps until A=True. if A=True then current N is our answer, namely N
	McNuggets connot be bought in exact quantity.'''

        N = input('\nHow many McNuggets you need to buy? ')
        
        while N >= 0 :

                A = True

                for a in range(0,(N/6)+1) :

                        for b in range(0,((N-6*a)/9)+1) :

                                for c in range(0,((N-6*a-9*b)/20)+1) :

                                        if N == 6*a+9*b+20*c :

                                                A = False
                if A == True :

                        print '\nLargest number of McNuggets that cannot be bought in exact quantity: ',N

                        break

                N -= 1
