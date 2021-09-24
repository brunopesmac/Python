altura = float (input("Digite sua altura: "))
sexo = str(input("Digite seu sexo [F/M] :")).upper()

if sexo == "M":
    print ("Seu peso ideal é {:.2f} kg".format( 72.7*altura-58))
elif sexo == "F":
    print ("Seu peso ideal é {:.2f} kg".format(62.1*altura - 44.7))
else:
    print("Dados invalidos!")
