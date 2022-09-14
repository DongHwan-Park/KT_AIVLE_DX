ot,baji = map(int,input().split())
ot_gul, baji_gul = map(int,input().split())
# way1 = a + b
# way2 = c + d
if baji > baji_gul:
    print('No')
else:
    if baji_gul - baji + ot_gul - ot >= 0:
        print('YES')
    else:
        print('NO')