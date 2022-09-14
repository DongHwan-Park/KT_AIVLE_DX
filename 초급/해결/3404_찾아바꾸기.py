#13
word = input()

n = int(input())

new_word = []

for j in range(n):
    s,t,cur = input().split()
    cur = int(cur)
    word = word[:cur] + word[cur:].replace(s,t)
    print(word)
    

# for i in range(n):
#     print(new_word[i])