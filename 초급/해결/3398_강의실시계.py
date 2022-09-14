import datetime

now = input()
delta = int(input())
cnt = int(input())

date_format = '%H:%M:%S'
tmp =datetime.datetime.strptime(now,date_format)
# tmp2 = datetime.datetime.strptime(delta,date_format)

tmp2 = datetime.timedelta(seconds= delta*(cnt-1))
ans = tmp + tmp2
answer = datetime.datetime.strftime(ans,date_format)
print(answer)
