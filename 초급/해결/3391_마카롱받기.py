list_num = list(map(int,input().split()))
ans_list = []

if list_num[0] == 2:
    ans_list.append('L')  
    for n in range(1,len(list_num)):
        if list_num[n] == 2:
            if ans_list[n-1] == 'L':
                ans_list.append('R')
            else:
                ans_list.append('L')
        elif list_num[n] == 1 :
            ans_list.append('L')
        elif list_num[n] == 3 :
            ans_list.append('R')
else:
    for n in range(0,len(list_num)):
        if list_num[n] == 2:
            if ans_list[n-1] == 'L':
                ans_list.append('R')
            else:
                ans_list.append('L')
        elif list_num[n] == 1 :
            ans_list.append('L')
        elif list_num[n] == 3 :
            ans_list.append('R')        
for i in ans_list:
    print(i, end=' ')
