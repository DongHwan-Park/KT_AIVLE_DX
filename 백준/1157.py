word = input().upper()

dic ={}

for char in word:
    if char in dic:
        dic[char] +=1
    else:
        dic[char] = 1
st_word = sorted(dic.items() ,key =  lambda x: x[1], reverse =True)
if len(st_word) >1:
    if st_word[0][1] == st_word[1][1]:
        print('?')
    else:
        print(st_word[0][0])
else:
    print(st_word[0][0])        