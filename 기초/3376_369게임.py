# while True :
a = input()
cnt = 0
for i in list(a):   
    if  int(i) == 3:
        cnt += 1
    elif int(i) == 6:
        cnt += 1
    elif int(i) == 9:
        cnt += 1
        
if cnt  != 0 :
    print('clap' * cnt)
else :
    print(int(a))