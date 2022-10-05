a,b = map(int,input().split())

def trans(num):
    x = num // 100
    num = num - x*100
    y = num // 10
    num = num - y*10
    z = num // 1
    return z*100 + y*10+ x*1

result_a = trans(a)
result_b = trans(b)

if result_a >= result_b:
    print(result_a)
else:
    print(result_b)
    

