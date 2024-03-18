#5. Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, combine-os para formar uma saudação personalizada.

def main():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    saudacao = f"Olá, {nome} {sobrenome}! Seja bem-vindo!"

    print(saudacao)

if __name__ == "__main__":
    main()
