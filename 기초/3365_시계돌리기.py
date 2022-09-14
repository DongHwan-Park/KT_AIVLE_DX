a, b = map(int,input().split())
def do(a,b):
    way1 = 60 - b + a 
    way2 = b - a
    if way1 <= way2 :
        print(way1)
    else :
        print(way2)
if a <= b :
    do(a,b)
        
else :
    do(b,a)