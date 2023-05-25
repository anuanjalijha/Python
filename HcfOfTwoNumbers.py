num1 = 18
num2 = 15
if num1>num2:
    greater = num1
else:
    greater = num2
for i in range(1,greater):
    if(num1%i==0 and num2%i==0):
        Hcf = i
print("Highest common factor is ",Hcf)