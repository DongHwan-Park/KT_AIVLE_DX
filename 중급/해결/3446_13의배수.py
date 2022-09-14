from itertools import *
num_list = list(input())
# do 함수
def do(set):
    for i in set:
        check = ''.join(list(i))
        if int(check) % 13 == 0 :
            return 'YES'
    return 'NO'
# set
set_list = []
set_list = list(permutations(num_list,len(num_list)))
print(do(set_list))




