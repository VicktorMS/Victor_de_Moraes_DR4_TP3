import pandas as pd
from questions.limpeza_de_dados_4 import carregar_dados_excel
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from utils.constants import DATA_PATH, DB_PATH


def conectar_banco_dados(nome_banco='INFwebNET_DB.db'):
    """
    Cria uma conexão com o banco de dados SQLite usando SQLAlchemy.

    :param nome_banco: Nome do arquivo do banco de dados SQLite.
    :return: Engine de conexão ou None se ocorrer um erro.
    """
    try:
        engine = create_engine(f'sqlite:///{nome_banco}', echo=False)
        # Testa a conexão executando uma consulta simples
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print(f"Conexão com o banco de dados '{nome_banco}' estabelecida com sucesso.")
        return engine
    except SQLAlchemyError as e:
        print(f"Erro ao conectar-se ao banco de dados '{nome_banco}': {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao conectar-se ao banco de dados '{nome_banco}': {e}")
        return None

def carregar_dados_para_sql(df, engine, nome_tabela='Usuarios_Historicos', if_exists='append'):
    """
    Carrega os dados do DataFrame para uma tabela SQL no banco de dados.

    :param df: DataFrame com os dados a serem carregados.
    :param engine: Engine de conexão com o banco de dados.
    :param nome_tabela: Nome da tabela SQL onde os dados serão inseridos.
    :param if_exists: O que fazer se a tabela já existir ('fail', 'replace', 'append').
    """
    if df is not None and engine is not None:
        try:
            # Carrega os dados para a tabela SQL
            df.to_sql(nome_tabela, con=engine, if_exists=if_exists, index=False)
            print(f"Dados carregados com sucesso na tabela '{nome_tabela}'.")
        except ValueError as e:
            print(f"Erro ao carregar dados na tabela '{nome_tabela}': {e}")
        except SQLAlchemyError as e:
            print(f"Erro de SQLAlchemy ao carregar dados na tabela '{nome_tabela}': {e}")
        except Exception as e:
            print(f"Erro inesperado ao carregar dados na tabela '{nome_tabela}': {e}")
    else:
        print("Erro: DataFrame ou Engine de conexão é inválido.")


# 7 - Carregando em SQL
########################
def main():
    print("Esta é a questão: Carregando em SQL")
    arquivo_excel = DATA_PATH + "INFwebNET_Historico_Combinado.xlsx"
    nome_banco = DB_PATH + "INFwebNET_DB.db"
    nome_tabela = "Usuarios_Historicos"
    
    # Passo 1: Carregar os dados do Excel
    dados = carregar_dados_excel(arquivo_excel)
    
    # Passo 2: Conectar-se ao banco de dados SQLite
    engine = conectar_banco_dados(nome_banco)
    
    # Passo 3: Carregar os dados para a tabela SQL
    if dados is not None and engine is not None:
        carregar_dados_para_sql(dados, engine, nome_tabela, if_exists='append')
    else:
        print("Não foi possível carregar os dados para o banco de dados devido a erros anteriores.")