velocidade = float (input ("Digite a velocidade do carro: "))
if velocidade>80:
    resto =velocidade-80
    multa = resto*7
    print("Sua multa é de R${:.2f}! pois você ficou {}Km acima do permitido".format(multa,resto))
else:
    print("Você não foi multado!")