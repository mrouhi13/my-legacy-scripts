#sample script
##x = 7 # Create a variable x and assign a value 7 to it
##x = x*x #Bind x to a value 49
##print x

##n = raw_input('Enter a number: ')
##print n
##x = int(n)
##print x**2


##Branch command
##n = raw_input('Enter a number: ')
##x = int(n)
##if (x/2)*2 == x:
##    print x,'is Even'
##else:
##    print x,'is Odd'
##print 'Nothing'

####Here I dont need else clause
##z = 'b'
##if 'x'
##    print 'Hello'
##    print 'There'

##if 'x'
##    print 'Hello'
##print 'There'

 

##x = 4
##y = 0.7
##z = 0.5
##print x,y,z
####Is this right?
####if x < y:
####    if x < z: print x, 'is the least'
####    else:print z, 'is the least'
####else: print y, 'is the least'
##
##if x
##elif y
##else: print z, 'is the least'

########################################
##n = raw_input('Enter a number:')
##x = int(n);
##y = 0
##itersLeft = x
##while(itersLeft>0):
##    y = y+x
##    itersLeft = itersLeft - 1
##
##print y

###########################################
n = raw_input('Enter a numnber:')
x = int(n)
i = 1
while (i
    if x%i == 0:
        print 'divisor',i
    i = i + 1
##x = 10       


##for i in range(1,x):
##    if x%i == 0:
##        print 'divisor',i
BMM

n=raw_input('enter a number:')
m=raw_input('enter a number:')
a=int(n)
b=int(m)
##cnt = int(x/2)
##while cnt>0:
##    if x%cnt==0 and y%cnt==0:
##        print 'The greatest common divisor is: ',cnt
##        break
##    cnt = cnt -1
x = a
y = b
r = x%y
while r > 0:
    r = x%y
    x = y
    y = r

print a*b/x

K

n=raw_input ('Enter the number: ')
x=int(n)
i=1
A=0

while (i
    if (x%i==0):
        A=A+1
    i=i+1

print A

KMM

a=int(raw_input('enter a number:'))
b=int(raw_input('enter a number:'))
cnt =1
while cnt <= b:
    if cnt*a%b==0:
        print cnt*a
        break
    cnt = cnt + 1

M

n=row-input

N

n=raw_input("enter a number: ")
m=raw_input("enter a number: ")
x=int(n)
y=int(m)
##cnt = 1
##while cnt<=x/2 :
##    if x%cnt==0 and y%cnt==0:
##        gcd = cnt
##    cnt = cnt+1
##print 'Greatest Common Divosor= ',gcd

cnt = x/2
while cnt>0 :
    if x%cnt==0 and y%cnt==0:
        break
    cnt = cnt-1
print 'Greatest Common Divosor= ',cnt

sqrt

##x = 16
##ans = 0
##if x>=0:
##    while ans*ans
##        ans = ans + 1
##        print 'ans =', ans
##    if ans * ans !=x:
##        print x,'is not a perfect square!'
##    else: print ans
##else: print x , 'is a negative number'

def sqrt(x):
## return the squre root of x, if x is a perfect square
## print the error message and return None otherwise        

    ans = 0
    if x>=0:
        while ans*ans
        if ans * ans !=x:
            print x,'is not a perfect square!'
            return None
        else: return ans
    else:
        print x , 'is a negative number'
        return None

## Sample code Lecture 3

## Find the square root of a perfect square

##x = 144

##ans = 0

##while (ans*ans < x): ans = ans + 1

##    

##print ans


##if (x/2)*2==x:

##    print 'even'

##else:

##    print 'odd'



##n=raw_input('Enter a number: ')

##Deffensive Programming

##x = -15

##ans = 0

##if x >= 0:

##    while ans*ans < x:

##        ans = ans + 1

##    if ans*ans != x:

##        print x ,'is not a perfect square number!'

##    else:

##        print 'ans = ',ans

##

##else:

##    print x, 'is a negative number'


##x = 10

##i = 1

##while i< x:

##    if x%i == 0:

##        print 'divisor ' , i

##    i = i+1


##x = 120

##for i in range(1,x):

##    if x%i == 0:

##        print 'divisor ',i

##

##

##x = 120

##divisors = ()

##for i in range(1, x):

##    if x%i == 0:

##        divisors = divisors + (i, )

##print divisors



s1 = 'abcdefg'

s2 = 'hijklmn'

##selecting

##print s1

##print s1[0]

##print s1[3]

##print s1[-1]


####slicing

##print s1[2:4]

##print s1[:3]

##print s1[3:]

##

##

##print s1.find('cde')

##

##print s1==s2

##print s1< s2

##print s1 > s2


##


x = 195244

sumDigits = 0

print x

for c in str(x):

    sumDigits += int(c)

print sumDigits

##x = 16

##ans = 0

##if x>=0:

##    while ans*ans

##        ans = ans + 1

####    print 'ans =', ans

##    if ans * ans !=x:

##        print x,'is not a perfect square!'

##    else: print ans

##else: print x , 'is a negative number'


##def sqrt(x):

##    ''' return the squre root of x, if x is a perfect

##    square. print the error message and return None otherwise '''

##

##    ans = 0

##    if x>=0:

##        while ans*ans

##            ans = ans + 1

##        

##        if ans * ans !=x:

##            print x,'is not a perfect square!'

##            return None

##        else: return ans

##    else:

##        print x , 'is a negative number'

##        return None

##

#### local binding vs global binding

##def f(x):

##    x = x+1

##    return x


 

##def solve(numHeads,numLegs):

##    for numChicks in range(0,numHeads + 1):

##        numSheeps = numHeads - numChicks

##        totLegs = 4*numSheeps + 2* numChicks

##        if totLegs == numLegs:

##            return[numSheeps,numChicks]

##    return [None,None]

##

##def barnYard():

##    heads = int(raw_input('Enter number of heads: '))

##    legs = int(raw_input('Enter number of legs: '))

##    sheeps, chickens = solve(heads,legs)

##    if sheeps==None:

##        print 'your problem is not solvable!'

##    else:

##        print 'Number of sheeps:',sheeps

##        print 'Number of chicks:',chickens


##

##

##

##def solve1(numHeads,numLegs):

##    for numChicks in range(0,numHeads + 1):

##        for numSheeps in range(0,numHeads-numChicks+1):

##            numSpiders = numHeads - numChicks - numSheeps

##            totLegs = 6*numSpiders + 4*numSheeps + 2* numChicks

##            if totLegs == numLegs:

##                return[numSheeps,numChicks,numSpiders]

##    return [None,None,None]


##def barnYard1():

##    '''return nothing and gets nothing'''

##    heads = int(raw_input('Enter number of heads: '))

##    legs = int(raw_input('Enter number of legs: '))    

##    sheeps, chickens, spiders = solve1(heads,legs)

##    if sheeps==None:

##        print 'There is no solution!'

##    else:

##        print 'Number of sheeps:',sheeps

##        print 'Number of chicks:',chickens

##        print 'Number of spiders:',spiders

####    solve2(legs,heads)

##


##def solve2(numLegs,numHeads):

##    solutionFound = False

##    for numChicks in range(0,numHeads + 1):

##        for numSheeps in range(0,numHeads-numChicks+1):

##            numSpiders = numHeads - numChicks - numSheeps

##            totLegs = 6*numSpiders + 4*numSheeps + 2* numChicks

##            if totLegs == numLegs:

##                print 'Number of sheeps:',numSheeps

##                print 'Number of chicks:',numChicks

##                print 'Number of spiders:',numSpiders

##                solutionFound = True            

##    if not solutionFound: print 'There is no solution'

##

##

##def integral(n):

##    sum = 0

##    for i in range(1,n+1):

##        sum +=i

##    return sum

##

##def integral2(n):

##    if n==1:

##        return(1)

##    else:

##        return integral2(n-1)+n

##

##

def isPalindrome(s):

    '''return True if s is palindrome and False otherwise'''

    if len(s)<=1: return True

    else: return s[0]==s[-1] and isPalindrome(s[1:-1])

##

##

##def fib(x):

##    if x ==0 or x ==1: return(x)

##    else: return fib(x-1) + fib(x-2)

print'1=add'
print'2=divide'
print'3=multiply '
print'4=subtract'
i=raw_input('Please enter your number of choice:')
b=int(i)
if b==1:
    c=raw_input('Please enter num1:')
    num1=float(c)
    e=raw_input('Please enter num2:')
    num2=float(e)
    s=num1+num2
    print s
if b==2:
    d=raw_input('Please enter num1:')
    num1=float(d)
    f=raw_input('Please enter num2:')
    num2=float(f)
    if num2==0:
        print'incorrect number'
        print'please enter correct number:'
        f=raw_input('Please enter num2:')
        num2=float(f)
    s=num1/num2
    print s
if b==3:
    k=raw_input('Please enter num1:')
    num1=float(k)
    g=raw_input('Please enter num1:')
    num2=float(g)
    s=num1*num2
    print s
if b==4:
    o=raw_input('Please enter num1:')
    num1=float(o)
    p=raw_input('Please enter num1:')
    num2=float(p)
    s=num1-num2
    print s

r=raw_input('How many grades do you want to enter:')

c=int(r)

k=float(r)

s=float(0)

while c > 0:

    n=raw_input('enter a number:')

    g=float(n)

    s=s+g

    #print type (k)

    c=c-1

a=s/k

print a

if 85<=a<100:

    print 'A'

if 70<=a<85:

    print 'B'

if 60<=a<70:

    print 'C'

if a<60:

    print 'D'

c=int(r)

k=c-1

while k > 0:

    if k%2!=0:

      print k

    k=k-1

i=0

k=0

s=raw_input('Please enter your string:')

c=raw_input('Please enter your char:')

while i < len(s):

 if s[i]==c:

    k=k+1

 i = i + 1

print k

def squareRootBi(x,epsilon):

    '''Assume x>= 0 and epsilon > 0

        Return y s.t. y*y is close enough to x'''

    assert x>=0, 'input should be nonnegative number, not' + str(x)

    assert epsilon > 0, 'epsilon should be positive number, not' + str(epsilon)

    low = 0 # lower bound of searching range 

    high = max(1,x) # upper bound of  searching range

    guess = (low+high)/2.0

    ctr = 1

    while abs(guess**2-x)>epsilon and ctr <=100:

        #print 'low:',low,'high:',high,'guess:',guess

        if guess**2 < x:

            low = guess

        else:

            high = guess


        guess = (low+high)/2.0

        ctr += 1


    assert ctr <= 100, 'Iteration exceeded'

    print 'Bi method. Num. Iteration:',ctr,'Estimate:',guess

    return guess


def testBi():

    print 'squareRootBi(4,0.0001)'

    squareRootBi(4,0.0001)

    print 'squareRootBi(9,0.0001)'

    squareRootBi(9,0.0001)

    print 'squareRootBi(2,0.0001)'

    squareRootBi(2,0.0001)

    print 'squareRootBi(0.25,0.0001)'

    squareRootBi(0.25,0.0001)

    

def squareRootNR(x,epsilon):

    '''Assume x>= 0 and epsilon > 0

        Return y s.t. y*y is close enough to x'''

    assert x>=0, 'input should be nonnegative number, not' + str(x)

    assert epsilon > 0, 'epsilon should be positive number, not' + str(epsilon)

    x = float(x)

    guess = x/2.0

##    guess = 0.01

    diff = guess**2 - x

    ctr = 1

    while abs(diff) > epsilon and ctr<=100:

        guess = guess - diff/(2.0*guess)

        diff = guess**2 - x

        ctr += 1


    assert ctr <= 100, 'Iteration exceeded'

    print 'NR method. Num. Iteration:',ctr,'Estimate:',guess

    return guess

##Example of Structured code

##

##import math

### Get Base

##inputOK = False;

##while not inputOK:

##    base = input('enter Base: ')

##    if type(base)==type(1.0): inputOK=True

##    else: print('Error: You must enter a float value');

##

### Get height

##inputOK = False;

##while not inputOK:

##    height = input('enter Height: ')

##    if type(height)==type(1.0): inputOK=True

##    else: print('Error: You must enter a float value');

##

##

##hyp = math.sqrt(base*base+height*height)

##

##print 'Base '+str(base)+'Height:'+str(height)+'hyp:'+str(hyp)

##

##

import math

def getFloat(reqMsg,ErrMsg):

    inputOK = False;

    while not inputOK:

        val = input(reqMsg)

        if type(val)==type(1.0): inputOK=True

        else: print(errMsg);

    return val

base = getFloat('Enter Base:','Err: Base must be float value.')

height = getFloat('Enter Height:','Err:Height Must be float value.')

hyp = math.sqrt(base*base+height*height)


print 'Base '+str(base)+'Height:'+str(height)+'hyp:'+str(hyp)

def exp1(a,b):

    ans = 1

    while (b>0):

        ans *= a

        b -=1

    return ans


def exp2(a,b):

    if b==1:

        return a

    else: return a*exp2(a,b-1)


def exp3(a,b):

    if b==1:

        return a

    if b%2 ==0:

        return exp3(a*a,b/2)

    else: return a*exp3(a,b-1)


def g (n,m):

    x = 0

    for i in range(n):

        for j in range(m):

            x+=1

    return x

def Towers(size,fromStack,toStack,sparseStack):

    if size == 1:

        print 'Move disk from',fromStack,'to',toStack

    else:

        Towers(size-1,fromStack,sparseStack,toStack)

        Towers(1,fromStack,toStack,sparseStack)

        Towers(size-1,sparseStack,toStack,fromStack)


def search(s,e):

    answer = None

    i = 0

    numCompares =0

    while i

        numCompares +=1

        if e==s[i]:

            answer = True

        elif e < s[i]:

            answer = False

        i +=1

    print answer, numCompares

                


def bsearch(s,e,first,last,calls):

    print first, last, calls

    if (last -first)< 2 : return s[first]==e or s[last]==e

    mid = first + (last-first)/2

    if s[mid] == e: return True

    if s[mid] > e:

        return bsearch(s,e,first,mid-1,calls+1)

    else:

        bsearch(s,e,mid+1,last,calls+1)

        

    

def search1(s,e):

    print bsearch(s,e,0,len(s)-1,1)

    print 'Search Completed!'



def testSearch():

    s = range(0,1000000)

    raw_input('basic 1000000')

    print search(s,1000000)

    raw_input('binary 1000000')

    print search1(s,1000000)

    

def selSort(s):

    for i in range(len(s)):

        minIdx = i

        for j in range(i+1,len(s)):

            if s[j]

                minIdx = j

        tmp = s[i]

        s[i]= s[minIdx]

        s[minIdx] = tmp

    return s


def BubbleSort(L):

    for j in range(len(L)):

        for i in range(len(L)-1):

            if L[i]>L[i+1]:

                temp = L[i]

                L[i]=L[i+1]

                L[i+1] = temp

        print L


def BubbleSort2(L):

    

    while swaped:

        swaped = False

        for i in range(len(L)-1):

            if L[i]>L[i+1]:

                temp = L[i]

                L[i]=L[i+1]

                L[i+1] = temp

                swaped = True

        print L


def merge(left,right):

    result = []

    i,j = 0,0

    while i

        if left[i]

            result.append(left[i])

            i = i+1

        else:

            result.append(right[j])

            j = j + 1

    while i

        result.append(left[i])

        i = i+1

    while j

        result.append(right[j])

        j = j+1

    return result


def mergeSort(L):

##    print L

    if len(L)<2:

        return L[:]

    else:

        middle = len(L)/2

        left = mergeSort(L[:middle])

        right = mergeSort(L[middle:])

        together = merge(left,right)

##        print 'together',together

        return together


def Max_sub1(L):

    max_Sum = 0

    for i in range(len(L)):

        for j in range(i,len(L)):

            this_Sum = 0

            for k in range(i,j+1):

                this_Sum = this_Sum + L[k]

            if this_Sum > max_Sum: max_Sum = this_Sum

    return max_Sum


def Max_sub2(L):

    max_Sum = 0

    for i in range(len(L)):

        this_Sum = 0

        for j in range(i,len(L)):

            this_Sum = this_Sum + L[j]

            if this_Sum > max_Sum: max_Sum = this_Sum

    return max_Sum

    

def Max_sub3(L,first,last):

    max_sub,max_perf,max_suf = 0,0,0

    if first==last:

        if L[first]>0:

            return L[first],L[first],L[first]

        else:

            return 0,0,0

    mid = int((first+last)/2)

    max_sub1,max_perf1,max_suf1= Max_sub3(L,first,mid);

    max_sub2,max_perf2,max_suf2= Max_sub3(L,mid+1,last);

    max_sub = max(max_sub1,max_sub2,max_suf1+max_perf2)


    max_perf = 0

    this_perf = 0

    for i in range(first,last+1):

        this_perf = this_perf+L[i]

        if this_perf > max_perf: max_perf = this_perf


    max_suf = 0

    this_suf = 0

    for i in range(first,last+1):

        this_suf = this_suf+L[first+last-i]

        if this_suf > max_suf: max_suf = this_suf

    return max_sub,max_perf,max_suf


def Max_sub4(L):

    max_sub,max_suf = 0,0

    if len(L)==1:

        if L[0]>0: return L[0],L[0]

        else: return 0,0

    max_sub1,max_suf1 = Max_sub4(L[0:-1])

    max_suf = 0

    if max_suf1+L[-1]>max_suf:

        max_suf = max_suf1+L[-1]

    max_sub = max(max_sub1,max_suf)

    return max_sub,max_suf

    

    

def Max_sub5(L):

    max_sub, max_suf = 0,0

    for i in range(len(L)):

        max_suf = max(0,max_suf+L[i]);

        max_sub = max(max_suf,max_sub);

    return max_sub
