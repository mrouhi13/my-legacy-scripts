#!/usr/bin/python

#-------------------------------
#  Name: Perimeter.py
#  Coded by Majid Roohi
#-------------------------------

def circumference() :

    print '\n\t\tCircumference'

    r = float(raw_input('\nRadiuse: '))

    circumference = 2*r*3.14

    print '\nCircumference: ',circumference,'\n'
    print '-------------------------------'


def SquarePerimeter() :

    print '\n\t\tSquare perimeter'

    a = float(raw_input('\nSquare side: '))

    square = a*4

    print '\nSquare perimeter: ',square,'\n'
    print '-------------------------------'


def RectangularPerimeter() :

    print '\n\t\tRectangular Perimeter'

    a = float(raw_input('\nRectangle height: '))
    b = float(raw_input('Rectangle width: '))

    rectangular = 2*(a+b)

    print '\nRectangular Perimeter: ',rectangular,'\n'
    print '-------------------------------'
