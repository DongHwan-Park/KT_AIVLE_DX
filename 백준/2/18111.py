num_list = []
while 1:
    num = input()
    if num == '0' :
        break
    if list(reversed(list(num))) == list(num) :
        num_list.append('yes')
    else:
        num_list.append('no')

for i in num_list:
    print(i)
        
