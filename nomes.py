nome=str(input("Qual seu nome? "))
if nome == 'Carlos':
    print("Que nome bonito {}!".format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Enzo' or nome == 'Ana':
    print("Seu nome é bem escolhido no Brasil")
else:
    print("Que nome comum {}!".format(nome))
print("Tenha um bom dia, {}!".format(nome))