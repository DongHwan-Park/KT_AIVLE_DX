a, b = map(int, input().split())
# list_ans = []
list_who = [0] * a
for _ in range(b):
    price , man = map(int,input().split())
    list_w = list(map(int,input().split()))
    price_per_man = int(price / man)
    for num in list_w :
        list_who[num-1] += price_per_man
        

for n in range(a):
    print(list_who[n],end=' ')


