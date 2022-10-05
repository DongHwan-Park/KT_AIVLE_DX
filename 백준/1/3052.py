num_list = list(int(input()) for _ in range(10))

for i in range(10):
    num_list[i] = num_list[i] % 42
    
print(len(set(num_list)))