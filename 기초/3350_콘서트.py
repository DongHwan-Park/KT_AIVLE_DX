week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
week2= week * 2
n = int(input()) % 7
input_week = input()

# week2[input_week]
print(week2[week.index(f'{input_week}') + n])
