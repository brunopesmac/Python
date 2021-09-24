num = int(input("Digite um numero :"))
escolha = int (input("Digite a converção:\n1 para binário\n2 para octal\n3 para hexadecimal\n"))
if escolha == 1:
    print("O numero em binário é: "+bin(num)[2:])
elif escolha == 2:
    print("O numero em octal é: "+oct(num)[2:])
elif escolha == 3:
    print("O numero em hexadecimal é: "+hex(num)[2:])
else:
    print("O valor digitado não é uma das converções disponíveis!!")