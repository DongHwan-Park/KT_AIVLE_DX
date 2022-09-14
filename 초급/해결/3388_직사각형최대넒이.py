# n 개막대기중 4개골라서 직사각형 중 가장 큰 넓이
n = int(input())
list_n = list(map(int, input().split()))
num_list = []
# n개 변수 생성
for num in range(10):
    num_list.append(0)

def add_cnt(number):
    num_list[number-1] += 1
    
for num in range(n):
    if list_n[num] % 10 == 1:
        add_cnt(1)        
    elif list_n[num] % 10 ==2:
        add_cnt(2)
    elif list_n[num] % 10 ==3:
        add_cnt(3)
    elif list_n[num] % 10 ==4:
        add_cnt(4)
    elif list_n[num] % 10 ==5:
        add_cnt(5)
    elif list_n[num] % 10 ==6:
        add_cnt(6)
    elif list_n[num] % 10 ==7:
        add_cnt(7) 
    elif list_n[num] % 10 ==8:
        add_cnt(8)
    elif list_n[num] % 10 ==9:
        add_cnt(9)
    elif list_n[num] % 10 == 0: 
        add_cnt(10)
        
# list 에서 value 값으로 다중 index 추출

list_2 = list(filter(lambda x : num_list[x] == 2, range(len(num_list))))
list_4 = list(filter(lambda x : num_list[x] ==4, range(len(num_list))))
last_list =[0]

# 최대값 구하기
if len(list_2) >= 2 :
    # 인덱스 값 + 1
    a = list_2.pop() + 1
    b = list_2.pop() + 1
    last_list.append(a * b)
elif len(list_4) >=1 :
    # 인덱스 값 + 1
    c = list_4.pop() + 1
    last_list.append(c ** 2)
if max(last_list) != 0:
    print(max(last_list))
else:
    print(0)
# list_4 = [num_list.index(x) for x in num_list if x == 4]
# print(list_4)
# list_2 = [num_list.index(x) for x in num_list if x == 2]
# print(list_2)

# if list_4 != 0:
#     print((list_4.pop() + 1)**2)
# # if 4 in num_list:
# #     print((num_list.index(4)+1)**2)
