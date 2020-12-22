

arr=[17,92,18,33,58,7,100,42]

arr.insert(0,101)
arr.pop(0)
arr.append(102)

print(58 in arr)
print(len(arr))

def mf(arr):
    index=0
    for i in range(1,len(arr)):
        if arr[i]>arr[index]:
            index=i
    
    return arr[index]
            
    
print(mf(arr))