a = int(input("Limit predkosci: "))
b = int(input("Predkosc pojazdu: "))

if a == 50:
    if b <= 60:
       print("Mandat wynosi :", 5*b)
    elif b > 60:
        print("Mandat wynosi :", 