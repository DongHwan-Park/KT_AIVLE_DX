import numpy as np

# n 행 m 열
n, m  = map(int, input().split())

# 초기 입력 n 행 m 열 --> 땅 g 바다 o 들고양이 c
grd = list(list(input()) for _ in range(n))

# 0 으로 채워진 c, o 위치에 대한 배열
arr_c = np.zeros((n,m),dtype= int)
arr_o = np.zeros((n,m),dtype= int)

# a = 바다로부터 거리가 a보다 같거나 작다.
# b = 모든 '들고양이 서식지' 칸과의 거리가 b보다 크다.
a, b = map(int,input().split())

# grg 카운트
cnt_g = 0

# c 고양이 , o 바다 위치 list 저장
list_o = []
list_c = []
for i in range(n):
    for j in range(m):
        if grd[i][j] == 'o' :
            list_o.append([i ,j])
        elif grd[i][j] == 'c':
            list_c.append([i, j])

for i in range(n):
    for j in range(m):
        if grd[i][j] == 'g':
            for num in range(len(list_o)):
                dis_o = abs(i-list_o[num][0]) + abs(j-list_o[num][1])
                if dis_o  <= a:
                    # 가능의 1 이후 c에 대해서도 1이 더해져서 총 2가될때 'g' count
                    arr_o[i][j] += 1
            for num in range(len(list_c)):
                dis_c = abs(i-list_c[num][0]) + abs(j-list_c[num][1])
                # 고양이의 경우 안되는경우를 1로하여 다시 1->0 , 0->1 치환
                if dis_c <= b :
                    arr_c[i][j] += 1
# check
new_arr_c =np.ones((n,m),dtype=int)
arr_o = np.where(arr_o != 0 , 1, arr_o)
new_arr_c = np.where(arr_c != 0, 0, new_arr_c)
# print('o')
# print(arr_o)
# print('c')
# print(arr_c)
# print('new_c')
# print(new_arr_c)
# 결과 count                    
ans_cnt = 0                                               
summ = arr_o + new_arr_c
for i in range(n):
    for j in range(m):
        if summ[i][j] >= 2 :
            ans_cnt +=1
           
print(ans_cnt)
      