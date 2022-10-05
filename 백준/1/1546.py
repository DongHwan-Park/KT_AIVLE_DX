n = int(input())
num_list = list(map(int,input().split()))
m = max(num_list)
print((100*sum(num_list)/m)/n)