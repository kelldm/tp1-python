#14. Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.


def votar(opcoes, votos):
    opcao = int(input("Escolha uma opção (1, 2 ou 3): "))
    if opcao in opcoes:
        votos[opcao] += 1
        print("Voto registrado com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")

def resultados(votos):
    print("\nResultados dos votos:")
    for opcao, voto in votos.items():
        print(f"Opção {opcao}: {voto} votos")

def main():
    opcoes = [1, 2, 3]
    votos = {1: 0, 2: 0, 3: 0}

    totalVotos = int(input("Quantos votos serão registrados? "))

    for _ in range(totalVotos):
        votar(opcoes, votos)

    resultados(votos)

if __name__ == "__main__":
    main()
