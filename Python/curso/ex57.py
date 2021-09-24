sexo = str(input("Digite seu sexo [M/F]: ")).upper()
while sexo != "F" and sexo != "M":
    sexo = str(input("Digite seu sexo [M/F]: ")).upper()
    if sexo != "F" and sexo != "M":
        print ("Valor errado digite novamente!")
print("Valor correto")