arr = [[1,2,3,4,5],
      [6,7,8,9,10],
      [11,12,13,14,15],
      [16,17,18,19,20],
      [21,22,23,24,25]]
def p(list_2d):
    for line in list_2d:
        print(line)
num = 3
for i in range(num): # len(li) -num+1 정사각형이아닌경우
    for j in range(num): # len(li) -num+1
        for row in arr[i:i+num]:
            row[j:j+num] = [0] * num
            print(p(arr))
            
print(arr)

