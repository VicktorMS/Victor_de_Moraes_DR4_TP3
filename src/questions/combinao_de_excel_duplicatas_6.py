from src.questions.combinao_de_excel_linhas_5 import carregar_planilhas_excel
from src.questions.manipulao_de_dados_3 import salvar_para_excel
import pandas as pd
from utils.constants import DATA_PATH

# 6 - Combinação de Excel Duplicatas
########################

def combinar_dataframes(dfs):
    """
    Combina múltiplos DataFrames em um único DataFrame.

    :param dfs: Lista de DataFrames a serem combinados.
    :return: DataFrame combinado.
    """
    try:
        df_combinado = pd.concat(dfs, ignore_index=True)
        print(f"DataFrames combinados com sucesso. Total de linhas após a combinação: {len(df_combinado)}")
        return df_combinado
    except ValueError as e:
        print(f"Erro ao combinar DataFrames: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao combinar DataFrames: {e}")
        return None

def remover_duplicatas(df, coluna_chave):
    """
    Remove duplicatas de um DataFrame com base em uma coluna específica.

    :param df: DataFrame do qual as duplicatas serão removidas.
    :param coluna_chave: Nome da coluna usada para identificar duplicatas.
    :return: DataFrame sem duplicatas.
    """
    if df is not None:
        try:
            num_duplicatas = df.duplicated(subset=coluna_chave).sum()
            df_limpo = df.drop_duplicates(subset=coluna_chave).reset_index(drop=True)
            print(f"Removidas {num_duplicatas} duplicatas baseadas na coluna '{coluna_chave}'.")
            return df_limpo
        except KeyError:
            print(f"Erro: A coluna '{coluna_chave}' não existe no DataFrame.")
            return df
        except Exception as e:
            print(f"Erro ao remover duplicatas: {e}")
            return df
    else:
        print("Erro: DataFrame de entrada é inválido.")
        return None
def main():
    print("Esta é a questão: Combinação de Excel Duplicatas")
    arquivo_excel = DATA_PATH + "INFwebNET_Historico.xlsx"
    planilhas = ["INFwebNET2022", "INFwebNET2023"]
    arquivo_saida = DATA_PATH + "INFwebNET_Historico_Combinado.xlsx"
    coluna_duplicata = "id"
    
    dados_planilhas = carregar_planilhas_excel(arquivo_excel, planilhas)
    
    if dados_planilhas is not None:
        df_combinado = combinar_dataframes(list(dados_planilhas.values()))
        df_limpo = remover_duplicatas(df_combinado, coluna_duplicata)
        salvar_para_excel(df_limpo, arquivo_saida)
    else:
        print("Não foi possível carregar as planilhas especificadas. Processo interrompido.")