n1 = float(input("Informe a primeira medida:"))
n2 = float(input("Informe a segunda medida:"))
n3 = float(input("Informe a terceira medida:"))

if (n1 + n2 < n3) or (n1 + n3 < n2) or (n2 + n3 < n1):
    print("Nao é um triângulo")
elif (n1 == n2) and (n1 == n3) :
    print("Equilátero")
elif (n1==n2) or (n1==n3) or (n2==n3):
     print("Isósceles")
else:
    print("Escaleno")