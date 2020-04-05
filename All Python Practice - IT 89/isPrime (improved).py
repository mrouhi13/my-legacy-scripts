##def squareRootNR(x,epsilon):
##
##    '''Assume x>= 0 and epsilon > 0
##        Return y s.t. y*y is close enough to x'''
##
##    assert x>=0, 'input should be nonnegative number, not' + str(x)
##    assert epsilon > 0, 'epsilon should be positive number, not' + str(epsilon)
##
##    x = float(x)
##    guess = x/2.0
##    diff = guess**2 - x
##    ctr = 1
##
##    while abs(diff) > epsilon and ctr<=100:
##
##        guess = guess - diff/(2.0*guess)
##        diff = guess**2 - x
##        ctr += 1
##
##
##    assert ctr <= 100, 'Iteration exceeded'
##
##    return guess

import math

def isPrime(m) :

    AllAns = ()

    if m >= 2 : AllAns = (2,)

    for a in range(2,m) :

        if a%2 != 0 :

            i = int(math.sqrt(a))

            for j in range(2,i+1) :

                if a%j == 0 : break

            else: AllAns += a,

    print AllAns
