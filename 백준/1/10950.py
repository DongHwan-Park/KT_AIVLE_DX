n = int(input())
num_list = list(list(map(int, input().split())) for _ in range(n))


for i in range(n):
    print(sum(num_list[i]))
