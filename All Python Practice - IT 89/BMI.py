#!/usr/bin/python

#-------------------------------
#  Name: BMI.py
#  Coded by Majid Roohi
#-------------------------------

def BMI() :

	Weight = float(input('\nEnter your weight(kg): '))
	Height = float(input('Enter your height(cm): '))
	Height /= 100
	bmi = float()
	bmi = Weight/Height**2

	print 

	if bmi <= 18.5 : print '\n',bmi,',Underweight\n'
	if 18.5 <= bmi <= 24.9 : print '\n',bmi,',Normal weight\n'
	if 25 <= bmi <= 29.9 : print '\n',bmi,',Overweight\n'
	if 30 <= bmi : print '\n',bmi,',Obesity\n'
