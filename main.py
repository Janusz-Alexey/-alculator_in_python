import math

A: int = 0
B: int = 0
C: int = 0


x = 0
D = 0
x1 = 0
x2 = 0
Boss = 0
A = int(input('Введите A:='))
B = int(input("Введите B:="))
C = int(input("Введите C:="))

def funcfion():
    if int (A) == 0:
        global Boss
        Boss == 1
    elif int (B) ==0:
        Boss == 2
    elif int (C) == 0:
        Boss = 3
    elif B == C == 0:
        Boss = 4


def Happy():
    if Boss == 4:
        global x
        x = 0
    elif Boss == 3:
        global x1
        global x2
        x1 = 0
        x2 = -B / A
    elif Boss == 2 ((-C / A) > 0):
        x1 = math.sqrt(-C / A)
        x2 = -(math.sqrt(-C / A))
    elif Boss == 2 ((-C / A) < 0):
        print("Нет решения")
    elif Boss == 1:
        x = -B / C
    pass


def equation():
    global D
    D = B * B - 4 * A * C
    print("Дискриминант = ", D)


def x2():
    if D < 0:
        print("нет корней")
    elif D == 0:
        global x
        x = B / (A * 2)
        print(x)
    elif D > 1:
        global x1
        global x2
        x1 = ((-B) + math.sqrt(D)) / (2 * A)
        x2 = ((-B) - math.sqrt(D)) / (2 * A)
        print("x1:=", x1)
        print("x2:=", x2)


import math

A: int = 0
B: int = 0
C: int = 0


x = 0
D = 0
x1 = 0
x2 = 0
Boss = 0
A = int(input('Введите A:='))
B = int(input("Введите B:="))
C = int(input("Введите C:="))

def funcfion():
    if int (A) == 0:
        global Boss
        Boss == 1
    elif int (B) ==0:
        Boss == 2
    elif int (C) == 0:
        Boss = 3
    elif B == C == 0:
        Boss = 4


def Happy():
    if Boss == 4:
        global x
        x = 0
    elif Boss == 3:
        global x1
        global x2
        x1 = 0
        x2 = -B / A
    elif Boss == 2 ((-C / A) > 0):
        x1 = math.sqrt(-C / A)
        x2 = -(math.sqrt(-C / A))
    elif Boss == 2 ((-C / A) < 0):
        print("Нет решения")
    elif Boss == 1:
        x = -B / C
    pass


def equation():
    global D
    D = B * B - 4 * A * C
    print("Дискриминант = ", D)


def x2():
    if D < 0:
        print("нет корней")
    elif D == 0:
        global x
        x = B / (A * 2)
        print(x)
    elif D > 1:
        global x1
        global x2
        x1 = ((-B) + math.sqrt(D)) / (2 * A)
        x2 = ((-B) - math.sqrt(D)) / (2 * A)
        print("x1:=", x1)
        print("x2:=", x2)
