#!/usr/bin/python

#----------------------------------------
#  Name: Greatest Number (lst).py
#  Coded by Majid Roohi
#  Last Modified: 11/15/2010, 07:32 PM
#  Description: perl is best...
#----------------------------------------

print '\n\n   ----------------------------------------'
print '  |                                        |'
print '  |  Name: Greatest Number (lst).py        |'
print '  |  Coded by Majid Roohi                  |'
print '  |  Last Modified: 11/15/2010 , 07:32 PM  |'
print '  |  Description: perl is best...          |'
print '  |                                        |'
print '   ----------------------------------------'

# One number received from the user.
num = input ( '\n\nWant some numbers together Compare?\t' )

# number must be greater than zero.
if ( num == 0 or num < 0 ): print '\n\n\t\tNumber must be greater than zero!!!\n'
else :

	i = 1
	greatest_number = []

	# By a loop, received num number from the user.
	while ( i <= num ):

		print '\nNumber ' , i , ':'

		number = input ()
		greatest_number.append(number)
		i += 1

	greatest_number.sort()

	# Than greatest_number[i-2] is greatest number.
	print '\n\n\t\tGreatest number is:\t' , greatest_number[i-2] , '\n'

print '\n\n\tGood Luck. :)'

raw_input ( '\n\nPress Enter to Exit...' )