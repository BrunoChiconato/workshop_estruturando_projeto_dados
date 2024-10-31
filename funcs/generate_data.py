import os

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

np.random.seed(42)

def generate_data(path: str) -> None:
    """
    Gera dados fictícios de vendas e salva em CSV, Parquet e JSON.

    Esta função cria um conjunto de dados fictícios com as seguintes colunas:
    
    - order_id (int)
    - customer_id (int)
    - order_date (date)
    - product_id (int)
    - quantity (int)
    - price (float)
    - payment_method (string)
    - store_location (string)

    A função verifica se o diretório especificado pelo argumento 'path' existe.
    Caso o diretório não exista, ele será criado. Em seguida, os dados são gerados
    e salvos nos formatos 'csv', 'parquet' e 'json'.

    Args:
        path (str): Caminho da pasta onde os arquivos serão salvos.

    Returns:
        None
    """
    n: int = 1000
    data: pd.DataFrame = pd.DataFrame({
        'order_id': np.arange(1, n+1),
        'customer_id': np.random.randint(100, 500, size=n),
        'order_date': pd.date_range('2023-01-01', periods=n, freq='D'),
        'product_id': np.random.randint(1000, 2000, size=n),
        'quantity': np.random.randint(1, 10, size=n),
        'price': np.round(np.random.uniform(10, 500, size=n), 2),
        'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'PayPal'], size=n),
        'store_location': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], size=n)
    })

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    data.to_csv(os.path.join(path, 'vendas_ficticias.csv'), index=False)
    data.to_parquet(os.path.join(path,'vendas_ficticias.parquet'), index=False)
    data.to_json(os.path.join(path,'vendas_ficticias.json'), orient='records', lines=True)

    print('Arquivos criados com sucesso!')

if __name__ == '__main__':
    output_path: str = './data/raw/'
    generate_data(output_path)
