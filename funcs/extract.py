import pandas as pd  # type: ignore

from classes.data_extractor import DataExtractor
from decorators.decorators import log_decorator, time_decorador


@time_decorador
@log_decorator
def extract_and_consolidate(data_path: str) -> pd.DataFrame:
    """
    Extrai e consolida dados de arquivos CSV, JSON e Parquet em um único DataFrame.

    Esta função cria uma instância da classe DataExtractor para ler dados de diferentes formatos
    de arquivos (CSV, JSON e Parquet) presentes em um diretório específico. Após a extração, os
    dados são concatenados em um único DataFrame.

    Parameters:
        data_path (str): Caminho do diretório onde os arquivos CSV, JSON e Parquet estão localizados.

    Returns:
        pd.DataFrame: DataFrame contendo os dados consolidados de todos os arquivos extraídos.

    Raises:
        FileNotFoundError: Se algum dos arquivos CSV, JSON ou Parquet não for encontrado no diretório especificado.
    """
    extractor = DataExtractor()

    csv_data: pd.DataFrame = extractor.read_csv_data(input_path = data_path)
    json_data: pd.DataFrame = extractor.read_json_data(input_path = data_path)
    parquet_data: pd.DataFrame = extractor.read_parquet_data(input_path = data_path)

    consolidate_data: pd.DataFrame = pd.concat([csv_data, json_data, parquet_data], ignore_index=True)
    return consolidate_data
