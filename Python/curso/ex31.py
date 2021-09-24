distancia = float (input("Qual a distancia da viajem em km? "))
if distancia<=200:
    valor = distancia*0.5
    print ("O valor da viajem será R${:.2f}!".format(valor))
else:
    valor = distancia*0.45
    print ("O valor da viajem será R${:2.f}!".format(valor))