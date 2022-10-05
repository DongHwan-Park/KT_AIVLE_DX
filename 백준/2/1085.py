x,y,w,h = map(int, input().split())

l = x
u = h-y
r = w-x
b = y

selectlist=[l,u,r,b]

print(min(selectlist))