n = int(input())
word = input()

word = list(word)
result = []
for w in range(len(word)):
    num = ord(word[w])-96
    result.append(num * (31**w))

print(sum(result)%1234567891)