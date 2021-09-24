#f
a  = float (input("Digite um numero: "))
b  = float (input("Digite um numero: "))
c  = float (input("Digite um numero: "))

if a > b > c:
    print ("{:.2f} {:.2f} {:.2f}".format(c,b,a))
if a > c > b:
    print ("{:.2f} {:.2f} {:.2f}".format(b,c,a))
if b > a > c:
    print ("{:.2f} {:.2f} {:.2f}".format(c,a,b))
if b > c > a:
    print ("{:.2f} {:.2f} {:.2f}".format(a,c,b))
if c > a > b:
    print ("{:.2f} {:.2f} {:.2f}".format(b,a,c))
if c > b > a:
    print ("{:.2f} {:.2f} {:.2f}".format(a,b,c))
   