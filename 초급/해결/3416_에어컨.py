comp_list = [x+1 for x in range(30)] # [1,2,3~30]
cnt_list = [0] * 31
want_list = []

# s e 값을 받은 n개의 리스트 만들기
n = int(input())
for _ in range(n):
    s ,e = map(int, input().split())
    for i in range(s,e+1):
        cnt_list[i] += 1

print(cnt_list.index(max(cnt_list)))
            
        