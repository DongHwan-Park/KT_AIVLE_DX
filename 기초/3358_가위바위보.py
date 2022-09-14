def game(f,s,score_a,score_b):
    global score_f, score_s
    if f == s :
        return   
    elif f == 1 and s == 3:
        score_f = score_a + 1
    elif f == 3 and s == 1 : 
        score_s = score_b + 1
    elif s > f :
        score_s = score_b + 1
    elif s < f :
        score_f = score_a + 1
    else:
        return
 
    return score_f , score_s

score_f = 0
score_s = 0 

t = int(input())
    
for i in range(t):
    a,b = map(int,input().split())
    game(a,b,score_f,score_s)
print(score_f,score_s)
    
    
# n  = int(input())
# a,b = 0,0
# for _ in range(n):
#     x,y = map(int,input().split())
#     if x == y :
#         continue
#     elif x == 1:
#         if y == 2:
#             b += 1
#         else : 
#             a += 1
#     elif x == 2:
#         if y == 1:
#             a+=1
#         else :
#             b+=1
#     else:
#         if y == 1:
#             b+=1
#         else:
#             a+=1
# print(a,b)
