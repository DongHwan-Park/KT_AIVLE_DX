# N개의 통에 사탕이 담겨 있습니다. 치훈이는 다음 2가지 연산을 이용해 모든 통에 들어있는 사탕의 개수가 같게 만드려고 합니다.

# 1. 임의의 통에 있는 사탕을 하나 먹는다.
# 2. 임의의 통에 있는 사탕을 다른 통으로 옮긴다.
# 이 때, 필요한 연산의 최소 횟수를 출력하는 프로그램을 작성해주세요.

n = int(input())
list_ball = list(map(int,input().split()))

def get_rid_1(lst):
    global list_ball
    m = lst.index(max(list_ball))
    lst[m] -= 1
    return lst

cnt =0

# 사탕갯수가 통개수의 배수에 맞게 먹고 count 하기
while sum(list_ball) % n != 0 :
    list_ball = get_rid_1(list_ball)
    cnt += 1
    
for i in list_ball:
    avg = sum(list_ball) / n
    if i > avg:
        cnt += i - avg    
        
print(int(cnt))