soma=0
cont=0
for a in range(0, 6):
    n=int(input("Digite um valor: "))
    if n % 2 == 0:
        soma+=n
        cont+=1
print("Soma: ", soma)