#3. Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

def main():
    print("Vamos combinar nomes?")
    nome1 = input("Digite o primeiro nome: ")
    nome2 = input("Digite o segundo: ")

    novoNome = nome1[:len(nome1)//2] + nome2[len(nome2)//2:]

    print("Novo nome combinado:", novoNome)

main()
