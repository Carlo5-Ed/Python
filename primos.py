
n=int(input("Digite um número: "))
total=0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        total+=1
    else:
        print('\33[31m', end="")
    print("{} ".format(c), end='')
if total == 2:
    print("\n \033[32mO número {} é primo!".format(n))
else:
    print("\n \033[31mO número {} não é primo!".format(n))