a,b,D,d = list(map(int, input().split()))

a_ans_D = 0
b_ans_D = 0
a_ans_d = 0
b_ans_d = 0

def do_find_D(num=int,yaksu_list=list,mok_list=list):
    global a
    global D 
    global d
    tmp = []
    tmp_D = D
    tmp_yaksu_list = yaksu_list
    tmp_yaksu_list.append(D)
    tmp = sorted(tmp_yaksu_list)
    idx = tmp.index(D)
    state = True
    if num//tmp_D != mok_list[idx]:
        return tmp_D
    while state:
        if tmp_D  > d :
            if num//tmp_D == mok_list[idx] :
                tmp_D -= 1
                if num // tmp_D != mok_list[idx] :
                    state = False
                    break
        else:
            return tmp_D
    return tmp_D
        # 혹시 D 가 d를 만나는 경우가 있을 수 있음
def do_find_d(num=int,yaksu_list=list,mok_list=list):
    global a
    global D 
    global d
    tmp = []
    tmp_d = d
    tmp_yaksu_list = yaksu_list
    tmp_yaksu_list.append(d)
    tmp = sorted(tmp_yaksu_list)
    idx = tmp.index(d) - 1
    state = True
    if num//tmp_d != mok_list[idx]:
        return tmp_d
    while state:
        if tmp_d < D:
            if num//tmp_d == mok_list[idx]:
                tmp_d += 1
                if num // tmp_d != mok_list[idx] :
                    state = False
                    break
        else:
            return tmp_d
    return tmp_d    
   
# make yaksu list
a_yaksu = []
a_mok = []
for i in range(1,a+1):
    if a % i == 0:
        a_yaksu.append(i)
        a_mok.append(a//i)
b_yaksu = []
b_mok = []       
for i in range(1,b+1):
    if b % i == 0:
        b_yaksu.append(i)            
        b_mok.append(b//i)
        
# if D <= a and D <= b:
if a//d < 1 or a // D < 1 or b//D < 1 or b //d < 1 :
    print(-1)
else:
    if D == d :
        min = (a//D + b//D) * 2
        max = (a//d + b//d) * 2
        print(min,max)   
    else:    
        if D in a_yaksu :
            a_ans_D = D   
        else:
            a_ans_D = do_find_D(a,a_yaksu,a_mok)
        if D in b_yaksu:
            b_ans_D = D
        else:
            b_ans_D = do_find_D(b,b_yaksu,b_mok)
        if d in a_yaksu:
            a_ans_d = d
        else:
            a_ans_d = do_find_d(a,a_yaksu,a_mok)
        if d in b_yaksu:
            b_ans_d = d
        else:
            b_ans_d = do_find_d(b,b_yaksu,b_mok)    
        min = (a // a_ans_D + b // b_ans_D) * 2 
        max = (a // a_ans_d + b // b_ans_d) * 2 
        print(min,max)            
# else:
#     print(-1) 
    
# print('a_ans_D에 의한 a의 최솟값',a_ans_D)      
# print('b_ans_D에 의한 b의 최솟값',b_ans_D)
# print('a_ans_d에 의한 a의 최솟값',a_ans_d)      
# print('b_ans_d에 의한 b의 최솟값',b_ans_d)  

