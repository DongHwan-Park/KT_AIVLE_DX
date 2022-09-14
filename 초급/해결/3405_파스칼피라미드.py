import numpy as np
n = int(input())


ans = [[0]*15 for _ in range(n+1)]

ans [0][0] = 1
for i in range(1,n):
    for j in range(i+1):
        ans[i][j] = ans[i-1][j-1] + ans[i-1][j]


for i in range(n-1,-1,-1):
    for j in range(i+1):
        print(ans[i][j] * ans[n-1][i],end = ' ')
    print() 

# ans_arr = np.array(ans)

# ans_arr[1:n-1] = ans_arr[1:n-1] * (n-1)


# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         print(ans_arr[i][j], end = ' ')
#     print()