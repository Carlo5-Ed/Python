operando1=int(input("Digite o primeiro operando: "))
operador=input("Digite o operador (+, -, *, /): ")
operando2=int(input("Digite o segundo operando: "))
if operador=='+':
    resultado=operando1+operando2
elif operador=='-':
    resultado=operando1-operando2
elif operador=='*':
      resultado=operando1*operando2
elif operador=='/':
    resultado=operando1/operando2
else:
    resultado='Operação incorreta'
print(str(operando1) + ' ' + str(operador) + ' ' + str(operando2) + ' = ' + str(resultado))