#!/usr/bin/python

#-------------------------------
#  Name: Factorial (Iteration).py
#  Coded by Majid Roohi
#-------------------------------

m = int(raw_input('\nEnter a number: '))
a = 1
j = 1

if m == 0 : print '\nFactorial 0 is: 0'
else :

	while a <= m :

		j *= a
		a += 1

	print '\nFactorial',m,'is: ',j
