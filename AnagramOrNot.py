def anagram(str1,str2):
    sorted1= sorted(str1)
    sorted2= sorted(str2)
    if(sorted1==sorted2):
        print("string is anagram")
    else:
        print("string is not anagram")
        
anagram("list","sitll")       