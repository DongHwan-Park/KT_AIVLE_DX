t = int(input())
result = []
for _ in range(t):
    h,w,n = map(int, input().split())
    a = str(n%h)
    b = str((n//h) +1) 
    hosu = int(a+'0'+b)
    result.append(hosu)

for i in result :
    print(i)