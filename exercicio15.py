#15. Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

def historia():
    print("Seja Bem-vindo à DUNGEON! Escolha com sabedoria...")

    escolha1 = input("Você deseja ir para a esquerda ou a direita? (esquerda/direita): ")
    if escolha1.lower() == "esquerda":
        print("Você escolheu a porta à esquerda.")
        escolha2 = input("Você vê uma chave e uma faca. Qual você pega? (chave/faca): ")
        if escolha2.lower() == "chave":
            print("Você pegou a chave e avançou para a próxima sala.")
            print("Parabéns! Você encontrou a saída! Quem escolhe a chave abre portas, quem escolha a violencia recebe suas consequências....")
        elif escolha2.lower() == "faca":
            print("Você pegou a faca e avançou para a próxima sala.")
            print("Um monstro apareceu, você o atacou mas sua pele era impenetrável. Ele te esmagou. Quem escolhe a chave abre portas, quem escolha a violencia recebe suas consequências.... Game over!")
        else:
            print("Opção inválida. Game over!")
    elif escolha1.lower() == "direita":
        print("Você escolheu a porta à direita.")
        print("Você caiu em um precipício. Game over!")
    else:
        print("Opção inválida.")

def main():
    historia()

if __name__ == "__main__":
    main()
