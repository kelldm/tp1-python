#10. Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.

import random

def criarHistoria(personagens, acoes, locais):
    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"Um dia, {personagem} decidiu {acao} {local}."
    return historia

def main():
    personagens = ["um mago", "um cowboy", "uma bruxa", "um dentista", "um anão"]
    acoes = ["explorar", "conquistar", "procurar", "destruir", "cair em"]
    locais = ["uma floresta da jamaica", "um hobbit simpático", "uma galáxia", "uma cidade inteira", "uma creche"]

    historia = criarHistoria(personagens, acoes, locais)
    print(historia)

if __name__ == "__main__":
    main()
