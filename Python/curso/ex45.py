from random import randint
cpu = randint(1,3)
player = int (input("JO KEN PO\n1 pedra\n2 papel\n3 tesoura\n"))
if cpu == player:
    print ("EMPATE!")
elif cpu == 1 and player == 2 or cpu == 2 and player == 3 or cpu == 3 and player == 1:
    print ("VOCÊ VENCEU!")
elif player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 3 and cpu == 1:
    print ("VOCÊ PERDEU!")