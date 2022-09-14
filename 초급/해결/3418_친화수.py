# 치훈이는 최근에 정수론 과목에서 친화수에 대해 배웠습니다.
# 두 양의 정수 A, B에 대하여, A의 진약수의 합이 B이고,
# B의 진약수의 합이 A라면 A와 B 쌍을 친화수 라고 합니다.
# (진약수란, 자기 자신을 제외한 약수를 말합니다.)
# 두 수의 쌍이 주어지면 친화수인지 판별하세요.

a, b = map(int, input().split())

def make_jinyaksu_list(num):
    new_list = []
    for i in range(num-1):
        if num % (i+1) == 0 :
            new_list.append(i+1)
            
    return new_list

list_a = make_jinyaksu_list(a)
list_b = make_jinyaksu_list(b)

if sum(list_a) == b  and sum(list_b) == a:
    print('YES')
else:
    print('NO')

    