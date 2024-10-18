import pandas as pd # type: ignore

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma um DataFrame agrupando os valores de 'price' por 'payment_method'.
    
    A função verifica se as colunas 'payment_method' e 'price' estão presentes no DataFrame 
    fornecido e, em seguida, realiza um agrupamento dos dados, somando os valores da coluna 
    'price' para cada método de pagamento. Retorna um novo DataFrame com duas colunas: 
    'payment_method' e 'price', onde 'price' representa a soma total para cada método de pagamento.

    Parâmetros:
    ----------
    data : pd.DataFrame
        DataFrame de entrada que deve conter as colunas 'payment_method' e 'price'.

    Retorna:
    -------
    pd.DataFrame
        DataFrame transformado com as colunas:
        - 'payment_method': Métodos de pagamento únicos.
        - 'price': Soma dos preços correspondentes a cada método de pagamento.

    Erros:
    ------
    KeyError
        Se a coluna 'payment_method' ou 'price' não estiver presente no DataFrame.
    
    Exception
        Se ocorrer qualquer outro erro durante a execução da função, uma mensagem de erro 
        será exibida e um DataFrame vazio será retornado.
    """
    transform_data: pd.DataFrame = pd.DataFrame()

    try:
        columns = data.columns.str.strip()

        if 'payment_method' not in columns:
            raise KeyError("A coluna 'payment_method' não foi encontrada.")
        if 'price' not in columns:
            raise KeyError("A coluna 'price' não foi encontrada.")
        
        transform_data = data.groupby('payment_method')['price'].sum().reset_index()
        transform_data.columns = ['payment_method', 'price']

        return transform_data
    
    except Exception as e:
        print(f'Erro: {e} Tente novamente.')
        return transform_data