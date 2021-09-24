frase = str(input("Digite uma frase: "))
res = bool(False)
frase =frase.replace(" ","")
fim = len(frase)
for c in range (0,len(frase)):
    if frase[c] == frase[fim-1]:
        if fim != 0:
            fim = fim-1
        res = True
    else:
        res = False
        break
if res == True:
    print ("A frase é um Palindromo")
else:
    print ("A frase não é um Palindromo")