num = int(input("Digite um numero: "))
fatorial = 1
while num != 1:
    fatorial = fatorial*(num)
    num -= 1
print("O fatorial é {}!".format(fatorial))