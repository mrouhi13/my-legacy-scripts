def isPrime(m) :

    AllAns = ()

    for a in range(2,m) :
        
        for j in range(2,a) :

            if a%j == 0 : break
        else: AllAns += a,

    print AllAns
