#i
a = float (input ("Aresta 1: "))
b = float (input ("Aresta 2: "))
c = float (input ("Aresta 3: "))
if a < b+c and b < a+c and c < a+b:
    print("É possível a criação de um triângulo!")
    if a == b and b ==c:
        print("O triângulo é equilátero! Todos os lados são iguais!")
    elif a == b and c !=b or b == c and c != a or a == c and c != b:
        print("O triângulo é isósceles! Possui 2 lados iguais e um diferente!")
    elif a != b and a != c and b != c:
        print("O triângulo é escaleno! Todos os lados são diferentes!")
else:
    print("Não é possível a criação de um triângulo!")
