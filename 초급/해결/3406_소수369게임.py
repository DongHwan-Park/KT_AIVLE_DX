check_list = []
def is_sosu(num):
    for i in range(1,num+1):
        global check_list 
        if num % i == 0:
            check_list.append(i)
    
    if len(check_list) == 2 :
        return True
    else:
        return False
    
n = int(input())

if is_sosu(n) :
    print('clap')
else:
    print(n)
    