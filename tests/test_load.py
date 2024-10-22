import pytest # type: ignore
import pandas as pd # type: ignore
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError # type: ignore
from funcs.load import load_data

@patch("funcs.load.create_engine")
@patch("funcs.load.quote_plus")
@patch("funcs.load.os.getenv")
def test_load_data_success(mock_getenv, mock_quote_plus, mock_create_engine):
    """
    Testa o comportamento da função `load_data` quando os dados são carregados com sucesso.

    Este teste simula um cenário onde todas as variáveis de ambiente necessárias estão presentes
    e a conexão com o banco de dados PostgreSQL é bem-sucedida. Verifica se a função `to_sql` 
    do pandas é chamada corretamente para carregar os dados na tabela.

    Parameters:
        mock_getenv: MagicMock
            Mock da função `os.getenv` para simular variáveis de ambiente.
        mock_quote_plus: MagicMock
            Mock da função `quote_plus` para simular a codificação de strings.
        mock_create_engine: MagicMock
            Mock da função `create_engine` para simular a criação de uma conexão com o banco de dados.

    Assertions:
        Verifica se `to_sql` foi chamado com os parâmetros corretos, garantindo que a função
        tenta carregar os dados no banco de dados.
    """
    mock_getenv.side_effect = lambda x: {
        'DB_USERNAME': 'user',
        'DB_PASSWORD': 'pass',
        'DB_HOSTNAME': 'localhost',
        'DB_PORT': '5432',
        'DB_NAME': 'test_db'
    }.get(x)
    mock_quote_plus.side_effect = lambda x: x

    data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['a', 'b', 'c']})

    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    with patch.object(pd.DataFrame, 'to_sql', return_value=None) as mock_to_sql:
        load_data(data)
        mock_to_sql.assert_called_once_with('sales_consolidated', mock_engine, if_exists='replace', index=False)

@patch("funcs.load.os.getenv")
def test_load_data_missing_env_vars(mock_getenv):
    """
    Testa o comportamento da função `load_data` quando variáveis de ambiente necessárias estão ausentes.

    Este teste simula a ausência de uma variável de ambiente essencial para a conexão com o banco de dados
    PostgreSQL (DB_USERNAME). Verifica se a função levanta uma exceção `ValueError` com a mensagem esperada.

    Parameters:
        mock_getenv: MagicMock
            Mock da função `os.getenv` para simular a ausência de variáveis de ambiente.

    Assertions:
        Verifica se a função `load_data` levanta uma `ValueError` quando uma variável de ambiente essencial
        está ausente.
    """
    mock_getenv.side_effect = lambda x: "" if x == 'DB_USERNAME' else 'value'

    data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['a', 'b', 'c']})

    with pytest.raises(ValueError, match="Variáveis de ambiente necessárias para a conexão ao banco de dados não foram encontradas."):
        load_data(data)

@patch("funcs.load.create_engine")
@patch("funcs.load.quote_plus")
@patch("funcs.load.os.getenv")
def test_load_data_connection_error(mock_getenv, mock_quote_plus, mock_create_engine):
    """
    Testa o comportamento da função `load_data` ao ocorrer um erro de conexão com o banco de dados.

    Este teste simula um cenário onde as variáveis de ambiente estão presentes, mas ocorre um erro
    ao criar a engine de conexão ao banco de dados PostgreSQL. Verifica se a função levanta uma 
    `SQLAlchemyError` corretamente.

    Parameters:
        mock_getenv: MagicMock
            Mock da função `os.getenv` para simular variáveis de ambiente.
        mock_quote_plus: MagicMock
            Mock da função `quote_plus` para simular a codificação de strings.
        mock_create_engine: MagicMock
            Mock da função `create_engine` para simular uma falha ao criar a conexão com o banco de dados.

    Assertions:
        Verifica se a função `load_data` levanta uma `SQLAlchemyError` quando ocorre um problema
        ao criar a conexão com o banco de dados.
    """
    mock_getenv.side_effect = lambda x: {
        'DB_USERNAME': 'user',
        'DB_PASSWORD': 'pass',
        'DB_HOSTNAME': 'localhost',
        'DB_PORT': '5432',
        'DB_NAME': 'test_db'
    }.get(x)
    mock_quote_plus.side_effect = lambda x: x

    mock_create_engine.side_effect = SQLAlchemyError("Erro de conexão")

    data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['a', 'b', 'c']})

    with pytest.raises(SQLAlchemyError, match="Erro de conexão"):
        load_data(data)