cnt = int(input())

my_dict = {}
for i in range(cnt):
    key, val = input().split()
    my_dict[key] = int(val)
    
search_word = input()

if search_word in my_dict :
    print(my_dict[search_word])
else :
    print(-1)