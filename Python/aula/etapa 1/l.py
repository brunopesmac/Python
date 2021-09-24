from datetime import date
atual = date.today().year
ano = int(input("Digite a seu ano de nascimento: "))
idade = atual - ano
print ("Nascido em {} no ano de {} possui {} anos".format(ano,atual,idade))
