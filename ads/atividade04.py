nome=input("Digite o nome do aluno: ")
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
soma=n1+n2
if soma>=60:
    soma=n1+n2
    print("Aprovado")
else:
    print("Reprovado")
print("Nome: ",nome, "\nNota",soma)