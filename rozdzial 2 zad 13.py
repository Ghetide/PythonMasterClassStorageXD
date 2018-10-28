a = float(input("Podaj a dla rownania ax^2+bx+c=0: "))
b = float(input("Podaj b dla rownania ax^2+bx+c=0: "))
c = float(input("Podaj c dla rownania ax^2+bx+c=0: "))
delta = ((b*b)-(4*a*c))
if delta > 0:
    print("Delta wynosi: ", delta)
    x1 = ((-b-delta**0.5)/2*a)
    print("pierwszy pierwiastek wynosi: ", x1)
    x2 = ((-b+delta**0.5)/2*a)
    print("drugi pierwiastek wynosi: ", x2)
elif delta == 0:
    print("Delta wynosi: ", delta)
    x0 = ((-b)/(2*a))
    print("pierwiastek wynosi: ", x0)
elif delta < 0:
    print("Rownanie nie posiada pierwiastkow")