def isPrime(num):
    a=1
    if num < 2:
        print("Number is not prime")
    for i in range(2,num):
        if num%i==0:
            a=0
    if(a==1):
        print("prime")
    else:
        print("not prime")
isPrime(30)            