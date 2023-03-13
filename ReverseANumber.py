def reverse(num):
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        reverse_num=(reverse_num*10)+last_digit
        num=num//10
    print(reverse_num)
reverse(123) 