salario = float (input ( "Digite o salario: "))
if salario > 1250:
    aumento = (salario/100)*10
    salario += aumento
else:
    aumento = (salario/100)*15
    salario += aumento
print ("O valor do aumento foi de R${:.2f} contabilizando um salario de R${:.2f}".format(aumento,salario))