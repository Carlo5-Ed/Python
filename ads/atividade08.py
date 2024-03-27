import math
x1=float(input("Digite a coordenada x do ponto 1: "))
y1=float(input("Digite a coordernada y do ponto 1: "))
x2=float(input("Digite a coordenada x do pontto 2: "))
y2=float(input("Digite a coordenada y do ponto 2: "))

ponto1=(x1, y1)
ponto2=(x2, y2)
distancia=(x2 - x1)**2 + (y2 - y1)**2

print("A distância entre os pontos é: ", distancia)
