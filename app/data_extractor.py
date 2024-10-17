import pandas as pd # type: ignore
import os

class DataExtractor:
    """
    Classe para extrair dados de diferentes formatos de arquivos, incluindo CSV, JSON e Parquet.

    Esta classe oferece métodos para validar a existência do caminho de entrada
    e para ler dados de arquivos nos formatos suportados, retornando-os como DataFrames do pandas.
    """

    def validate_input_path(self, input_path: str) -> str:
        """
        Valida se o caminho do arquivo de entrada existe.

        Levanta uma exceção FileNotFoundError se o caminho especificado não existir.

        Parameters:
        -----------
        input_path : str
            Caminho do arquivo de entrada a ser validado.

        Returns:
        --------
        str
            O mesmo caminho de entrada, se for válido.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do arquivo de entrada não existir.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"O caminho '{input_path}' não existe.")
        return input_path
    
    def read_csv_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um arquivo CSV e retorna um DataFrame.

        Verifica se o caminho de entrada é válido antes de ler o arquivo.

        Parameters:
        -----------
        input_path : str
            Caminho do arquivo CSV a ser lido.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo CSV.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do arquivo de entrada não existir.
        """
        ok_input_path = self.validate_input_path(input_path)
        return pd.read_csv(ok_input_path)

    def read_json_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um arquivo JSON e retorna um DataFrame.

        Verifica se o caminho de entrada é válido antes de ler o arquivo.

        Parameters:
        -----------
        input_path : str
            Caminho do arquivo JSON a ser lido.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo JSON.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do arquivo de entrada não existir.
        """
        ok_input_path = self.validate_input_path(input_path)
        return pd.read_json(ok_input_path)
    
    def read_parquet_data(self, input_path: str) -> pd.DataFrame:
        """
        Lê dados de um arquivo Parquet e retorna um DataFrame.

        Verifica se o caminho de entrada é válido antes de ler o arquivo.

        Parameters:
        -----------
        input_path : str
            Caminho do arquivo Parquet a ser lido.

        Returns:
        --------
        pd.DataFrame
            DataFrame contendo os dados do arquivo Parquet.

        Raises:
        -------
        FileNotFoundError
            Se o caminho do arquivo de entrada não existir.
        """
        ok_input_path = self.validate_input_path(input_path)
        return pd.read_parquet(ok_input_path)