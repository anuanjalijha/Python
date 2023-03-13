def findFactorial(num):
    if(num<=1):
        factorial=1
    if(num>1):
        factorial= num*findFactorial(num-1)
    return factorial
print(findFactorial(8))