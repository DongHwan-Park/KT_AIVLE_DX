n = int(input())

a, b = map(int,input().split())

minn = 3000
for _ in range(n):
    c, d = map(int,input().split())
    distance = abs(c-a) + abs(d-b)
    if distance <= minn:
        minn = distance
    
print(minn * 100)