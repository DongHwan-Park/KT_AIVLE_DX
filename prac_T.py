def indexExists(l,ind):
    try:
        l[ind]
        return True
    except:
        return False

# 2차원 배열 입력받기
arr = [list(map(int, input().split())) for _ in range(10)]


cnt_5, cnt_4, cnt_3, cnt_2 , cnt_1 = 0, 0, 0, 0, 0 
total_cnt = 0
# for i in range(num): # len(li) -num+1 정사각형이아닌경우
#     for j in range(num): # len(li) -num+1
#         for row in arr[i:i+num]:
#             row[j:j+num] = [0] * num
ar= []
for i in range(10):
    for j in range(10):
        if indexExists(arr,j+4) & indexExists(arr,i+ 4):
            for row in arr[i:i+5]:
                ar += row
            if 0 not in ar:
                cnt_5 += 1
                for row in arr[i:i+5]:
                    row = [0]* 5
                    arr[i]
                
# for i in range(10):
#     for j in range(10):
#         if indexExists(arr,j + 3) & indexExists(arr,i + 3):
#             if 0 in arr[i:i+4,j:j+4] :
#                 pass
#             else:
#                 arr[i:i+4,j:j+4] = 0
#                 cnt_4 += 1
#                 total_cnt+=1
# for i in range(10):
#     for j in range(10):
#         if indexExists(arr,j+ 2) & indexExists(arr,i+ 2):
#             if 0 in arr[i:i+3,j:j+3] :
#                 pass
#             else:
#                 arr[i:i+3,j:j+3] = 0
#                 cnt_3 +=1 
#                 total_cnt+=1  
# for i in range(10):
#     for j in range(10):
#         if indexExists(arr,j+ 1) & indexExists(arr,i + 1):
#             if 0 in arr[i:i+2,j:j+2] :
#                 pass
#             else:
#                 arr[i:i+2,j:j+2] = 0
#                 cnt_2 +=1 
#                 total_cnt+=1
# for i in range(10):
#     for j in range(10):
#         if indexExists(arr,j) & indexExists(arr,i):
#             if 0 in arr[i:i+1,j:j+1] :
#                 pass
#             else:
#                 arr[i:i+1,j:j+1] = 0
#                 cnt_1 +=1   
#                 total_cnt+=1 
                
print(cnt_1,cnt_2,cnt_3,cnt_4,cnt_5)
print(arr) 
if cnt_3 > 5 or cnt_2 > 5 or cnt_1 > 5 :
    print(-1)
else:
    print(total_cnt)           


