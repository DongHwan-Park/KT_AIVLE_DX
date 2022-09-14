#8 200~400
n = int(input())
space = [int((n**2 + n + 2)/2) for n in range(1,45) if (n**2 + n + 2)/2 <= 1000]
#[2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154,
# 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497,
# 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991]
# for i in range(len(space)) :
#     if space[i] < n <= space[i+1]:
#         print(i+1)
new = space
new.append(n)
new = sorted(new)
# print(new)
if n == 1:
    print(0)
else:
    print(new.index(n)+1)
