# 1 - Erros ao Carregar Arquivo
########################

def carregar_arquivo(nome_arquivo):
    """
    Tenta abrir um arquivo e retorna seu conteúdo.
    Exibe uma mensagem de erro se o arquivo não for encontrado.

    :param nome_arquivo: Nome do arquivo a ser carregado.
    :return: Conteúdo do arquivo ou None se não for possível carregar.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que o arquivo está disponível.")
        return None
    
def main():
    print("Esta é a questão: Erros ao Carregar Arquivo")
    arquivo = "src/data/dados_usuarios.csv"
    conteudo = carregar_arquivo(arquivo)
    if conteudo:
        print("Arquivo carregado com sucesso!")
    else:
        print("Não foi possível carregar o arquivo.")