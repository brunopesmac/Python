numero1 = float(input ("Digite o 1 numero: "))
numero2 = float(input ("Digite o 2 numero: "))
numero3 = float(input ("Digite o 3 numero: "))
if numero1 > numero2 and numero1 > numero3:
    if numero2>numero3:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero1,numero3))
    if numero3>numero2:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero1,numero2))
if numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero2,numero3))
    if numero3 > numero1:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero2,numero1))
if  numero3 > numero1 and numero3 > numero2:
    if numero1 > numero2:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero3,numero2))
    if numero2 > numero1:
        print("O maior numero é o {:.2f} e o menor é o {:.2f}".format(numero3,numero1))
