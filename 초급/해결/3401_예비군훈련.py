year, rok, dw, sinbun = input().split()

year = int(year)
rok = rok.upper()
dw = dw.upper()
sinbun = sinbun.capitalize()

if sinbun == "Private":
    if year >= 5 and dw=="N":
        print(20)
    elif year == 0 and dw=='N':
        print(0)
    else:
        if dw =="Y":
            print(28)
        else:
            if rok =="ROKAF":
                print(28)
            else:
                print(32)
elif sinbun == "Officer":
    if year == 0:
        print(0)
    else:
        print(28)