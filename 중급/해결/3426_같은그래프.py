#4 1500
n, m  = map(int, input().split())
x = list([0] * 10)

for i in range(m):
    a,b = map(int, input().split())
    x[a-1] += 1
    x[b-1] += 1
    
# print(x)    
    
p, q  = map(int, input().split())
y = list([0] * 10)

for i in range(q):
    a,b = map(int, input().split())
    y[a-1] += 1
    y[b-1] += 1
    
# print(y)

if sorted(x) == sorted(y):
    print('YES')
else:
    print('NO')