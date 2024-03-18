#6. Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
import random

def main():
    numSecreto = random.randint(1, 100)

    while True:
        numEscolhido = int(input("Adivinhe o número secreto (entre 1 e 100): "))

        # Verificar se o palpite está correto, muito alto ou muito baixo
        if numEscolhido == numSecreto:
            print("Parabéns! Você acertou!!!!!! GOOD JOB")
            break
        elif numEscolhido < numSecreto:
            print("Ihhhh, ta frio....")
        else:
            print("TA QUENTE EIN......")

if __name__ == "__main__":
    main()
