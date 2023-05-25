arr = [109, 5, 8, 20]
largest = arr[0]
second_largest = arr[1]
for num in arr:
    if num>largest:
        second_largest = largest
        largest = num
    elif num>second_largest and num!= largest:
        second_largest = num
print("Largest number is ",largest)
print("Second Largest number is ",second_largest)