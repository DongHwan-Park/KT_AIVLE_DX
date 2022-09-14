from itertools import *
n = int(input())

num_list = list(map(int,input().split()))

l = list(map(list,combinations(num_list,4)))

state = True
while state :
    for i in l:
        if i[0] * i[1] == i[2] * i[3]:
            print('YES')
            state = False
            break
        elif i[0] * i[2] == i[1] * i[3]:
            print('YES')
            state = False
            break
        elif i[0] * i[3] == i[1] * i[2]:
            print('YES')
            state = False
            break
        elif i[0] * i[1] == i[2] * i[3]:
            print('YES')
            state = False
            break
    if state == True:
        print('NO')
    state=False
    
