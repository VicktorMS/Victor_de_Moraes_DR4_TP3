# 3 - Manipulação de Dados
########################

import pandas as pd

def carregar_dados_csv(nome_arquivo, separador=';'):
    """
    Carrega um arquivo CSV em um DataFrame do Pandas.
    
    :param nome_arquivo: Nome do arquivo CSV a ser carregado.
    :param separador: Delimitador usado no arquivo CSV.
    :return: DataFrame com os dados ou None se ocorrer um erro.
    """
    try:
        df = pd.read_csv(nome_arquivo, sep=separador)
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso.")
        return df
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
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return None

def filtrar_por_idade(df, idade_minima=30):
    """
    Filtra o DataFrame para incluir apenas usuários com idade maior que a idade mínima.
    
    :param df: DataFrame com os dados dos usuários.
    :param idade_minima: Idade mínima para filtrar os usuários.
    :return: DataFrame filtrado ou None se o DataFrame de entrada for inválido.
    """
    if df is not None:
        try:
            df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
            df_filtrado = df[df['idade'] > idade_minima]
            print(f"Filtrado usuários com idade maior que {idade_minima}. Total: {len(df_filtrado)}")
            return df_filtrado
        except KeyError:
            print("Erro: A coluna 'idade' não existe no DataFrame.")
            return None
        except Exception as e:
            print(f"Erro ao filtrar por idade: {e}")
            return None
    else:
        print("Erro: DataFrame de entrada é inválido.")
        return None

def salvar_para_excel(df, nome_arquivo):
    """
    Salva o DataFrame fornecido em um arquivo Excel.
    
    :param df: DataFrame a ser salvo.
    :param nome_arquivo: Nome do arquivo Excel de saída.
    """
    if df is not None and not df.empty:
        try:
            df.to_excel(nome_arquivo, index=False)
            print(f"Dados filtrados salvos com sucesso em '{nome_arquivo}'.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo Excel: {e}")
    else:
        print("Erro: Não há dados para salvar no arquivo Excel.")
        
        
def main():
    print("Esta é a questão: Manipulação de Dados")
    arquivo_entrada = "src/data/dados_usuarios.csv"
    arquivo_saida = "src/data/INFwebNET_30mais.xlsx"
    idade_minima = 30
    
    dados = carregar_dados_csv(arquivo_entrada)
    
    dados_filtrados = filtrar_por_idade(dados, idade_minima)
    
    salvar_para_excel(dados_filtrados, arquivo_saida)