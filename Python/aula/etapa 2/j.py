#j
import math
a = 0.0
while a == 0:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    if a == 0:
        print("Valor de a tem que ser diferente de 0!")
delta = b**2 - 4*a*c
x1 = (-b + math.sqrt(delta))/2*a
x2 = (-b - math.sqrt(delta))/2*a
if delta > 0:
    print("A função possui duas raizes reais distintas sendo elas {:.2f} e {:.2f}".format(x1,x2))
if delta == 0:
    print("A função posusi uma única raiz real sendo ela {:.2f}".format(x1))
if delta < 0:
    print("A função não possui raiz real")
