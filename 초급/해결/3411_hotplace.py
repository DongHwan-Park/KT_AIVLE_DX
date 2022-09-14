n , r = map(int, input().split())

positions = []
for i in range(n):
    x,y = map(int,input().split())
    positions.append((x,y))
    
ans = []
for i in range(-120,121):
    for j in range(-120,121):
        cnt = 0 
        for posi in positions:
            if (posi[0]-i)**2 + (posi[1]-j)**2 <= r**2:
                cnt += 1
        ans.append((i,j,cnt))

# 중요 튜플 키값을 기준으로 정렬 (,reverse =True) 는 내림차순
ans.sort(key=lambda x :-x[2])
# print(ans[0:10])
print(ans[0][0], ans[0][1])