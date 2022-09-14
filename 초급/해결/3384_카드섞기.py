num = int(input())
card_list = [0]

for i in range(num):
    up_down = input()
    if up_down == 'D' :
        
        card_list = [i+1] + card_list
        
    elif up_down == 'U' :
        
        card_list = card_list + [i+1]

# 숫자 이므로 리스트 각element 에 대해 join 불가
for i in range(num+1):
    print(card_list[i], end =' ')