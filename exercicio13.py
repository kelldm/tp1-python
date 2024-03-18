#13. Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

def main():
    texto = input("Digite uma palavra ou frase: ")

    if palindromo(texto):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

if __name__ == "__main__":
    main()
