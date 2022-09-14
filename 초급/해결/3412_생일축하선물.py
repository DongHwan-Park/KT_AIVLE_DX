a = int(input())
list_b = list(map(int, input().split()))

new_list = []
sum_list2 = []
maxi = 0
ind = 0
mid = []
last_list = []
for n in range(a-2):
    new_list.append(list_b[n : n+3])
    sum_list2.append(sum(new_list[n]))
    if sum_list2[n] >= maxi : # 크거나 같은경우 중앙값이 더 큰걸 출력해야하는데..
       maxi = sum_list2[n]
       ind = n 
       mid.append(new_list[ind])
for n in range(len(mid)):
    last_list.append(sorted(mid[n])[1])

print(max(last_list))