d=int(input("Quantos dias alugados? "))
km=float(input("Quantos km rodados? "))
total=(d*60)+(km*0.15)
print("Total a pagar é de R${:.2f}".format(total))