# 9 - Consolidando Dados
########################
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from questions.carregando_em_sql_7 import conectar_banco_dados
from questions.combinao_de_excel_duplicatas_6 import remover_duplicatas
from questions.consulta_sql_8 import consultar_usuarios_idade
from utils.constants import DB_PATH


def criar_tabela_consolidado(engine, df_consolidado, nome_tabela='Consolidado', if_exists='replace'):
    """
    Cria a tabela 'Consolidado' no banco de dados e insere os dados consolidados nela.
    
    :param engine: Engine de conexão com o banco de dados.
    :param df_consolidado: DataFrame consolidado a ser inserido na tabela.
    :param nome_tabela: Nome da tabela SQL a ser criada/inserida.
    :param if_exists: O que fazer se a tabela já existir ('fail', 'replace', 'append').
    """
    if df_consolidado is not None and engine is not None:
        try:
            df_consolidado.to_sql(nome_tabela, con=engine, if_exists=if_exists, index=False)
            print(f"Dados inseridos com sucesso na tabela '{nome_tabela}'.")
        except ValueError as e:
            print(f"Erro ao inserir dados na tabela '{nome_tabela}': {e}")
        except SQLAlchemyError as e:
            print(f"Erro de SQLAlchemy ao inserir dados na tabela '{nome_tabela}': {e}")
        except Exception as e:
            print(f"Erro inesperado ao inserir dados na tabela '{nome_tabela}': {e}")
    else:
        print("Erro: DataFrame consolidado ou Engine de conexão é inválido.")

def carregar_dados_existentes(engine, tabelas=['Usuarios_Historicos']):
    """
    Carrega os dados das tabelas existentes no banco de dados.
    
    :param engine: Engine de conexão com o banco de dados.
    :param tabelas: Lista de nomes das tabelas a serem carregadas.
    :return: Lista de DataFrames carregados ou None se ocorrer um erro.
    """
    dataframes = []
    if engine is not None:
        for tabela in tabelas:
            try:
                query = text(f"SELECT * FROM {tabela}")
                df = pd.read_sql_query(query, con=engine)
                print(f"Dados da tabela '{tabela}' carregados com sucesso. Número de linhas: {len(df)}")
                dataframes.append(df)
            except SQLAlchemyError as e:
                print(f"Erro ao carregar dados da tabela '{tabela}': {e}")
                return None
            except Exception as e:
                print(f"Erro inesperado ao carregar dados da tabela '{tabela}': {e}")
                return None
        return dataframes
    else:
        print("Erro: Engine de conexão é inválida.")
        return None
    
def main():
    print("Esta é a questão: Consolidando Dados")
    nome_banco = DB_PATH + "INFwebNET_DB.db"
    nome_tabela_principal = "Usuarios_Historicos"
    nome_tabela_consolidado = "Consolidado"
    idade_min = 22
    idade_max = 30
    
    coluna_chave = "id"  
    
    engine = conectar_banco_dados(nome_banco)
    
    df_usuarios = consultar_usuarios_idade(engine, tabela=nome_tabela_principal, idade_min=idade_min, idade_max=idade_max)
    
    if df_usuarios is not None:
        df_usuarios = remover_duplicatas(df_usuarios, coluna_chave=coluna_chave)
    
    if df_usuarios is not None:
        criar_tabela_consolidado(engine, df_usuarios, nome_tabela=nome_tabela_consolidado, if_exists='replace')
    else:
        print("Não foi possível consolidar os dados devido a erros anteriores.")