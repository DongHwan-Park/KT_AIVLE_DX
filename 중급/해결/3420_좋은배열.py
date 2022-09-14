#8 1000+
n = int(input())
num_list = list(map(int,input().split())) # [2,1,1,2,3,3]
tmp = []
tmp2 = []
state = True
for i in range(1,n+1):
    # tmp = []
    # tmp2 = []
    start = num_list.index(i)
    
    tmp = num_list[start+1:]
    end = tmp.index(i)
    
    tmp2 = tmp[end+1:]
    tmp = tmp[:end]
    if tmp != [] and tmp2 !=[]:
        for j in tmp:
            if j in tmp2 :
                # print('y')
                state = False

if state == False :
    print('NO')
else:
    print('YES')  

