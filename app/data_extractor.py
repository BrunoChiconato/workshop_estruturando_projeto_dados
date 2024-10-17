import pandas as pd # type: ignore
import os
import glob

class DataExtractor:
    """
    Classe para extrair dados de diferentes formatos de arquivos, incluindo CSV, JSON e Parquet.

    Esta classe oferece métodos para validar a existência do caminho de entrada
    e para ler dados de arquivos nos formatos suportados, retornando-os como DataFrames do pandas.
    """

    def validate_input_path(self, input_path: str) -> str:
        """
        Valida se o caminho do diretório de entrada existe.

        Levanta uma exceção FileNotFoundError se o caminho especificado não existir.

        Parameters:
        -----------
        input_path : str
            Caminho do diretório a ser validado.

        Returns:
        --------
        str
            O mesmo caminho de entrada, se for válido.

        Raises:
        -------
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
        # Busca o único arquivo CSV no diretório
        csv_files = glob.glob(os.path.join(ok_input_path, '*.csv'))
        if len(csv_files) != 1:
            raise FileNotFoundError(f"Esperado exatamente um arquivo CSV no diretório '{input_path}', mas encontrou {len(csv_files)}.")
        
        return pd.read_csv(csv_files[0])

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
        
        return pd.read_json(json_files[0])
    
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
        
        return pd.read_parquet(parquet_files[0])
