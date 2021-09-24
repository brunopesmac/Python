a1 = float (input("Digite a nota da avaliação 1: "))
a2 = float (input("Digite a nota da avaliação 2: "))
media = (a1+a2)/2
if media < 5:
 print("Sua média foi {:.1f} portanto REPROVADO!".format(media))
elif 7 > media >= 5:
    print("Sua média foi {:.1f} portanto RECUPERAÇÃO!".format(media))
elif media >= 7:
    print("Sua média foi {:.1f} portanto APROVADO!".format(media))
