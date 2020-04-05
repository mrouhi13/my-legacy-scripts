#!/usr/bin/python

#------------------------------------------------------
#  Name: List of solution for McNuggets.py
#  Coded by Majid Roohi
#  Last Modified: 03/12/2010 , 02:30 PM
#  Description: All of solutions of McNuggets problem
#------------------------------------------------------

def Diophantine() :

        ''' This program take number of McNuggets from user and find all of solution for this number of McNuggets and return it, if not finde
	any solution return None.'''
        
        N = input('\nHow many McNuggets you need to buy? ')

        print '\nList of solution for this number of McNuggets:\n'

        for a in range(0,(N/6)+1) :

                for b in range(0,((N-6*a)/9)+1) :

                        for c in range(0,((N-6*a-9*b)/20)+1) :

                                if N == 6*a+9*b+20*c :

                                        print a,'  Pack 6 Pieces.'
                                        print b,'  Pack 9 Pieces.'
                                        print c,'  Pack 20 Pieces.'
                                        print '-------------------------\n'
