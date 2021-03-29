import kivy
import cmath
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

def Happy():
    if A+B+C != 0:
        global D
        D = B * B - 4 * A * C
        if D < 0:
            print("нет корней")
        elif D == 0 and A != 0:
            global x
            x = B / (A * 2)
            print(x)
        elif D > 1 and A != 0 and B !=0:
            global x1
            global x2
            x1 = ((-B) + math.sqrt(D)) / (2 * A)
            x2 = ((-B) - math.sqrt(D)) / (2 * A)
            print("x1:=", x1)
            print("x2:=", x2)
    if A == B == C == 0:
        x = str('Любое число')
        print(x)
    elif C == 0 and A == 0:
        print(0)
    elif B == A == 0:
        x = C
        print('Это не уравнение!')
    elif B == C == 0:
        print(0)
    elif C == 0:
        x1 = 0
        x2 = -B / A
        print(x1)
        print(x2)
    elif A == 0:
        x = -B / C
        print(x)

    if B == 0 and A != 0 and C != 0:
        x1 = (cmath.sqrt(-C / A))
        x2 = -(cmath.sqrt(-C / A))
        print(x1)
        print(x2)
    elif A != 0 and C != 0 and B == 0 > (-C / A):
        x1 = print("Нет решения")
    else:
        pass
    return

Happy()
