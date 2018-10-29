x = int(input("Podaj zmienna x: "))
y = int(input("Podaj zmienna y: "))

if x == 0 and y == 0:
    print("Punkt (x,y) znajduje sie na poczatku ukladu")
elif x > 0 and y == 0:
    print("Punkt (x,y) znajduje sie na osi X")
elif x < 0 and y == 0:
    print("Punkt (x,y) znajduje sie na osi X")
elif x > 0 and y > 0:
    print("Punkt (x,y) znajduje sie w 1 cwiartce")
elif x < 0 and y > 0:
    print("Punkt (x,y) znajduje sie w 2 cwiartce")
elif x < 0 and y < 0:
    print("punkt (x,y) znajduje sie w 3 cwiartce")
elif x > 0 and y < 0:
    print("punkt (x,y) znajduje sie w 4 cwiartce")
          