n = int(input())
word_list = list(list(input().split()) for _ in range(n))
# print(word_list)
result = []
for word in word_list:
    # print(word)
    # print(word[0])
    sup = int(word[0])
    sup_word=''
    for spelling in word[1]:
        sup_word += spelling*sup
    result.append(sup_word)
    
for i in result:
    print(i)
    
