k = int(input())
state = True 
cnt = 1

def is_odd(b):
    if b % 2 == 1:
        return True
    else :
        return False
    
if k == 1 :
    print(2)
else:
    a = int(k/2)
    while state :
        if is_odd(a+cnt) :
            print(int(2 * (a+cnt)))
            state = False
        else:
            cnt+=1