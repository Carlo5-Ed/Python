a=input("Digite algo: ")
print("O tipo primitivo desse valor é", type(a))
print("Possui espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Possui maiúsculas? ", a.isupper())
print("Possui minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())