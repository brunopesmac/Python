from random import randint
computer= randint(0,10)
cont = 0
pessoa =int(input("Digite um numero entre 0 e 10: "))
while pessoa != computer:
    pessoa =int(input("Digite um numero entre 0 e 10 novamente: "))
    cont += 1
print ("O computador pensou no {} e você precisou de {} tentativas!".format(computer,cont))