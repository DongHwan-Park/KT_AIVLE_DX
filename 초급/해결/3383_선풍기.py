# 15

n = int(input())
a =input().upper()
# lst = ['OOOOO', 'OOOOX', 'OOOXO', 'OOOXX', 'OOXOO', 'OOXOX', 'OOXXO', 'OOXXX', 
#        'OXOOO', 'OXOOX', 'OXOXO', 'OXOXX', 'OXXOO', 'OXXOX', 'OXXXO', 'OXXXX', 
#        'XOOOO', 'XOOOX', 'XOOXO', 'XOOXX', 'XOXOO', 'XOXOX', 'XOXXO', 'XOXXX', 
#        'XXOOO', 'XXOOX', 'XXOXO', 'XXOXX', 'XXXOO', 'XXXOX', 'XXXXO', 'XXXXX']
cnt = 0
state = True
while state :

    if 'O' in list(a):
        if a[0:3] == 'OXO':
            a = a[3:]
            cnt +=1
            # print(a)
        # elif a[0:3] == 'XOX':
        #     a = a[2:]
        #     cnt += 1
        #     # print(a)
        elif a[0:2] == 'OX' :
            a = a[2:]
            cnt += 1
            # print(a)
        elif a[0:4] =='XOXO':
            a = a[4:]
            cnt +=1
        elif a[0:2] =='XO':
            a = a[2:]
            cnt += 1
            # print(a)
        elif a[0:2] =='XX':
            a = a[1:]
            # cnt += 1
    else:
        state = False
print(cnt)