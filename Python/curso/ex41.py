from datetime import date
ano = int (input("Qual o ano de nascimento: "))
anoA = date.today().year
idade = anoA-ano
if idade <=9:
    categoria = "MIRIM"
elif 9 < idade <=14:
    categoria = "INFANTIL"
elif 14 < idade <= 19:
    categoria = "JÚNIOR"
elif 19 < idade <= 25:
    categoria = "SENIOR"
else:
    categoria = "MASTER"
print("O Atleta tem {} ano(s) portanto está na categoria {}!".format(idade,categoria))