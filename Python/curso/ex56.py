media = 0
nomeM = ""
maior = 0
cont = 0
for c in range(0,4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite M para masculino e F para feminino: "))
    media += idade
    if sexo =="m" or "M":
        if idade > maior:
            nomeM = nome
            maior = idade
    if sexo == "f" or "F":
        if idade < 20:
            cont += 1
media= media/c
print("A media de idade é {:.0f} anos, o homem mais velho possui {} anos e se chama {} e {} mulheres possuem menos de 20 anos!".format(media,maior,nomeM,cont))