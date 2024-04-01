sala=float(input("Digite o seu salário:R$ "))
if sala <= 1250:
    aument=sala+(sala*15/100)
else:
    aument=sala+(sala*10/100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(sala, aument))