import os
from urllib.parse import quote_plus

import pandas as pd  # type: ignore
from dotenv import load_dotenv  # type: ignore
from loguru import logger  # type: ignore
from sqlalchemy import create_engine, text  # type: ignore

from decorators.decorators import log_decorator, time_decorador

load_dotenv()

@time_decorador
@log_decorator
def load_data(data: pd.DataFrame) -> None:
    """
    Carrega um DataFrame em uma tabela PostgreSQL chamada 'sales_consolidated' no Render.

    Esta função estabelece uma conexão com um banco de dados PostgreSQL usando credenciais armazenadas
    em variáveis de ambiente. Se as credenciais estiverem corretas e a conexão for bem-sucedida, 
    os dados do DataFrame fornecido serão carregados na tabela 'sales_consolidated'. Caso a tabela 
    já exista, ela será substituída.

    Parameters:
        data : pd.DataFrame
            O DataFrame contendo os dados que serão carregados no banco de dados.

    Exceptions:
        ValueError:
            Levantada se qualquer uma das variáveis de ambiente necessárias estiver ausente.
        Exception:
            Levantada para qualquer erro ocorrido durante o processo de conexão ou inserção de dados no banco de dados,
            com um log detalhado do erro.

    Logs:
        - Loga um erro se as variáveis de ambiente estiverem ausentes.
        - Loga a confirmação de que a tabela foi criada e os dados foram carregados com sucesso.
        - Loga um erro detalhado caso haja falha no processo.

    Returns:
        None
            A função não retorna nada, mas levanta exceções em caso de erro.
    """
    db_username = quote_plus(os.getenv('DB_USERNAME'))
    db_password = quote_plus(os.getenv('DB_PASSWORD'))
    db_hostname = os.getenv('DB_HOSTNAME')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    try:
        if not all([db_username, db_password, db_hostname, db_port, db_name]):
            logger.error("Algumas variáveis de ambiente estão ausentes.")
            raise ValueError("Variáveis de ambiente necessárias para a conexão ao banco de dados não foram encontradas.")
        
        connection_url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_name}"

        engine = create_engine(connection_url, connect_args={'client_encoding': 'utf8'})

        data.to_sql('sales_consolidated', engine, if_exists='replace', index=False)
        logger.info("Tabela criada e dados carregados com sucesso!")

    except Exception as e:
        logger.error(f'Erro: {e}')
        raise