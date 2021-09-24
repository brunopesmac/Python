p1 = float(input("Digite a P1: "))
p2 = float(input("Digite a P2: "))
t = float(input("Digite o T: "))
media = (p1+p2+t)/3
if media >= 70:
    print("Com a média de {:.2f} o aluno está aprovado!".format(media))
else:
    print("Com a média de {:.2f} o aluno está reprovado!".format(media))
