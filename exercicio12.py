#12. Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

def classificacao(lista):
    palavrasCurtas = []
    palavrasLongas = []
    for palavra in lista:
        if len(palavra) < 5:
            palavrasCurtas.append(palavra)
        else:
            palavrasLongas.append(palavra)
    return palavrasCurtas, palavrasLongas

def main():
    lista = input("Digite uma lista de palavras separadas por espaço: ").split()
    palavrasCurtas, palavrasLongas = classificacao(lista)

    print("Palavras curtas:", palavrasCurtas)
    print("Palavras longas:", palavrasLongas)

if __name__ == "__main__":
    main()
