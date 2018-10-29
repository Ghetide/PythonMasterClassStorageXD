x = -1
y = -1

if x==0 and y==0:
    print(f"Punkt P({x},{y}) znajduje się w początku układu współrzędnych.")
elif x==0:
    print(f"Punkt P({x},{y}) znajduje się na osi OY.")
elif y==0:
    print(f"Punkt P({x},{y}) znajduje się na osi OX.")
elif x<0:
    if y>0:
        print(f"Punkt P({x},{y}) znajduje się w II ćwiartce układu wspolrzednych")
    elif y<0:
        print(f"Punkt P({x},{y}) znajduje się w III ćwiartce układu wspolrzednych")
elif x>0:
    if y>0:
        print(f"Punkt P({x},{y}) znajduje się w I ćwiartce układu wspolrzednych")
    elif y<0:
        print(f"Punkt P({x},{y}) znajduje się w IV ćwiartce układu wspolrzednych")