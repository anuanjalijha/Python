string1 = "I live in Janadh"
no_of_lower_case = 0
no_of_upper_case = 0
for char in string1:
    if char.islower():
        no_of_lower_case+= 1
    elif char.isupper():
        no_of_upper_case+=1
print("number of uppercase is ",no_of_upper_case)
print("number of lowercase is ",no_of_lower_case)




