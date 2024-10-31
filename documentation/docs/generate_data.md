## Conteúdo

A presente seção inclui um código em Python, localizado em `funcs/generate_data.py`, que gera dados fictícios de vendas para diversas finalidades. A função principal, `generate_data`, utiliza as bibliotecas `os`, `pandas` e `numpy` para criar dados simulados e salvá-los em formatos variados, incluindo `.csv`, `.json` e `.parquet`.

Abaixo está uma descrição detalhada do funcionamento da função `generate_data`:

1. **Parâmetro de caminho**: A função recebe uma string que especifica o caminho onde os dados gerados serão salvos. Esse caminho pode ser personalizado pelo usuário.

2. **Definição do tamanho dos dados**: O número de linhas do conjunto de dados é definido na função. Neste projeto, o valor padrão é `n = 1000`, mas pode ser ajustado conforme a necessidade.

3. **Criação do DataFrame**: Utilizando a biblioteca `pandas`, a função cria um **DataFrame** e define colunas que representam um relatório de vendas fictício. Para popular essas colunas, são utilizados arrays gerados com a biblioteca `numpy`, simulando dados como identificadores de vendas, valores, datas e outros detalhes relevantes.

4. **Verificação e criação do caminho**: A função verifica se o caminho fornecido existe. Caso o caminho não exista, ele é criado automaticamente para garantir que os arquivos possam ser salvos.

5. **Salvamento dos arquivos**: O **DataFrame** gerado é salvo nos três formatos de arquivo especificados (`.csv`, `.json` e `.parquet`). Após o salvamento, uma mensagem de sucesso é exibida, confirmando que os arquivos foram gerados com sucesso.

## Função `generate_data`

::: funcs.generate_data.generate_data