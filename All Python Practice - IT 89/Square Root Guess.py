def SquareRootGuess(m,epsilon):

    '''Assume m >= 0 and epsilon > 0 and start with a guess'''

    assert m >= 0, 'input should be nonnegative number, not ' + str(m)

    assert epsilon > 0, 'epsilon should be positive number, not ' + str(epsilon)

    m = float(m)

    g = m/2

    diff = g**2 - m

    ctr = 1

    while abs(diff) > epsilon and ctr <= 100 :

        g = (g + m/g) / 2

        diff = g**2 - m

        ctr += 1


    assert ctr <= 100, 'Iteration exceeded'

    print 'Guess method. Num. Iteration: ',ctr,'Estimate: ',g

    return g

def testSquareRootGuess():

    print 'SquareRootGuess(8,0.001)'

    SquareRootGuess(8,0.001)

    print 'SquareRootGuess(25,0.001)'

    SquareRootGuess(25,0.001)

    print 'SquareRootGuess(16,0.001)'

    SquareRootGuess(16,0.001)

    print 'SquareRootGuess(0.25,0.001)'

    SquareRootGuess(0.25,0.001)
