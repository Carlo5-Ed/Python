distancia=float(input("Digite a distancia da viagem em km: "))
if distancia <= 200:
    preco= distancia*0.50
    print("Valor a pagar R$ ", preco)
else:
    preco= distancia*0.45
    print("Valor a pagar R${:.2f}".format(preco))