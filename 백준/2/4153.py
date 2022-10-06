result = []
while 1:
    a,b,c = map(int, input().split())
    li = [a,b,c]
    if (a,b,c) !=(0,0,0):
        li = sorted(li)
        if li[0]**2 +li[1]**2 == li[2]**2:
            result.append('right')
        else:
            result.append('wrong')
        
    else:
        break
    
for _ in result:
    print(_)
    
