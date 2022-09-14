# 12
n = int(input())
num_list = list(map(int,input().split()))

ans = sorted(num_list)
cnt = 0

def do(list):
    global cnt
    if list[0] != min(list):
        for i in range(n):
            if sorted(num_list[ : i+1]) + num_list[i+1 :] == ans: 
                return i+1
    elif list[0] == min(list):
        cnt +=1
        list = list[1:]
        return do(list)    
        
print(do(num_list)-cnt)  