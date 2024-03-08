
import csv
import os

# Função para ler dados de um arquivo CSV
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        return [linha for linha in leitor_csv]

# Função para escrever dados em um arquivo CSV
def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados:
            escritor_csv.writerow(linha)

# Função para remover um item de uma lista que vem de um arquivo CSV
def remover_item_lista_csv(nome_arquivo, item_para_remover):
    dados = ler_csv(nome_arquivo)

    # Encontrar o índice da linha a ser removida
    indices_para_remover = [i for i, linha in enumerate(dados) if linha == item_para_remover]

    # Remover as linhas correspondentes
    dados_atualizados = [linha for i, linha in enumerate(dados) if i not in indices_para_remover]

    # Substituir o arquivo original pelo atualizado
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados_atualizados:
            escritor_csv.writerow(linha)

# Exemplo de uso
arquivo_saida = 'exemplo.csv'

# Capturar dados do usuário
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cidade = input("Digite a cidade: ")

# Adicionar alguns dados ao arquivo CSV para teste
dados_para_adicionar = [
    [nome, idade, cidade]
]

escrever_csv(arquivo_saida, dados_para_adicionar)

# Ler dados do arquivo CSV antes da remoção
print("Dados no arquivo antes da remoção:")
print(ler_csv(arquivo_saida))

# Definir o item a ser removido
item_remover = ['Maria', '30', 'Rio de Janeiro']

# Remover o item do arquivo CSV
remover_item_lista_csv(arquivo_saida, item_remover)

# Ler dados do arquivo CSV após a remoção
print("\nDados no arquivo após a remoção:")
print(ler_csv(arquivo_saida))
