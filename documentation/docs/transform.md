## Descrição

Esta seção descreve a função `transform_data`, localizada em `funcs/transform.py`. Essa função recebe um `DataFrame` de entrada e aplica uma série de verificações e operações de transformação, com o objetivo de consolidar os valores da coluna `price` por método de pagamento (`payment_method`). O resultado final é um novo `DataFrame` com cada método de pagamento único e a soma dos preços correspondentes.

A função é decorada com dois decoradores:
- **`log_decorator`**: Registra logs da execução, permitindo rastrear o processamento dos dados.
- **`time_decorador`**: Mede o tempo de execução da função, facilitando o monitoramento de performance dentro da pipeline.

## Funcionamento

O funcionamento da função `transform_data` pode ser dividido nas seguintes etapas:

1. **Verificação das colunas necessárias**: A função começa verificando se as colunas `payment_method` e `price` estão presentes no `DataFrame` de entrada. Caso uma dessas colunas esteja ausente, um erro do tipo `KeyError` é levantado, informando a ausência da coluna necessária. Esse mecanismo de verificação garante que a função só prossiga se os dados mínimos exigidos estiverem presentes.

2. **Conversão de valores para numérico**: Em seguida, a função tenta converter os valores da coluna `price` para um tipo numérico. Se houver valores não numéricos, eles são convertidos para `NaN`. Essa etapa é importante para garantir que apenas valores válidos sejam considerados na agregação dos dados.

3. **Validação de dados numéricos**: A função verifica se todos os valores na coluna `price` são inválidos (`NaN`). Caso todos os valores sejam inválidos, a função retorna um `DataFrame` vazio e exibe uma mensagem de erro, informando que não há dados válidos para o cálculo.

4. **Agrupamento e soma dos valores**: Após a validação, a função realiza o agrupamento dos dados pela coluna `payment_method`, somando os valores correspondentes de `price` para cada método de pagamento. O resultado é um novo `DataFrame` com as colunas `payment_method` e `price`, onde cada linha representa um método de pagamento único e a soma total de `price` associada a ele.

5. **Tratamento de exceções**: Caso ocorra qualquer erro inesperado durante a execução da função, uma mensagem de erro é exibida e um `DataFrame` vazio é retornado. Esse tratamento garante a robustez da função, evitando falhas críticas na pipeline ETL.

## Função `transform_data`
::: funcs.transform.transform_data
