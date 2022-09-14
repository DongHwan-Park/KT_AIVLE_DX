import numpy as np

n,a,b,c = map(int,input().split())

# n * n  빈 배열
arr= list([0]*n for _ in range(n))


def air(x,y,array,n):
    global b
    for i in range(1,b+1):
        if x-1+i <= n-1:
            arr[x-1+i][y-1] += 1
        if x-1-i >= 0:
            arr[x-1-i][y-1] += 1
        if y-1+i <= n-1:
            arr[x-1][y-1+i] += 1
        if y-1-i >= 0 :
            arr[x-1][y-1-i] += 1
        arr[x-1][y-1] = -50    
    # array[x-1][y-1] -= 2
    return array

for num in range(a):
    x,y = map(int,input().split())
    arr = air(x,y,arr,n)
    
cnt = 0
for i in range(n):
    for j in range(n):
        
        if arr[i][j]  >= c :
            cnt +=1
            
# print(np.array(arr))    
print(cnt)
    