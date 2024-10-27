# Workshop - Como Estruturar seu Projeto de Dados do Zero

## Objetivo
Este repositório tem como objetivo implementar um exemplo de um problema comum na Engenharia de Dados: receber dados de diferentes fontes, consolidá-los em um único arquivo, aplicar transformações e carregá-los em um banco de dados, utilizando `Python` e a estrutura abordada no workshop **Como Estruturar seu Projeto de Dados do Zero**, seguindo as melhores práticas da Engenharia de Dados. O repositório oficial do workshop está disponível [aqui](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/01-como-estruturar-projetos-e-processos-de-dados-do-zero). Neste repositório, são utilizadas as seguintes ferramentas:

1. Git e GitHub;
2. `Pyenv` e `Poetry` para gestão de ambiente e dependências;
3. Modularização do código;
4. Utilização de funções, classes e decoradores;
5. Testes unitários com `pytest`;
6. Banco de dados PostgreSQL hospedado no Render;
7. Utilização da biblioteca `SQLAlchemy` para gravar o DataFrame consolidado no banco em nuvem;
8. Utilização das bibliotecas `isort` e `black` para padronização do código;
9. Utilização da biblioteca `Pandera` para validação dos schemas dos DataFrames de input;
10. Utilização da biblioteca `taskipy` para automação de tarefas. 

### Próximas Implementações:
1. Construir uma documentação com `mkdocs` e realizar seu deploy.

## Estrutura do Projeto
A estrutura atual do projeto é a seguinte:
```plaintext
workshop_estruturando_projeto_dados
├── .vscode
│   └── settings.json            # Configurações específicas do Visual Studio Code.
├── app
│   └── pipeline.py              # Arquivo principal que orquestra a execução do pipeline de dados.
├── classes
│   ├── __init__.py              # Permite que o diretório seja tratado como um pacote.
│   └── data_extractor.py        # Módulo que contém a classe para extração de dados.
├── data                         # Diretório contendo os dados brutos.
│   └── raw
│       ├── dados_vendas.csv
│       ├── dados_vendas.json
│       └── dados_vendas.parquet    
├── decorators
│   ├── __init__.py              # Permite que o diretório seja tratado como um pacote.
│   └── decorators.py            # Módulo que contém os decoradores utilizados.
├── funcs
│   ├── __init__.py              # Permite que o diretório seja tratado como um pacote.
│   ├── extract.py               # Módulo responsável por extrair dados.
│   ├── generate_data.py         # Módulo que gera dados simulados para testes.
│   ├── load.py                  # Módulo responsável por carregar dados processados.
│   └── transform.py             # Módulo que contém funções para transformar e consolidar os dados.
├── tests
│   ├── __init__.py              # Permite que o diretório seja tratado como um pacote.
│   ├── test_extract.py          # Testes unitários para as funções de extração de dados.
│   ├── test_load.py             # Testes unitários para as funções de carga de dados.
│   └── test_transform.py        # Testes unitários para as funções de transformação de dados.
├── .gitignore                   # Arquivo para especificar quais arquivos devem ser ignorados pelo Git.
├── .python-version              # Arquivo que define a versão do Python usada no projeto.
├── poetry.lock                  # Arquivo de bloqueio gerado pelo Poetry, com as versões exatas das dependências.
├── pyproject.toml               # Arquivo de configuração do Poetry, especificando dependências e configurações do projeto.
└── README.md                    # Arquivo de documentação do projeto.
```

## Como executar esse projeto?

1. Clone este repositório utilizando o seguinte comando:
    ```bash
    git clone git@github.com:BrunoChiconato/workshop_estruturando_projeto_dados.git
    ```
   
2. Certifique-se de que o `pyenv` está instalado em sua máquina. A versão do Python será automaticamente ajustada para 3.12.5 ao navegar para o diretório do projeto, pois o arquivo `.python-version` já está definido.

3. Instale o `poetry` e todas as dependências do projeto utilizando o comando:
    ```bash
    poetry install
    ```

4. Para gerar os arquivos que serão utilizados na pipeline, execute o seguinte comando:
    ```bash
    poetry run task gen_data
    ```

5. Agora, você estará pronto para executar o código principal presente em `pipeline.py` utilizando o comando:
    ```bash
    poetry run task main
    ```

6. Para saber quais outros comandos você poderá executar dentro desse projeto, execute o seguinte comando:
    ```bash
    poetry run task --list
    ```