# 10
# cols
al = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

cols = al
for i in range(26):
    for j in range(26):
        cols.append(al[i]+al[j])

for i in range(26):
    for j in range(26):
        for k in range(26):
            cols.append(al[i]+al[j]+al[k])
            
# rows
word = input().upper()
for i in range(len(word)):
    if word[:len(word)-i] in cols:
        word_word = word[:len(word)-i]
        word_num = word[len(word)-i:]
        break

# x -1 자리
print(cols[cols.index(word_word) -1] + word_num)

# y -1 자리
print(word_word + str(int(word_num)-1))

