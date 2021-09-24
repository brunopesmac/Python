from datetime import date
atual = date.today().year
idade = int(input("Digite a sua idade: "))
seculo = atual
while seculo % 100 != 0:
    seculo += 1
idadef = seculo-atual+idade
print("Na proxima virada de seculo no ano de {} você terá {} anos".format(seculo,idadef))

