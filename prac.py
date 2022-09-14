n = int(input())
move = list(input().split())
start = [1,1]
posi = start
for key in move :
    if key== 'U' :
        if posi[1] == 1:
            pass
        else:
            posi[1] -= 1
    
    if key== 'D' :
        if posi[1] == n:
            pass
        else:
            posi[1] += 1
    if key== 'L' :
        if posi[0] == 1:
            pass
        else:
            posi[0] -= 1
    if key== 'R' :
        if posi[0] == n :
            pass
        else:
            posi[0] += 1
            
print(posi)