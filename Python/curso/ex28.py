from random import randint
computer= randint(0,5)
pessoa =int(input("Digite um numero entre 0 e 5: "))
print ("O computador pensou no {} e você no {}".format(computer,pessoa))
if pessoa==computer:
    print("Voce acertou")
else:
    print("Voce errou")
