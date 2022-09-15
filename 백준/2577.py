a = int(input())
b = int(input())
c = int(input())

num = a*b*c
# print(num)
dic ={}
for _ in range(10):
    dic[_] = 0
st = str(num)
for n in st:
    if int(n) in dic:
        n = int(n)
        dic[n] += 1
    # else:
    #     n = int(n)
    #     dic[n] = 1

for items in dic:
    print(dic[items])