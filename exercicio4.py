#4. Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

#Operações
def adicao(num1, num2):
    return round(num1 + num2)

def subtracao(num1, num2):
    return round(num1 - num2)

def multiplicacao(num1, num2):
    return round(num1 * num2)

def divisao(num1, num2):
    if num2 != 0:
        return round(num1 / num2)
    else:
        return "Não é possível dividir por zero."

#Menu do usuário
def main():
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    #Inputs para o usuário escolher a operação e os números em seguida
    escolha = input("ESCOLHA: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    #dependendo da escolha do usuário, chama operação escolhida, com seu resultado.
    if escolha == '1':
        print("Resultado:", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
    else:
        print("Escolha inválida. Por favor, escolha uma operação válida.")

main()

