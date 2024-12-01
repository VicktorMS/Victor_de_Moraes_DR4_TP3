import pandas as pd
import re
from src.questions.manipulao_de_dados_3 import salvar_para_excel
from src.utils.constants import DATA_PATH

# 4 - Limpeza de Dados
########################
def carregar_dados_excel(nome_arquivo):
    """
    Carrega um arquivo Excel em um DataFrame do Pandas.
    
    :param nome_arquivo: Nome do arquivo Excel a ser carregado.
    :return: DataFrame com os dados ou None se ocorrer um erro.
    """
    try:
        df = pd.read_excel(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso.")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except ValueError as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return None

def validar_email(email):
    """
    Valida se o e-mail fornecido é válido utilizando expressão regular.
    
    :param email: String contendo o e-mail a ser validado.
    :return: True se o e-mail for válido, False caso contrário.
    """
    if pd.isna(email):
        return False
    # Expressão regular básica para validação de e-mails
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def remover_emails_invalidos(df):
    """
    Remove os usuários que não possuem e-mail válido.
    
    :param df: DataFrame com os dados dos usuários.
    :return: DataFrame filtrado sem usuários com e-mails inválidos.
    """
    if df is not None:
        try:
            # Aplica a validação de e-mail em cada linha
            valid_emails = df['email'].apply(validar_email)
            df_filtrado = df[valid_emails].reset_index(drop=True)
            print(f"Removidos {len(df) - len(df_filtrado)} usuários com e-mails inválidos.")
            return df_filtrado
        except KeyError:
            print("Erro: A coluna 'email' não existe no DataFrame.")
            return df
        except Exception as e:
            print(f"Erro ao remover e-mails inválidos: {e}")
            return df
    else:
        print("Erro: DataFrame de entrada é inválido.")
        return None

def preencher_valores_ausentes(df):
    """
    Preenche valores ausentes nas colunas 'cidade' e 'estado'.
    
    :param df: DataFrame com os dados dos usuários.
    :return: DataFrame com valores preenchidos.
    """
    if df is not None:
        try:
            fill_values = {}
            if 'cidade' in df.columns:
                num_cidades_ausentes = df['cidade'].isna().sum()
                fill_values['cidade'] = 'Não Informada'
                print(f"Preenchidos {num_cidades_ausentes} valores ausentes na coluna 'cidade' com 'Não Informada'.")
            else:
                print("Aviso: A coluna 'cidade' não existe no DataFrame.")
            
            if 'estado' in df.columns:
                num_estados_ausentes = df['estado'].isna().sum()
                fill_values['estado'] = 'ZZ'
                print(f"Preenchidos {num_estados_ausentes} valores ausentes na coluna 'estado' com 'ZZ'.")
            else:
                print("Aviso: A coluna 'estado' não existe no DataFrame.")
            
            # Aplica o preenchimento
            if fill_values:
                df = df.fillna(fill_values)
            
            return df
        except Exception as e:
            print(f"Erro ao preencher valores ausentes: {e}")
            return df
    else:
        print("Erro: DataFrame de entrada é inválido.")
        return None
        
        
def main():
    print("Esta é a questão: Limpeza de Dados")
    
    arquivo_entrada = DATA_PATH + "INFwebNET_30mais.xlsx"
    arquivo_saida = DATA_PATH + "INFwebNET_30mais_limpo.xlsx"
    
    dados = carregar_dados_excel(arquivo_entrada)
    
    dados_sem_emails_invalidos = remover_emails_invalidos(dados)
    
    dados_limpos = preencher_valores_ausentes(dados_sem_emails_invalidos)
    
    salvar_para_excel(dados_limpos, arquivo_saida)