## Descrição

Esta seção descreve o código em Python localizado em `funcs/extract.py`, que extrai dados de diferentes tipos de arquivos, consolida-os em um **DataFrame** e retorna o **DataFrame** consolidado. Para alcançar esse objetivo, é definida a função `extract_and_consolidate`.

A função `extract_and_consolidate` utiliza a biblioteca `pandas` para a extração e consolidação dos dados. Ela faz uso da classe `DataExtractor` (descrita em detalhes na seção **Classes**) e aplica dois decoradores: um para registrar logs e outro para calcular o tempo total de execução da função, ambos explicados na seção **Decoradores** desta documentação.

A função recebe como parâmetro o caminho do diretório onde os dados de entrada estão armazenados. Em seguida, cria uma instância da classe `DataExtractor` e utiliza seus métodos para ler dados em diferentes formatos, armazenando cada conjunto de dados em um DataFrame específico. Por fim, a função concatena todos esses DataFrames e retorna o resultado consolidado ao usuário.

## Função `extract_and_consolidate`

::: funcs.extract.extract_and_consolidate

## Teste unitário

Esse teste unitário verifica o comportamento correto da função `extract_and_consolidate` utilizando mocks para simular as operações da classe `DataExtractor`. Isso permite validar a função sem realmente acessar o sistema de arquivos.

### Aspectos validados

1. **Validação do caminho de entrada**: O teste assegura que o método `validate_input_path` aceita o caminho dos dados fornecido.
2. **Leitura de dados simulados**:
      - São criados mocks para os métodos `read_csv_data`, `read_json_data` e `read_parquet_data`, que retornam DataFrames pré-definidos para simular dados CSV, JSON e Parquet.
      - Esses mocks garantem que o teste é isolado do sistema de arquivos real.
3. **Consolidação dos dados**:
      - O teste chama a função `extract_and_consolidate` e compara o DataFrame resultante com um DataFrame esperado que contém a consolidação dos dados simulados.
      - A comparação é feita com `pd.testing.assert_frame_equal`, que verifica se o DataFrame resultante é idêntico ao esperado em estrutura e valores.
4. **Verificação de chamadas**:
      - O teste verifica que cada método de leitura (`read_csv_data`, `read_json_data`, `read_parquet_data`) foi chamado exatamente uma vez com o caminho correto, usando `assert_called_once_with`.
5. **Asserção final**: Caso a saída da função não corresponda ao DataFrame esperado, um erro de asserção é levantado, indicando uma falha no comportamento esperado da função.

## Função `test_extract_and_consolidate`

::: tests.test_extract.test_extract_and_consolidate
