#!/usr/bin/python

#----------------------------------------
#  Name: Greatest Number (if).py
#  Coded by Majid Roohi
#  Last Modified: 11/15/2010, 07:33 PM
#  Description: perl is best...
#----------------------------------------

print '\n\n   ----------------------------------------'
print '  |                                        |'
print '  |  Name: Greatest Number (if).py         |'
print '  |  Coded by Majid Roohi                  |'
print '  |  Last Modified: 11/15/2010 , 07:33 PM  |'
print '  |  Description: perl is best...          |'
print '  |                                        |'
print '   ----------------------------------------'

# One number received from the user.
num = input ( '\n\nWant some numbers together Compare?\t' )

# number must be greater than zero.
if ( num == 0 or num < 0 ) : print '\n\n\t\tNumber must be greater than zero!!!\n'
else :

	i = 1
	temp = 0

	# By a loop, received num number from the user.
	while ( i <= num ) :

		# Received number[i] from the user.
		print '\nNumber ' , i , ':'

		number = input ()

		# by if, Compare the number[i-1] & number[i].
		if ( temp < number ) :

			greatest_number = number
			temp = number

		i += 1

	# Than greatest_number is greatest number.
	print '\n\nGreatest number is:\t' , greatest_number

print '\n\n\tGood Luck. :)'

raw_input ( '\n\nPress Enter to Exit...' )