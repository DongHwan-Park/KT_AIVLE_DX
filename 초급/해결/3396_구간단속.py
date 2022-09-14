# 15
from datetime import datetime
import time
import math

meter = int(input())
n = int(input())

time_stamp = list(input().split() for _ in range(n*2))
for i in range(n*2):
    time_stamp[i][1] = datetime.strptime(time_stamp[i][1],'%H:%M:%S')

time_stamp = sorted(time_stamp)

for i in range(n):
    t = (((time_stamp[i*2 + 1][1]-time_stamp[i*2][1]).seconds)/3600)
    print(time_stamp[i*2][0], math.floor(meter/t), sep=' ')

