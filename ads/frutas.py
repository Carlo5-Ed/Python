print("Vou adivinhar a fruta que você pensou.")
print("Pense em morango, uva, acerola, cereja, coco , melão, maracujá e limão.")
r1=input("Digite v se a fruta é avermelhada ou roxa: ")
if r1=="V" or r1=="v":
    r2=input("Digite v se a fruta nasce em ramas: ")
    r3=input("Digite v se a fruta é cultivada em lugares quentes: ")
    if r2=="V" or r2=="v":
        if r3=="V" or r3=="v":
            print("Você pensou em Morango!")
        else:
            print("Você pensou em Uva!")
    else:
        if r3=="v" or r3=="v":
            print("Acerola")
        else:
            print("Cereja")
else:
    r4=input("Digite v se a fruta nasce em ramas: ")
    r5=input("Digite v se a fruta é doce: ")
    if r4=="v" or r4=="v":
        if r5=="v" or r5=="v":
            print("Você pensou em Melão!")
        else:
            print("Você pensou em Maracujá!")
    else:
        if r5=="v" or r5=="v":
            print("Você pensou em Coco!")
        else:
            print("Você pensou em Limão!")