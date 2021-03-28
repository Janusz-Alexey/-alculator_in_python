import math

A: int = 0
B: int = 0
C: int = 0


x = 0
D = 0
x1 = 0
x2 = 0
Boss = 0
helper = 0
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
    elif B == A == 0:
        Boss = 5
    elif C == A == 0:
        Boss = 6
    elif A == B == C == 0:
        Boss = 7
    else:
        Boss = 8




def Happy():
    if Boss == 8:
        global helper
        helper = 1
    elif Boss == 7:
        global x
        x = str('Любое число')
        print(x)
    elif Boss == 6:
        x = 0
        print(x)
    elif Boss == 5:
        x = C
        print(x)
    elif Boss == 4:
        x = 0
        print(x)
    elif Boss == 3:
        global x1
        global x2
        x1 = 0
        x2 = -B / A
        print(x1)
        print(x2)
    elif Boss == 1:
        x = -B / C
        print(x)
    else:
        pass
def happy_2():
    if Boss == 2:
        global x1
        global x2
        x1 = math.sqrt(-C / A)
        x2 = -(math.sqrt(-C / A))
    elif 0 > (-C / A):
        x1 = print("Нет решения")


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


Happy()
happy_2()
x2()
