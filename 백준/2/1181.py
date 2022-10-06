n = int(input())

result = []
word_list = list(set(input() for _ in range(n)))
word_list.sort(key=len)
# print(word_list)
len_list = []

for word in word_list:
    len_list.append(len(word))
a = []    
for i in range(max(len_list)):
    if i+1 in len_list:
        a.append(len_list.index(i+1))
    # else:
    #     a.append('n')
# print(a)   

for num in range(len(a)):
    if num != len(a)-1:
        result += (sorted(word_list[a[num] : a[num+1]]))
    else:
        result += (sorted(word_list[a[num] :]))

for word in result:
    print(word)




