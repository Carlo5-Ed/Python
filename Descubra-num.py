import random
num=int(input("Advinhe o número: "))
num2 = random.randint(0, 5)
print(num2)
if num==num2:
    print("Você venceu!!")
else:
    print("Você perdeu!!")
