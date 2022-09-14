a = int(input())
ans = a
state = True
while state :
    if ans % 3 == 0 and ans % a == 0:
        print(ans)
        state = False
    else:
        ans += 1