#!/usr/bin/python

#--------------------------------------------
#  Name: McNuggets.py
#  Coded by Majid Roohi
#  Last Modified: 03/12/2010 , 03:04 PM
#  Description: McNuggets problem solution
#--------------------------------------------

def Solve() :

        '''Program take number of McNuggets from the user and give it to Diophantine function, If can be bought McNuggets with recommend packages
	then print number of each packages else print no suggestion for this number of McNuggets. Of course maybe exist to many solve for bought
	McNuggets, But program offer for user one solve.'''

        n = int(input('\nHow many McNuggets you need to buy? '))

        McNuggets,x,y,z = Diophantine(n)

        if McNuggets != None :

                print '\nWe offer you the following packages we recommend:\n'
                print x,' Package  6 Pieces.'
                print y,' Package  9 Pieces.'
                print z,' Package  20 Pieces.\n'

        elif McNuggets == None :

                print '\nWe have no suggestion for you!'

        raw_input('\nPress Enter to Exit...')

def Diophantine(N) :

        '''take number of McNuggets from solve function and test diffrent solve for solution this equation, finally return one solve.'''

        for a in range(0,(N/6)+1) :

                for b in range(0,((N-6*a)/9)+1) :

                        for c in range(0,((N-6*a-9*b)/20)+1) :

                                if N == 6*a+9*b+20*c :

                                        return N,a,b,c

        else :

                return None,None,None,None
