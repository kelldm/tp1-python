#1. Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

#Inputs usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#Calcula soma
soma = round(num1 + num2)
print("Soma:", soma)

#Calcula subtração
subtracao = round(num1 - num2)
print("Subtração:", subtracao)

#Calcula multiplicação
multiplicacao = round(num1 * num2)
print("Multiplicação:", multiplicacao)

#Calcula divisão
if num2 != 0:
    divisao = round(num1 / num2)
    print("Divisão:", divisao)

    divisao_inteira = num1 // num2
    print("Divisão inteira:", divisao_inteira)

#Caso tentem dividir por 0
else:
    print("Não é possível dividir por zero.")
