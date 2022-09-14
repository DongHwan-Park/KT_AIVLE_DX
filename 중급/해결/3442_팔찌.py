#26 300~500

a = input()
b = input()
cnt = 0
for i in range(len(a)):
    b = b[i:] + b[:i]
    if a == b :
        cnt +=1
        break
        
if cnt >= 1:
    print('YES')
else:
    print('NO')