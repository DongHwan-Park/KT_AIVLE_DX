# 13
import numpy as np

h, w = map(int,input().split())
arr = list(list(input()) for _ in range(h))
# arr = np.array(arr)

empty = np.empty( dtype=str, shape= (h,w))

h2,w2 =map(int,input().split())
arr2 = list(list(input()) for _ in range(h2))


for i in range(h2):
    for j in range(w2):
        empty[h-h2+i][w-w2+j] = arr2[i][j]
    


ans = np.empty( dtype=str,shape= (h,w))

for i in range(h):
    for j in range(w):
        if empty[i][j]=='.':
            empty[i][j] = ''
            c = empty[i][j] + arr[i][j] 
            ans[i][j] = c
        else: 
            ans[i][j] = empty[i][j] + arr[i][j]
# print('arr')        
# print(arr)
# print('empty')
# print(empty)
# print('ans')               
# print(ans)

for i in range(h):
    print(''.join(ans[i]))


