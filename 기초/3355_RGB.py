import numpy as np

n, m = map(int, input().split())

list1 = [input().split() for _ in range(n)]
list2 = [input().split() for _ in range(n)]

arr1 = np.array(list1)
arr2 = np.array(list2)

# 신규 배열 초기화 및 생성시 데이터형식 맞춰서 넣어주기!!

arr3 = np.zeros((n,m), dtype = "U4")
for i in range(n):
    for j in range(m):
        summ = arr1[i][j] + arr2[i][j]
        if summ == 'GB' or summ == 'BG':
            arr3[i][j] = 'C'
        elif summ == 'RB' or summ == 'BR':
            arr3[i][j] ='M'
        elif summ == 'RG' or summ == 'GR' :
            arr3[i][j] = 'Y'
        elif summ == 'RR':
            arr3[i][j] ='R'
        elif summ == 'GG' :
            arr3[i][j] ='G'
        elif summ == 'BB':          
            arr3[i][j] = 'B' 

for i in range(n):
    for j in range(m):
        print(arr3[i,j],end =' ')
    print()