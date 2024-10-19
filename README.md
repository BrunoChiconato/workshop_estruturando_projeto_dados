# workshop_estruturando_projeto_dados
## Como executar esse projeto?
1. **Clone este repositório** utilizando o seguinte comando:
    ```bash
    git clone git@github.com:BrunoChiconato/workshop_estruturando_projeto_dados.git
    ```
   
2. **Certifique-se de que o Pyenv está instalado** em sua máquina. A versão do Python será automaticamente ajustada para 3.12.5 ao navegar para o diretório do projeto, pois o arquivo `.python-version` já está definido.

3. **Instale o Poetry** e todas as dependências do projeto utilizando o comando:
    ```bash
    poetry install
    ```

4. A partir deste momento, você poderá executar os códigos presentes na pasta `app`. Navegue até essa pasta utilizando o comando:
    ```bash
    cd app
    ```
5. Para gerar os arquivos que serão utilizados na pipeline, execute o seguinte comando:
    ```bash
    python funcs/generate_data.py
    ```

6. Agora, você estará pronto para executar o código principal presente em `pipeline.py` utilizando o comando:
    ```bash
    python -m src.pipeline
    ```