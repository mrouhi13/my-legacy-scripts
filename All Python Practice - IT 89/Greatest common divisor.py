#!/usr/bin/python

#----------------------------------------
#  Name: Greatest common divisor.py
#  Coded by Majid Roohi
#  Last Modified: 11/15/2010 , 04:45 PM
#  Description: perl is best...
#----------------------------------------

print '\n\n   ----------------------------------------'
print '  |                                        |'
print '  |  Name: Greatest common divisor.py      |'
print '  |  Coded by Majid Roohi                  |'
print '  |  Last Modified: 11/15/2010 , 04:45 PM  |'
print '  |  Description: perl is best...          |'
print '  |                                        |'
print '   ----------------------------------------'

# Two numbers received from the user.
print '\n\nPlease enter two numbers.'

num1 = input ( '\n\nNumber 1: ' )
num2 = input ( 'Number 2: ' )

# If the input(s), not numbers, i don't know really what to do.
# If number(s) was 0, then:
if ( num1 == 0 ) or ( num2 == 0 ) : print '\n\nGreatest common divisor :\t0'
else :

	# If numbers was negative, then:
	if ( num1 < 0 ) : num1 = -num1
	if ( num2 < 0 ) : num2 = -num2

	# By a loop, the greatest common divisor we find.
	while ( 0 < num2 ) :

		temp = num1
		num1 = num2
		num2 = temp % num2

	# Then num1 is greatest common divisor.
	print '\n\nGreatest common divisor :\t' , num1

print '\n\n\tGood Luck. :)'

raw_input ( '\n\nPress Enter to Exit...' )