# Workshop - Estruturando Projetos de Dados do Zero

## Objetivo

Este repositório exemplifica uma solução para um problema comum na Engenharia de Dados: consolidar dados provenientes de diversas fontes, aplicar transformações necessárias e carregá-los em um banco de dados. A implementação utiliza `Python` e é baseada nas práticas abordadas no workshop **Estruturando Projetos de Dados do Zero**. O repositório original do workshop está disponível [aqui](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/01-como-estruturar-projetos-e-processos-de-dados-do-zero).

O projeto visa demonstrar o uso de ferramentas e práticas recomendadas na Engenharia de Dados, incluindo:

1. Controle de versão com Git e GitHub;
2. Gestão de ambiente e dependências com `Pyenv` e `Poetry`;
3. Estruturação modular de código;
4. Uso de funções, classes e decoradores para organização e reutilização de código;
5. Implementação de testes unitários com `pytest`;
6. Persistência de dados em PostgreSQL, hospedado em nuvem no Render;
7. Integração da biblioteca `SQLAlchemy` para gravação do DataFrame consolidado no banco de dados;
8. Padronização de código com `isort` e `black`;
9. Validação de schemas de DataFrames com a biblioteca `Pandera`;
10. Automação de tarefas com `taskipy`;
11. Documentação com `MkDocs`.

## Documentação

Para consultar a documentação detalhada do projeto, acesse [este link](https://brunochiconato.github.io/workshop_estruturando_projeto_dados/).

## Estrutura do Projeto

Abaixo está a estrutura de diretórios e arquivos do projeto:

```plaintext
workshop_estruturando_projeto_dados
├── .vscode
│   └── settings.json            # Configurações do Visual Studio Code específicas para o projeto.
├── app
│   └── pipeline.py              # Script principal que orquestra a execução do pipeline de dados.
├── classes
│   ├── __init__.py              # Torna o diretório um pacote Python.
│   └── data_extractor.py        # Módulo com a classe para extração de dados.
├── data                         # Diretório para armazenamento dos dados brutos.
│   └── raw
│       ├── dados_vendas.csv
│       ├── dados_vendas.json
│       └── dados_vendas.parquet
├── decorators
│   ├── __init__.py              # Torna o diretório um pacote Python.
│   └── decorators.py            # Módulo com decoradores para funcionalidades específicas.
├── documentation                # Diretório contendo arquivos da documentação.
├── funcs
│   ├── __init__.py              # Torna o diretório um pacote Python.
│   ├── extract.py               # Módulo de extração de dados.
│   ├── generate_data.py         # Módulo que gera dados simulados para testes.
│   ├── load.py                  # Módulo de carga de dados processados.
│   └── transform.py             # Módulo de funções para transformação e consolidação de dados.
├── tests
│   ├── __init__.py              # Torna o diretório um pacote Python.
│   ├── test_extract.py          # Testes unitários para funções de extração.
│   ├── test_load.py             # Testes unitários para funções de carga.
│   └── test_transform.py        # Testes unitários para funções de transformação.
├── .gitignore                   # Arquivo de configuração para ignorar arquivos no Git.
├── .python-version              # Define a versão Python usada no projeto.
├── poetry.lock                  # Arquivo de bloqueio do Poetry com as versões exatas das dependências.
├── pyproject.toml               # Arquivo de configuração do Poetry com dependências e configurações do projeto.
└── README.md                    # Documentação principal do projeto.
```

## Como Executar o Projeto

1. Clone este repositório executando:

    ```bash
    git clone git@github.com:BrunoChiconato/workshop_estruturando_projeto_dados.git
    ```

2. Verifique se o `pyenv` está instalado. A versão Python será automaticamente configurada para 3.12.5 ao entrar no diretório do projeto, conforme especificado no arquivo `.python-version`.

3. Instale o `Poetry` e todas as dependências do projeto com o comando:

    ```bash
    poetry install
    ```

4. Para gerar arquivos de exemplo para a pipeline, execute:

    ```bash
    poetry run task gen_data
    ```

5. Para rodar o código principal localizado em `pipeline.py`, utilize:

    ```bash
    poetry run task main
    ```

6. Para listar os outros comandos disponíveis neste projeto, execute:

    ```bash
    poetry run task --list
    ```
