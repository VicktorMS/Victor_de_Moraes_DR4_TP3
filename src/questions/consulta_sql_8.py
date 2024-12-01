from src.questions.carregando_em_sql_7 import conectar_banco_dados
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from utils.constants import DB_PATH
# 8 - Consulta SQL
########################

def consultar_usuarios_idade(engine, tabela='Usuarios_Historicos', idade_min=22, idade_max=30):
    """
    Executa uma consulta SQL para selecionar usuários com idade entre idade_min e idade_max.

    :param engine: Engine de conexão com o banco de dados.
    :param tabela: Nome da tabela SQL onde os dados estão armazenados.
    :param idade_min: Idade mínima para filtragem.
    :param idade_max: Idade máxima para filtragem.
    :return: DataFrame com os usuários filtrados ou None se ocorrer um erro.
    """
    if engine is not None:
        try:
            query = text(f"""
                SELECT *
                FROM {tabela}
                WHERE idade BETWEEN :min_idade AND :max_idade
            """)
            parametros = {"min_idade": idade_min, "max_idade": idade_max}
            df_resultado = pd.read_sql_query(query, con=engine, params=parametros)
            print(f"Consulta executada com sucesso. Número de usuários encontrados: {len(df_resultado)}")
            return df_resultado
        except SQLAlchemyError as e:
            print(f"Erro ao executar a consulta na tabela '{tabela}': {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao executar a consulta na tabela '{tabela}': {e}")
            return None
    else:
        print("Erro: Engine de conexão é inválida.")
        return None


def exibir_resultado(df):
    """
    Exibe o DataFrame resultante da consulta na tela.

    :param df: DataFrame com os dados a serem exibidos.
    """
    if df is not None and not df.empty:
        print("\nUsuários com idade entre 22 e 30 anos:")
        print(df)
    elif df is not None and df.empty:
        print("Nenhum usuário encontrado com a faixa etária especificada.")
    else:
        print("Erro: DataFrame está vazio ou não foi carregado corretamente.")


def main():
    print("Esta é a questão: Consulta SQL")
        
    nome_banco = DB_PATH + "INFwebNET_DB.db"
    nome_tabela = "Usuarios_Historicos"
    idade_min = 22
    idade_max = 30
    
    engine = conectar_banco_dados(nome_banco)
    
    df_usuarios = consultar_usuarios_idade(engine, tabela=nome_tabela, idade_min=idade_min, idade_max=idade_max)
    
    exibir_resultado(df_usuarios)