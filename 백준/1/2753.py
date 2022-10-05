n = int(input())

def is_yoon(num):
    if num % 4 ==0:
        if num % 100 != 0:
            print(1)
        elif num % 400 ==0:
            print(1)         
        else:
            print(0)
    else:
        print(0)
        
is_yoon(n)