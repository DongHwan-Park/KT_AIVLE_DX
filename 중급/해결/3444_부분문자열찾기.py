a = list(input()) # abcde
b = list(input()) # ace
c= []
n = len(a)
for word in b :
    for w in a:
        if word != w:
            a = a[1:]
        elif word == w:
            c.append(w)
            break
# print(c)
if c == b:
    print('YES')
else:
    print('NO')


