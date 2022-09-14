text = input()

state = True

for i in range(1,len(text)+1): # text_len == 100 일때 1~100 까지
    len_slice = int(100/i) #
    for j in range(1,len_slice+1):
        if text[:i] * j == text :
            print(text[:i])
            state = False
            break
    if state == False:
        break

