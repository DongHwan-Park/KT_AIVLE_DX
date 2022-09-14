S = list(input())
new_S = []
for x in S :
    if x == "\'" :
        new_S.append("\\\'")
    elif x == "\"" :
        new_S.append('\\\"')
    elif x == "\\" :
        new_S .append("\\\\")
    else :
        new_S.append(x)
new_S =''.join(new_S)
print(new_S)