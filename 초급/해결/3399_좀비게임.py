#15
ppl , who_is_zombie = map(int,input().split())
time = int(input())

zombie_list = []
zombie_list.append(who_is_zombie)

for i in range(time):
    a,b = map(int,input().split())
    if a in zombie_list or b in zombie_list:
        zombie_list.append(a)
        zombie_list.append(b)
    
    
print(len(set(zombie_list)))
