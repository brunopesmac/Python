#g
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
num = int
while num != 6:  
    num = int(input("[1]somar\n[2]subtrair\n[3]multiplicar\n[4]dividir\n[5]novos numeros\n[6]sair\n"))
    if num == 1:
        print ("{:.2f} + {:.2f} = {:.2f}".format(a,b,a+b))
    if num == 2:
        print ("{:.2f} - {:.2f} = {:.2f}".format(a,b,a-b))
    if num == 3:
        print ("{:.2f} x {:.2f} = {:.2f}".format(a,b,a*b))
    if num == 4:
        print ("{:.2f} / {:.2f} = {:.2f}".format(a,b,a/b))
    if num == 5:
        a = float(input("Digite um numero: "))
        b = float(input("Digite um numero: "))
    if num > 6:
        print ("Comando inexistente! Programa reiniciando!")
        num == 5
print("Programa finalizado!")
