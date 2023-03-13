def primeFactor(num):
    i=2
    factor=[]
    while i<=num:
        if num%i==0:
            factor.append(i)
            num= num//i
        else:
            i=i+1
    return factor
print(primeFactor(320))