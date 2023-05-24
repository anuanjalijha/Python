def isArmstrong(num):
    sum = 0
    temp = num
    length = len(str(temp))
    while temp>0:
        last_digit = temp % 10
        sum += (last_digit ** length)
        temp //= 10
    if (num==sum):
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")
isArmstrong(153)        
   


        