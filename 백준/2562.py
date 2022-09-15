num_list =[]
for _ in range(9):
    n = int(input())
    num_list.append(n)

m = max(num_list)
print(m,num_list.index(m)+1, sep='\n')