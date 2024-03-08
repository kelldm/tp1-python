#2. Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

#função para 'minutos para horas e minutos'
def minParaHorasEMin(totalMinutos):
    horas = totalMinutos // 60
    minutos = totalMinutos % 60
    return horas, minutos

#função para 'horas e minutos para minutos'
def horasEMinParaMin(horas, minutos):
    totalMinutos = horas * 60 + minutos
    return totalMinutos

#função que conversa com o usuário
def main():
    #minutos para horas e minutos
    minutos = int(input("Digite o número total de minutos: "))
    horas, minutosRestantes = minParaHorasEMin(minutos)
    print(f"{minutos} minutos são {horas} horas e {minutosRestantes} minutos.")

    #horas e minutos para minutos
    horas = int(input("Digite o número de horas: "))
    minutos = int(input("Digite o número de minutos: "))
    totalMinutos = horasEMinParaMin(horas, minutos)
    print(f"{horas} horas e {minutos} minutos são {totalMinutos} minutos.")

main()


