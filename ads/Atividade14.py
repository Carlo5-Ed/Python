lado1=int(input("Digite o lado do triangulo: "))
lado2=int(input("Digite o lado do triangulo: "))
lado3=int(input("Digite o lado do triangulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("As retas podem formar um triangulo ", end='')
    if lado1==lado2==lado3:
     print("Equilátero")
    elif lado1 != lado2 != lado3 != lado1:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Erro")