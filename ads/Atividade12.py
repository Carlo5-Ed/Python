num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
num3=int(input("Digite o terceiro número: "))
i=num1,num2,num3
maior=num1
if num2>num1 and num2>num3:
    maior=num2
elif num3>num1 and num3>num2:
    maior=num3
print("O maior é ", maior)

menor=num1
if num2<num1 and num2<num3:
    menor=num2
elif num3<num1 and num3<num2:
    menor=num3
print("O menor é ", menor)

maior2=num1
if num2+num1-maior-menor and num2+num3-maior-menor:
    maior2=num2
elif num3+num1-maior-menor and num3+num2-maior-menor:
    maior2=num3
print("O segundo maior é ", maior2)
if num1==num2 or num1==num3 or num2==num3:
    print("Erro, os números não são diferentes.")