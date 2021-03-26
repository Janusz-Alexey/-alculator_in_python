import math

print("A*X*X+B*X+C")
A = int(input('Введите A:='))
B = int(input("Введите B:="))
C = int(input("Введите C:="))

x = 0
D = 0
x1 = 0
x2 = 0
def equation():
    global D
    D = B * B - 4 * A * C
    print("Дискриминант = ",D)


equation()

def x2():
    if D < 0:
        print("нет корней")
    elif D == 0:
        global x
        x = B/(A*2)
        print(x)
    elif D > 1:
        global x1
        global x2
        x1 = ((-B) + math.sqrt(D))/(2*A)
        x2 = ((-B) - math.sqrt(D)) / (2 * A)
        print("x1:=", x1)
        print("x2:=", x2)
x2()
