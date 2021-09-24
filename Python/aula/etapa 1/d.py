salario = float(input("Digite o salario: "))
grat = salario*0.05
imp = salario*0.07
fim = salario+grat-imp
print("O salario de R${:.2f} recebeu R${:.2f} de gratificação e R${:.2f} de imposto ficando R${:.2f}".format(salario,grat, imp,fim))
