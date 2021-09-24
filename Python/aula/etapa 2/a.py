a1 = float (input("Digite a nota da avaliação 1: "))
a2 = float (input("Digite a nota da avaliação 2: "))
media = (a1+a2)/2
if media < 6:
 print("Sua média foi {:.1f} portanto REPROVADO!".format(media))
else:
    print("Sua média foi {:.1f} portanto APROVADO!".format(media))
