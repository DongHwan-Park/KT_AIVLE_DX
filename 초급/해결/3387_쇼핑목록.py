#우선순위 높은 같으면 싼 물건에다가 거리가 가까운순
# a,b,c 에서 a는 내림차순, 오름, 오름
n = int(input())
list_a = []
dic= {}

for i in range(n):
    k = i
    value = list(map(int, input().split()))
    dic[k] = value
    
dic = dict(sorted(dic.items(), key = lambda x : (-x[1][0], x[1][1], x[1][2])))


for key in dic:
    print( key + 1 , end=' ')
    