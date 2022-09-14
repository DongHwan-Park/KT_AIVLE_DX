ot,baji = map(int,input().split())
ot_gul, baji_gul = map(int,input().split())

if ot_gul >= ot :
    if ot_gul - ot + baji_gul - baji >= 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')