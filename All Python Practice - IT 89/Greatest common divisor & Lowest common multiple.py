#!/usr/bin/python

#-------------------------------------------------------------
#  Name: Greatest common divisor & Lowest common multiple.py
#  Coded by Majid Roohi
#  Last Modified: 11/15/2010 , 04:41 PM
#  Description: perl is best...
#-------------------------------------------------------------

print '\n\n   -------------------------------------------------------------'
print '  |                                                             |'
print '  |  Name: Greatest common divisor & Lowest common multiple.py  |'
print '  |  Coded by Majid Roohi                                       |'
print '  |  Last Modified: 11/15/2010 , 04:41 PM                       |'
print '  |  Description: perl is best...                               |'
print '  |                                                             |'
print '   -------------------------------------------------------------'

# Two numbers received from the user.
print '\n\nPlease enter two numbers.'

num1 = input ( '\n\nNumber 1: ' )
num2 = input ( 'Number 2: ' )

# If the input(s), not numbers, i don't know really what to do.
# If number(s) was 0, then:
if ( num1 == 0 ) or ( num2 == 0 ) : print '\n\nGreatest common divisor :\t0\nLowest common multiple :\t0'
else :

	# The smaller and larger numbers, are identified.
	i = num2

	if ( num1 < num2 ) : i = num1

	# If i was negative, then:
	if ( i < 0 ) : i = -i

	# By a loop, the greatest common divisor we find.
	while ( i > 0 ) :

		if (( num1 % i == 0 ) and ( num2 % i == 0 )) :

			# Then i is greatest common divisor.
			print '\n\nGreatest common divisor :\t' , i

			# Lowest common multiple, is equal to multiplying two numbers divided by the greatest common divisor of two numbers.
			i = ( num1 * num2 ) / i

			# Then i is lowest common multiple.
			print 'Lowest common multiple :\t' , i

			break

		i -=  1

print '\n\n\tGood Luck. :)'

raw_input ( '\n\nPress Enter to Exit...' )