num = int(input())
ans_list_1 = [1]

cnt_list = [0] * 20

for i in range(1,num):
    globals()['ans_list_'+str(i+1)] = []
    for j in range(1,max(globals()['ans_list_' + str(i)])+1):
        globals()['ans_list_'+str(i+1)].append(j)
        globals()['ans_list_'+str(i+1)].append(globals()['ans_list_'+ str(i)].count(j))
        
globals()['ans_list_'+str(num)]
for i in globals()['ans_list_'+str(num)]:
    print(str(i), end='')
