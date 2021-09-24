valor = float(input("Digite o valor do produto: R$"))
metodo = int(input("METODO DE PAGAMENTO\n1 para dinheiro: desconto de 10%\n2 a vista no cartão: desconto de %5\n3 2x no cartão\n4 3 ou mais no cartão: juros de 20%\n"))
if metodo == 1:
    print ( "O valor final do produto com desconto de 10% é R${:.2f}! PAGAMENTO COM DINHEIRO!".format(valor*0.9))
elif metodo == 2:
    print ( "O valor final do produto com desconto de 5% é R${:.2f}! PAGAMENTO A VISTA NO CARTÃO!".format(valor*0.95))
elif metodo == 3:
    print ( "O valor final do produto é R${:.2f}! PAGAMENTO 2x NO CARTÃO!".format(valor))
elif metodo == 4:
    print ( "O valor final do produto com juros de 20% é R${:.2f}! PAGAMENTO 3x OU MAIS NO CARTÃO!".format(valor*1.2))
else:
    print ("METODO INEXISTENTE")