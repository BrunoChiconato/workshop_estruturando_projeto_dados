import pytest  # type: ignore
import pandas as pd  # type: ignore
from funcs.transform import transform_data

def test_transform_data_success():
    """
    Testa a função `transform_data` com um DataFrame válido, verificando se 
    o agrupamento por 'payment_method' é realizado corretamente.
    """
    input_data = pd.DataFrame({
        'payment_method': ['Credit Card', 'Cash', 'Credit Card', 'Debit Card', 'Cash'],
        'price': [100.0, 50.0, 150.0, 200.0, 50.0]
    })

    expected_data = pd.DataFrame({
        'payment_method': ['Cash', 'Credit Card', 'Debit Card'],
        'price': [100.0, 250.0, 200.0]
    })

    result = transform_data(input_data)
    
    pd.testing.assert_frame_equal(result, expected_data)

def test_transform_data_missing_columns():
    """
    Testa a função `transform_data` quando as colunas necessárias estão ausentes,
    esperando que um DataFrame vazio seja retornado.
    """
    input_data_missing_column = pd.DataFrame({
        'price': [100.0, 200.0]
    })

    result = transform_data(input_data_missing_column)
    expected_data = pd.DataFrame()

    pd.testing.assert_frame_equal(result, expected_data)

    input_data_missing_price = pd.DataFrame({
        'payment_method': ['Credit Card', 'Cash']
    })

    result = transform_data(input_data_missing_price)

    pd.testing.assert_frame_equal(result, expected_data)

def test_transform_data_unexpected_exception():
    """
    Testa a função `transform_data` para verificar se uma exceção genérica é tratada
    e um DataFrame vazio é retornado.
    """
    input_data_invalid = pd.DataFrame({
        'payment_method': ['Credit Card', 'Cash'],
        'price': ['invalid_price', 'another_invalid']
    })

    result = transform_data(input_data_invalid)
    expected_data = pd.DataFrame()
    
    pd.testing.assert_frame_equal(result, expected_data)

