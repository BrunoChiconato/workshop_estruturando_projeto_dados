import glob
import os

import pandas as pd  # type: ignore
import pandera as pa  # type: ignore
from loguru import logger  # type: ignore


class DataExtractor:
    """
    Classe para extrair dados de diferentes formatos de arquivos, incluindo CSV, JSON e Parquet.

    Esta classe oferece métodos para validar a existência do caminho de entrada
    e para ler dados de arquivos nos formatos suportados, retornando-os como DataFrames do pandas.
    """
    def __init__(self):
        """
        Inicializa a classe DataExtractor com um esquema de validação Pandera para os dados extraídos.

        O esquema define as colunas esperadas e os tipos de dados, com verificações de integridade,
        como valores não nulos e limites numéricos mínimos.
        """
        self.schema = pa.DataFrameSchema({
            'order_id': pa.Column(int, checks = pa.Check.gt(0)),
            'customer_id': pa.Column(int, checks = pa.Check.gt(0)),
            'order_date': pa.Column(pa.DateTime),
            'product_id': pa.Column(int, checks = pa.Check.gt(0)),
            'quantity': pa.Column(int, checks = pa.Check.gt(0)),
            'price': pa.Column(float, checks = pa.Check.gt(0)),
            'payment_method': pa.Column(str, nullable = False),
            'store_location': pa.Column(str, nullable = False)
        })

    def validate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Valida e ajusta um DataFrame com base no esquema pré-definido.

        As colunas que não estão no tipo correto, como 'order_date' e 'customer_id', são convertidas
        para os tipos esperados (ex.: datetime para 'order_date' e int64 para IDs).

        Parameters:
            df: pd.DataFrame
                DataFrame que será validado.

        Returns:
            pd.DataFrame
                DataFrame validado de acordo com o esquema.

        Raises:
            pandera.errors.SchemaError
                Se o DataFrame não atender aos requisitos do esquema.
        """
        if 'order_date' in df.columns:
            df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        if 'customer_id' in df.columns:
            df['customer_id'] = df['customer_id'].astype('int64')
        if 'product_id' in df.columns:
            df['product_id'] = df['product_id'].astype('int64')
        if 'quantity' in df.columns:
            df['quantity'] = df['quantity'].astype('int64')

        try:
            validated_df = self.schema.validate(df)
            logger.info('DataFrame validado com sucesso!')
            return validated_df
        except pa.errors.SchemaError as e:
            logger.error(f'Erro de validação: {e}')
            raise

    def validate_input_path(self, input_path: str) -> str:
        """
        Valida se o caminho do diretório de entrada existe.

        Levanta uma exceção FileNotFoundError se o caminho especificado não existir.

        Parameters:
            input_path : str
                Caminho do diretório a ser validado.

        Returns:
            str
                O mesmo caminho de entrada, se for válido.

        Raises:
            FileNotFoundError
                Se o caminho do diretório não existir.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"O caminho '{input_path}' não existe.")
        return input_path
    
    def read_csv_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um único arquivo CSV em um diretório e retorna um DataFrame.

        Verifica se o caminho de entrada é válido e busca pelo único arquivo CSV no diretório.

        Parameters:
        -----------
        input_path : str
            Caminho do diretório onde o arquivo CSV está localizado.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo CSV.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do diretório ou nenhum arquivo CSV for encontrado.
        """
        ok_input_path = self.validate_input_path(input_path)

        csv_files = glob.glob(os.path.join(ok_input_path, '*.csv'))
        if len(csv_files) != 1:
            raise FileNotFoundError(f"Esperado exatamente um arquivo CSV no diretório '{input_path}', mas encontrou {len(csv_files)}.")
        
        validated_df: pd.DataFrame = pd.read_csv(csv_files[0], encoding='utf-8')
        return self.validate_dataframe(validated_df)

    def read_json_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um único arquivo JSON em um diretório e retorna um DataFrame.

        Verifica se o caminho de entrada é válido e busca pelo único arquivo JSON no diretório.

        Parameters:
        -----------
        input_path : str
            Caminho do diretório onde o arquivo JSON está localizado.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo JSON.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do diretório ou nenhum arquivo JSON for encontrado.
        """
        ok_input_path = self.validate_input_path(input_path)

        json_files = glob.glob(os.path.join(ok_input_path, '*.json'))
        if len(json_files) != 1:
            raise FileNotFoundError(f"Esperado exatamente um arquivo JSON no diretório '{input_path}', mas encontrou {len(json_files)}.")
        
        validated_df: pd.DataFrame = pd.read_json(json_files[0], lines=True, encoding='utf-8')
        return self.validate_dataframe(validated_df)
    
    def read_parquet_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um único arquivo Parquet em um diretório e retorna um DataFrame.

        Verifica se o caminho de entrada é válido e busca pelo único arquivo Parquet no diretório.

        Parameters:
        -----------
        input_path : str
            Caminho do diretório onde o arquivo Parquet está localizado.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo Parquet.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do diretório ou nenhum arquivo Parquet for encontrado.
        """
        ok_input_path = self.validate_input_path(input_path)

        parquet_files = glob.glob(os.path.join(ok_input_path, '*.parquet'))
        if len(parquet_files) != 1:
            raise FileNotFoundError(f"Esperado exatamente um arquivo Parquet no diretório '{input_path}', mas encontrou {len(parquet_files)}.")
        
        validated_df: pd.DataFrame = pd.read_parquet(parquet_files[0])
        return self.validate_dataframe(validated_df)
