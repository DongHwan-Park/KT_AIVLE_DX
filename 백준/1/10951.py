result = []
while 1:
    try :
        num = list(map(int,input().split()))
        if sum(num) == 0:
            break
        
        else:    
            result.append(sum(num))
        
    except EOFError:
        break
        
for i in result:
    print(i)
