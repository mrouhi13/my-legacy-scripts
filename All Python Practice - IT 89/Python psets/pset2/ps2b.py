#!/usr/bin/python

#----------------------------------------
#  Name: ps2b.py
#  Coded by Majid Roohi
#  Last Modified: 03/12/2010 , 03:45 PM
#  Description: -
#----------------------------------------

def Diophantine() :

        '''Program take packages size from the user and test 0 to 200 for N (number of McNuggets) with iterative. if A=False namely N McNuggets
        can be bought in exact quantity,else N=N-1 and once again repeat this steps until A=True. if A=True then current N is our answer, namely
        N McNuggets connot be bought in exact quantity.'''

        x = input('\nEnter size of first package: ')
        y = input('Enter size of second package: ')
        z = input('Enter size of third package: ')

        packagesize = []
        packagesize = [x,y,z]
        
        packagesize.sort()

        x = packagesize[0]
        y = packagesize[1]
        z = packagesize[2]
        
        if x == 0 or y == 0 or z == 0 : print '\nPackage size must be greater than zero.\n'
        else :

                N = 200

                while N >= 0 :

                        A = True

                        for a in range(0,(N/x)+1) :

                                for b in range(0,((N-x*a)/y)+1) :

                                        for c in range(0,((N-x*a-y*b)/z)+1) :

                                                if N==x*a+y*b+z*c :

                                                        A = False

                        if A == True:

                                print '\nLargest number of McNuggets that cannot be bought in exact quantity: ',N

                                break

                        elif N == 0 and A == False : print '\nLargest number of McNuggets that cannot be bought in exact quantity: ',N

                        N -= 1
