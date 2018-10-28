#Program liczacy wiek psa w psich latach

a = int(input("Podaj wiek psa: "))
if a <= 2:
    print(a*10.5)
if a > 2:
    print("Wiek psa w psich latach to: ", 21 + (a-2)*4)
