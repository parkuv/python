
arr=["tom","jerry","mike","tom"]

def findsame(n):
    for i in n:
        for j in range(len(n)+1):
            if i == n[j]:
                return i
    
print(findsame(arr))