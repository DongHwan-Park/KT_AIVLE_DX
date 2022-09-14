# 1234 입력후 [1,2,3,4] 각 요소 int 로 저장
list_num = input()
list_num = list(list_num)

for i in range(len(list_num)):
    list_num[i] = int(list_num[i])
    
# 오름차순 정렬 후 map
list_num = sorted(list_num)   
a,b,c,d = list_num[0],list_num[1],list_num[2],list_num[3]
summ = sum(list_num)
# if summ % 2 == 0 : # 짝수일때 돌아가기
#     half = summ / 2
#     if a + d == half:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
    
if a+d == b+c:
    print('YES')
else:
    print('NO')



