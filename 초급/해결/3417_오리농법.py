import numpy as np

# n 차 정사각 배열 입력받기 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
# tmp = np.array(arr)
# arrT = tmp.T

# 각 행 기준 0 과 2 만 있을 시 해당행 0000으로 교체
for i in range(n):
    if 1 in arr[i] :
        continue
    else:
        arr[i] = [0]*n
        
# numpy 에서 전치행렬로 바꿔줌


tmp = np.array(arr)
arrT = tmp.T

# 행에 대해서 한 번 더 탐색
for i in range(n):
    if 1 in arrT[i]:
        continue
    else:
        arrT[i]=[0]*n

        
# arr안에 2 갯수 count
for i in range(n):
    for j in range(n):
        if arrT[i][j] == 2:
            cnt += 1

print(cnt) 

# 위 방식으로 하니 1 1 0
#                 2 2 2
#                 0 0 1 에서 3열 조건에서 부합하지않는데 행삭제가 일어남