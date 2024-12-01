# 2 - Explorando Dados
########################
import csv

def carregar_dados_csv(nome_arquivo):
    """
    Carrega um arquivo CSV e retorna os dados como uma lista de dicionários.

    :param nome_arquivo: Nome do arquivo CSV a ser carregado.
    :return: Lista de dicionários com os dados ou None se ocorrer um erro.
    """
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = list(leitor)
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except csv.Error as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return None

def exibir_primeiras_linhas(dados, numero_linhas=10):
    """
    Exibe as primeiras linhas dos dados carregados.

    :param dados: Lista de dicionários com os dados.
    :param numero_linhas: Número de linhas a serem exibidas.
    """
    if dados:
        print(f"\nAs {numero_linhas} primeiras linhas do arquivo:")
        for i, linha in enumerate(dados[:numero_linhas], start=1):
            print(f"Linha {i}: {linha}")
    else:
        print("Não há dados para exibir as linhas.")

def listar_colunas(dados):
    """
    Lista todas as colunas presentes nos dados carregados.

    :param dados: Lista de dicionários com os dados.
    """
    if dados:
        colunas = dados[0].keys()
        print("\nColunas presentes no arquivo:")
        for coluna in colunas:
            if type(coluna) == str:
                coluna = coluna.split(';')
                for col in coluna:
                    print(f"- {col}")
    else:
        print("Não há dados para listar as colunas.")
        
def main():
    print("Esta é a questão: Explorando Dados")
    arquivo = "src/data/dados_usuarios.csv"
    dados = carregar_dados_csv(arquivo)
    exibir_primeiras_linhas(dados, 10)
    listar_colunas(dados)