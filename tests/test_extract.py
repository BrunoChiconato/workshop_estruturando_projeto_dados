import pytest  # type: ignore
from unittest.mock import patch, MagicMock
import pandas as pd  # type: ignore
from funcs.extract import extract_and_consolidate  # type: ignore

@patch('funcs.extract.DataExtractor')
def test_extract_and_consolidate(MockDataExtractor):
    """
    Testa a função `extract_and_consolidate` para garantir que ela consolida 
    corretamente os dados de várias fontes (CSV, JSON e Parquet) em um único DataFrame.

    A função simula os métodos da classe `DataExtractor` usando mocks para evitar o acesso 
    ao sistema de arquivos. O teste valida os seguintes aspectos:

    - O método `validate_input_path` aceita o caminho dos dados fornecido.
    - Os métodos `read_csv_data`, `read_json_data` e `read_parquet_data` retornam 
      DataFrames simulados para os dados CSV, JSON e Parquet, respectivamente.
    - A saída da função `extract_and_consolidate` é um DataFrame consolidado que corresponde 
      à estrutura e aos valores esperados.
    - Verifica se cada método de leitura foi chamado exatamente uma vez com o caminho correto.
    
    Parâmetros:
    - MockDataExtractor (MagicMock): Mock da classe `DataExtractor` para simular a leitura 
      de dados e evitar acessos reais ao sistema de arquivos.

    Exceções:
    - Levanta um erro de asserção se a saída da função não corresponder ao DataFrame esperado.
    """
    mock_extractor = MockDataExtractor.return_value
    
    mock_extractor.validate_input_path.side_effect = lambda path: path
    
    mock_extractor.read_csv_data.return_value = pd.DataFrame({
        'order_id': [1, 2], 
        'customer_id': [202, 448], 
        'order_date': ['2023-01-01', '2023-01-02'], 
        'product_id': [1484, 1027], 
        'quantity': [5, 4], 
        'price': [99.68, 20.8], 
        'payment_method': ['Cash', 'Debit Card'], 
        'store_location': ['Los Angeles', 'Houston']
    })
    mock_extractor.read_json_data.return_value = pd.DataFrame({
        'order_id': [3], 
        'customer_id': [370], 
        'order_date': ['2023-01-03'], 
        'product_id': [1713], 
        'quantity': [6], 
        'price': [362.8], 
        'payment_method': ['Credit Card'], 
        'store_location': ['New York']
    })
    mock_extractor.read_parquet_data.return_value = pd.DataFrame({
        'order_id': [4], 
        'customer_id': [206], 
        'order_date': ['2023-01-04'], 
        'product_id': [1038], 
        'quantity': [7], 
        'price': [214.82], 
        'payment_method': ['Credit Card'], 
        'store_location': ['Houston']
    })
    
    data_path = 'fake_path'
    
    result = extract_and_consolidate(data_path)
    
    mock_extractor.read_csv_data.assert_called_once_with(input_path=data_path)
    mock_extractor.read_json_data.assert_called_once_with(input_path=data_path)
    mock_extractor.read_parquet_data.assert_called_once_with(input_path=data_path)
    
    expected_data = pd.DataFrame({
        'order_id': [1, 2, 3, 4], 
        'customer_id': [202, 448, 370, 206], 
        'order_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'], 
        'product_id': [1484, 1027, 1713, 1038], 
        'quantity': [5, 4, 6, 7], 
        'price': [99.68, 20.8, 362.8, 214.82], 
        'payment_method': ['Cash', 'Debit Card', 'Credit Card', 'Credit Card'], 
        'store_location': ['Los Angeles', 'Houston', 'New York', 'Houston']
    })
    
    pd.testing.assert_frame_equal(result, expected_data)