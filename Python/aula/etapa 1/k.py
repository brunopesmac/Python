salario = float(input("Digite o salario: "))
menu = 1
com = 0.0
while menu > 0:
    menu = int(input("[1]valor do  produto vendido\n[0]finalizar mês\n"))
    if menu == 1:
        com += float(input("Digite o valor da venda: "))
    if menu > 1:
        print ("Comando inexistente!")
valorF = com*0.04+salario
print("Com o salário de R${:.2f} e o valor de venda final de {:.2f} com 4% de comissão o salario final ficou {:.2f}".format(salario,com,valorF))
