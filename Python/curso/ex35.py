a = float (input ("Aresta 1: "))
b = float (input ("Aresta 2: "))
c = float (input ("Aresta 3: "))
if a < b+c and b < a+c and c < a+b:
    print("É possível a criação de um triângulo!")
else:
    print("Não é possível a criação de um triângulo!")
