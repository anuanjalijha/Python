def palindrome(string):
    reversed_string=""
    for char in string:
        reversed_string=char+reversed_string
    if(reversed_string==string):
        print("palindrome")
    else:
        print("Not palindrome") 
palindrome("naman")        