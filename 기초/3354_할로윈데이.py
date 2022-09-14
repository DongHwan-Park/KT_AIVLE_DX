def is_int(a):
    if a == int(a):
        return True
    else :
        return False
    
num = int(input())

if is_int(num / 3) == True :
    print('YES')
else:
    print('NO')