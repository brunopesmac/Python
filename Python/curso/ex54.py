from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (0,7):
    ano = int(input("Digite o ano de nascimento: "))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print("{} pessoas atingiram a maioridade e {} ainda não atingiram!".format(maior,menor))