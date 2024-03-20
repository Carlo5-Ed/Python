veloci=int(input("Digite a velocidade km: "))
km=7.00
if veloci > 80:
    print("Você foi multado!")
if veloci > 80:
    valor= (veloci-80)*7
    print("O valor da multa é {:.2f}".format(valor))
else:
    print("De acordo com a via!")