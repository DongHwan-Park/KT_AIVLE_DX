def check(i,j):
    x = arr[i][j]
    if i >= 1:
        x += arr[i-1][j]
    if i < n-1:
        x += arr[i+1][j]
    if j >= 1:
        x += arr[i][j-1]
    if j < m-1:
        x += arr[i][j+1]
    return x

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

summ = []

for i in range(n):
    for j in range(m):
        summ.append(check(i,j))
 
print(max(summ))