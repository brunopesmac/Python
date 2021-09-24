peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/(altura**2)
if IMC < 18.5:
    resultado ="ABAIXO DO PESO"
elif 18.5 <= IMC < 25:
    resultado = "PESO IDEAL"
elif 25 <= IMC < 30:
    resultado = "SOBREPESO"
elif 30 <= IMC < 40:
    resultado = "OBESIDADE"
else:
    resultado = "OBESIDADE MÓRBIDA"
print ("Seu IMC é {:.1f}, portanto você esta {}!".format(IMC,resultado))