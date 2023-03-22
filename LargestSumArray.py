arr = [-5,10,11,3,8,-21,53]
y = len(arr)-1
mx = -1
firstindex = 0
lastIndex = 0
for i in range(y):
    if arr[i] + arr[i + 1] > mx:
        mx = arr[i] + arr[i + 1]
        firstindex  = arr[i]
        lastindex = arr[i+1]
        
        
print("largest sum is", mx)
print("first index is",firstindex )
print("last index is",lastindex )

        
