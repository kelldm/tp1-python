#7. Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

def calculaIMC(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    imc = calculaIMC(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é {imc:.2f}, classificado como '{classificacao}'.")

if __name__ == "__main__":
    main()
