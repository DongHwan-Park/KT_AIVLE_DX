from ast import Delete
import numpy as np

a = list(list(map(int,input())) for _ in range(3))
a = np.array(a)

if a[0][0] == 1:
    a[1][2] +=3
    a[2][1] +=3
if a[0][1] == 1:
    a[2][0] +=3
    a[2][2] +=3
if a[0][2] == 1:
    a[1][0] +=3
    a[2][1] +=3
if a[1][0] == 1:
    a[0][2] +=3
    a[2][2] +=3
# if a[1][1] == 1:
#     pass
if a[1][2] == 1:
    a[0][0] +=3
    a[2][0] +=3
if a[2][0] == 1:
    a[0][1] +=3
    a[1][2] +=3
if a[2][1] == 1:
    a[0][0] +=3
    a[0][2] +=3
if a[2][2] == 1:
    a[0][1] +=3
    a[1][0] +=3         

# print(a)
if a[1][1] != 0 :
    print('impossible')
elif 5 in a  or 8 in a:
    print('possible')
else:
    print('impossible')