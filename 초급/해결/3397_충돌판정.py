#13
from math import *
x1,y1,r1 = map(int, input().split())
x2,y2,r2 = map(int, input().split())


a=[x1-r1/2, x1+r1/2, y1-r1/2, y1+r1/2]
b=[x2-r2/2, x2+r2/2, y2-r2/2, y2+r2/2]


if (a[0]<=b[0]<=a[1] or a[0]<=b[1]<=a[1] \
    or b[0]<=a[0]<=b[1] or b[0]<=a[1]<=b[1] )\
    and (a[2]<=b[2]<=a[3] or a[2]<=b[3]<=a[3] \
    or b[2]<=a[2]<=b[3] or b[2]<=a[3]<=b[3]) :
    print('YES')
else:
    print('NO')