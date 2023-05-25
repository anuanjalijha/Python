num1 = 15
num2 = 3
for i in range(num1,num1*num2+1):
    if(i%num1==0 and i%num2==0):
        lcm = i
        break
print("Least common factor is ",lcm)