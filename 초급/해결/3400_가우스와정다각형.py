n = int(input())
n_p = [2,3,5,17,257,65537]
# n_2 = [2**x for x in range(27) if 2**x < 10**8]
# n_2 = sorted(n_2,reverse=True)
yaksu = True
state = True
while state :
    if n == 1:
        state = False
        break
    # 페르마 숫자인 경우
    drop = 1
    for num in n_p:
        if n % num == 0 :
            drop = num
            break
    if drop == 1 :
        state = False
        yaksu = False
        break
    else:
        n = n // drop
        if  drop != 2:
            n_p.remove(drop)
            
if yaksu == False:
    print('NO')
else:
    print('YES')
            
       