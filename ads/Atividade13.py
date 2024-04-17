num=int(input("0: Verde\n1: Amarelo\n2: Vermelho\n"))
if num==0:
    print("\033[32mpasse schumi!")
elif num==1:
    print("\33[33macelera rubinho!")
elif num==2:
    print("\33[31mfreia berenice")
else:
    print("Opção inválida")