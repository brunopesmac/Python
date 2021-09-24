from datetime import date
anoNasc = int(input("Digite o ano que você nasceu: "))
anoAtual = date.today().year
idade = anoAtual-anoNasc
if idade == 18:
    print("É a hora exata de se alistar!")
elif idade > 18:
    print("Já passou {} ano(s) do seu alistamento! Seu alistamento foi no ano de {}!".format(idade-18,anoAtual-(idade-18)))
elif idade < 18:
    print("Falta {} ano(s) para seu alistamento! Seu alistamento será no ano de {}!".format(18-idade, anoAtual+(18-idade)))