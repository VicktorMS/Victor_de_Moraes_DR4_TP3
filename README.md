# Python para Dados [24E4_4] Teste de Performance - TP3

Prezado Avaliador,

Neste projeto, você encontrará 9 resoluções das 12 questões apresentadas no Teste de Performance (TP3). As orientações para executar o projeto estão detalhadas no arquivo README.

Conforme solicitado no enunciado da questão, o projeto foi [submetido em um repositório](https://github.com/VicktorMS/Victor_de_Moraes_DR4_TP2).

Caso tenha qualquer dúvida ou precise de informações adicionais, não hesite em entrar em contato diretamente comigo.

Atenciosamente,
Victor de Moraes
victor.dsilva@al.infnet.edu.br

## Como instalar e configurar esse projeto 

### 1. Criar um Ambiente Virtual

Certifique-se de criar ou ativar um ambiente virtual:

```bash
python -m venv nome_do_ambiente
```

Substitua nome_do_ambiente pelo nome desejado para o ambiente virtual.
### 2. Ativar o Ambiente Virtual

No Windows:

```bash
nome_do_ambiente\Scripts\activate
```
No Linux/MacOS:
```bash
source nome_do_ambiente/bin/activate
```
Após ativar, você verá algo como (nome_do_ambiente) no início do terminal.
### 3. Instalar as Dependências

Com o ambiente virtual ativado, use o comando pip para instalar as dependências listadas no requirements.txt:
```bash
pip install -r requirements.txt
```
## Como está estruturado o projeto

### `questions`
Todos as questões estão organizadas em módulos separados dentro do diretório `src/questions`. Elas estão listadas de acordo com a ordem forma que foram apresentadas no moodle.

Por exemplo, o seguinte enunciado:

> <b>1. (★) Abrindo as Portas:</b><br>
a. Escreva um programa que leia o arquivo ""rede_INFNET_atualizado.txt" que foi elaborado no seu TP1, que contém dados básicos dos usuários (nome, idade, cidade, estado) - INFNETianos; <br>
b. Utilizando a biblioteca csv, exporte um arquivo “INFwebNet.csv” contendo os mesmos dados.

Equivale ao módulo `src/questions/abrindo_as_portas_1.py` gerado automáticamente pelo `src/utils/generate_questions.py`.

### `data`
Diretório que contém todos os arquivos consumidos e gerados pelas questões.

### `utils`
Contém módulos usados apenas na inicialização do projeto, tem como objetivo gerar um módulo específico para cada questão. Na maior parte é irrelevante para o Avaliador.


### `helpers`
Contém módulos que agrupam funções comuns a várias questões. 

Ex: `carregar_dados`, `salvar_dados`...

## Como rodar as questões

Após a configuração do projeto, basta executar o scipt `main.py`, que serve como entrypoint da aplicação.
```bash 
python main.py
```

Após isso será solicitado ao usuário o número da questão que será executada, novamente, as questões estão ordenadas de acordo com a ordem do Moodle.

Exemplo de execução:
```bash 
Digite o número da questão para executar (1, 2, 3...): 13
Esta é a questão: Selecionando INFNETiano
...
Executando questão 13...
```