string1 = "This is anjali jha from muzaffarpur"
list1 = string1.split()
for i in range(len(list1)-1):
    if(len(list1[i])>len(list1[i+1])):
        great = list1[i]
    else:
        great = list1[i+1]
    
print("The word with maximum number of length is:",great)
