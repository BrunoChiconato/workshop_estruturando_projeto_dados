## Conteúdo

Esta seção descreve o código em Python localizado em `funcs/extract.py`, que extrai dados de diferentes tipos de arquivos, consolida-os em um **DataFrame** e retorna o **DataFrame** consolidado. Para alcançar esse objetivo, é definida a função `extract_and_consolidate`.

A função `extract_and_consolidate` utiliza a biblioteca `pandas` para a extração e consolidação dos dados. Ela faz uso da classe `DataExtractor` (descrita em detalhes na seção **Classes**) e aplica dois decoradores: um para registrar logs e outro para calcular o tempo total de execução da função, ambos explicados na seção **Decoradores** desta documentação.

A função recebe como parâmetro o caminho do diretório onde os dados de entrada estão armazenados. Em seguida, cria uma instância da classe `DataExtractor` e utiliza seus métodos para ler dados em diferentes formatos, armazenando cada conjunto de dados em um DataFrame específico. Por fim, a função concatena todos esses DataFrames e retorna o resultado consolidado ao usuário.

## Função `extract_and_consolidate`

::: funcs.extract.extract_and_consolidate
