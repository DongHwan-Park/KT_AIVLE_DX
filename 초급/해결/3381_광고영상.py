n, k =map(int, input().split())

list_a = list(map(int, input().split()))

max_sum = 0

for i in range(n-k+1):
    
    if 0 in list_a[i:i+k]:
        
        continue
    else:
        if sum(list_a[i:i+k]) >= max_sum :
            max_sum = sum(list_a[i:i+k])
           
            
print(max_sum)