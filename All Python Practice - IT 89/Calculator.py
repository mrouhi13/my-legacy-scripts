def Calculator() :

    print 'Please select one of following options:\n'
    print '1 = Sum'
    print '2 = Subtraction'
    print '3 = Multiply'
    print '4 = Divide\n'

    m = raw_input('Option: ')

    x = float(raw_input('\nFirst Number: '))
    y = float(raw_input('Second Number: '))
    
    if m == '1' : a = Sum(x,y)
    elif m == '2' : a = Subtraction(x,y)
    elif m == '3' : a = Multiplym(x,y)
    elif m == '4' : a = Divide(x,y)

    print '\n',a,'\n'

def Sum(m,n) :

    return m + n

def Subtraction(m,n) :

    return m - n

def Multiplym(m,n) :

    return m * n

def Divide(m,n) :

    if n == 0 : print 'Incorrect number.'
    else : return m / n
