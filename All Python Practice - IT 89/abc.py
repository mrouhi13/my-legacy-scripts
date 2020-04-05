#!/usr/bin/python

#-------------------------------
#  Name: abc.py
#  Coded by Majid Roohi
#-------------------------------

def abc(a,b,c) :

	if (a <= b <= c) or (c <= b <= a) : return True
	else : return False
