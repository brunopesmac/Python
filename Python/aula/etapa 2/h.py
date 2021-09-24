#h
maior = 0
for c in range(1,4):
    base = float(input("Digite a base do {} triangulo: ".format(c)))
    altura = float(input("Digite a altura do {} triangulo: ".format(c)))
    area = (base*altura)/2
    if area > maior:
        maior = area
print ("A maior area é {} cm²".format(maior))
