import datetime

n = int(input())
now = datetime.datetime(year=2022, month=8, day=22, hour=12, minute=0, second=0)
# now = datetime(2022,12,31,12,00,00,000000)
def add_sec(now, count):
    result = now + datetime.timedelta(seconds = count)
    return result

ans = add_sec(now , -n)
print(ans.strftime('%H:%M:%S'))





