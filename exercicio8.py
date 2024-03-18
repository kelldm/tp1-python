#8. Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

def maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

def main():
    # Solicitar a idade do usuário
    idade = int(input("Digite sua idade: "))
    resultado = maioridade(idade)
    print(resultado)

if __name__ == "__main__":
    main()
