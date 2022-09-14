n = int(input())

state = list(input().upper() for _ in range(n))

def reset(num):
    num = 0
    return num

a,b,c,d = 0,0,0,0
max_c = [0]
max_d = [0]
score_list = []
win_list =[]

# 초항 입력
if state[0] == 'WIN':
    score_list.append([1,0,1,0])
    win_list.append(1)
    max_c.append(1)
    a = 1
else :
    score_list.append([0,1,0,1])
    win_list.append(0)
    max_d.append(1)
    b = 1
    
for k in range(1,n):
    if win_list[k-1] == 1:
        #이기고 이김
        if state[k] == 'WIN':
            win_list.append(1) # 이기면 1 지면 0
            a += 1
            b = reset(b)
            if max(max_c) < a :
                max_c.append(a)
                score_list.append([a,b,max(max_c),max(max_d)])
            else :
                score_list.append([a,b,max(max_c),max(max_d)])
        #이기고 짐
        elif state[k] == 'LOSE':
            win_list.append(0)
            b += 1
            a = reset(a)
            if max(max_d) < b:
                max_d.append(b)
                score_list.append([a,b,max(max_c),max(max_d)])
            else:
                score_list.append([a,b,max(max_c),max(max_d)])
    
    elif win_list[k-1] == 0:
        # 지고 이김
        if state[k] == 'WIN':
            win_list.append(1) # 이기면 1 지면 0
            a += 1
            b = reset(b)
            if max(max_c) < a :
                max_c.append(a)
                score_list.append([a,b,max(max_c),max(max_d)])
            else :
                score_list.append([a,b,max(max_c),max(max_d)])
        #지고 짐
        elif state[k] == 'LOSE':
            win_list.append(0)
            b += 1
            a = reset(a)
            if max(max_d) < b:
                max_d.append(b)
                score_list.append([a,b,max(max_c),max(max_d)])
            else:
                score_list.append([a,b,max(max_c),max(max_d)])
            
for i in range(n):
    for j in range(4):
        print(score_list[i][j], end=' ')
    if i != n-1:
        print()
    else:
        break