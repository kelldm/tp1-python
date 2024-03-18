#9. Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.

def calcDesconto(compra):
    if compra > 200:
        desconto = 0.15
    elif compra > 100:
        desconto = 0.10
    else:
        desconto = 0
    
    return compra * desconto

def main():
    compra = float(input("Digite o valor da compra: R$"))
    desconto = calcDesconto(compra)

    print(f"Desconto aplicado: R${desconto:.2f}")

if __name__ == "__main__":
    main()
