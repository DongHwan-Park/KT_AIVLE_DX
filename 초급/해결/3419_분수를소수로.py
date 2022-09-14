from decimal import Decimal as de, getcontext
getcontext().prec = 10000

a, b = map(int, input().split())

n = int(input())

ans = de(a)/de(b)

print(format(ans, f'.{n}f'))

