total =0
num = int (input ("Digite um numero: "))
for c in range( 1 , num+1):
    if num % c == 0:
        total+=1
if total == 2:
    print("O numero é primo")
else:
    print("O numero não é primo")