a = int(input())

c =[]
for num in range(a):
    b = int(input())
    c.append(b)

for x in c :
    if x % 2 == 0 :
        print('R')
    else : 
        print('L')