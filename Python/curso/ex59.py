a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
num = int
while num != 5:  
    num = int(input("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair\n"))
    if num == 1:
        print ("{:.2f} + {:.2f} = {:.2f}".format(a,b,a+b))
    if num == 2:
        print ("{:.2f} x {:.2f} = {:.2f}".format(a,b,a*b))
    if num == 3:
        if a > b:
            print ("{} > {}".format(a,b))
        else:
            print ("{} > {}".format(b,a))
    if num == 4:
        a = float(input("Digite um numero: "))
        b = float(input("Digite um numero: "))
    if num > 5:
        print ("Comando inexistente! Programa reiniciando!")
        num == 4
print("Programa finalizado!")