# 5 - Combinação de Excel Linhas
########################

import pandas as pd

from utils.constants import DATA_PATH

def carregar_planilhas_excel(nome_arquivo, planilhas):
    """
    Carrega as planilhas especificadas de um arquivo Excel.

    :param nome_arquivo: Nome do arquivo Excel a ser carregado.
    :param planilhas: Lista de nomes das planilhas a serem carregadas.
    :return: Dicionário com DataFrames das planilhas ou None se ocorrer um erro.
    """
    try:
        excel = pd.ExcelFile(nome_arquivo)
        dados_planilhas = {}
        
        for planilha in planilhas:
            try:
                # Carrega cada planilha
                df = pd.read_excel(excel, sheet_name=planilha)
                dados_planilhas[planilha] = df
                print(f"Planilha '{planilha}' carregada com sucesso. Número de linhas: {len(df)}")
            except ValueError as e:
                print(f"Erro: A planilha '{planilha}' não foi encontrada no arquivo '{nome_arquivo}'.")
                return None
        
        return dados_planilhas

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{nome_arquivo}' está vazio.")
        return None
    except pd.errors.ParserError as e:
        print(f"Erro de parsing ao carregar o arquivo '{nome_arquivo}': {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo '{nome_arquivo}': {e}")
        return None

def exibir_numero_linhas(df, nome_planilha):
    """
    Exibe o número total de linhas de um DataFrame.

    :param df: DataFrame cuja contagem de linhas será exibida.
    :param nome_planilha: Nome da planilha para referência na mensagem.
    """
    if df is not None:
        num_linhas = len(df)
        print(f"A planilha '{nome_planilha}' possui {num_linhas} linhas.")
    else:
        print(f"DataFrame para a planilha '{nome_planilha}' está vazio ou não foi carregado.")


def main():
    print("Esta é a questão: Combinação de Excel Linhas")
    arquivo_excel = DATA_PATH + "INFwebNET_Historico.xlsx"
    planilhas = ["INFwebNET2022", "INFwebNET2023"]
    
    dados = carregar_planilhas_excel(arquivo_excel, planilhas)
    
    if dados is not None:
        for nome_planilha, df in dados.items():
            exibir_numero_linhas(df, nome_planilha)
    else:
        print("Não foi possível carregar as planilhas especificadas.")