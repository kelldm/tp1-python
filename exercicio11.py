#11. Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random

def lancarDados(numero):
    resultados = []
    for _ in range(numero):
        resultado = random.randint(1, 6) 
        resultados.append(resultado)
    return resultados

def main():
    numero = int(input("Quantos dados você deseja jogar? "))
    resultados = lancarDados(numero)

    print("Resultados dos lançamentos:", resultados)

if __name__ == "__main__":
    main()
