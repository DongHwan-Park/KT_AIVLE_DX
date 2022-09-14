a, b, c = map(int,input().split())
sik = b**2 * c - a**2
# print(sik)
if sik >= 0 :
    print('YES')
else :
    print('NO')