valor = float(input("Qual o valor da casa? R$"))
salario = float(input("Quanto você ganha? R$"))
anos = int(input("Em quantos anos ira pagar? "))
mensal = (valor/anos)/12
print ("Para pegar uma casa com o valor de R${:.2f} em um intervalo de {} anos, será feito no valor de R${:.2f} mensais".format(valor,anos,mensal))
if mensal > salario*0.3:
    print ("Emprestimo negado!")
else:
    print ("Emprestimo aprovado!")