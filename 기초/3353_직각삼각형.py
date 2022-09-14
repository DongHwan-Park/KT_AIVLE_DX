a,b,c = map(int , input().split())

list_a = [a,b,c]
min_num = min(list_a)
max_num = max(list_a)
if a == min_num :
    if b == max_num :
        mid_num = c 
    else:
        mid_num = b
elif b == min_num :
    if a == max_num :
        mid_num = c
    else:
        mid_num = a
elif c == min_num:
    if a == max_num:
        mid_num = b 
    else:
        mid_num = a
        
print(int((min_num * mid_num / 2)))
