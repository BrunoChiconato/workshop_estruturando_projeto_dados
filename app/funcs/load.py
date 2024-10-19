import pandas as pd # type: ignore
import os
from decorators.log_decorator import log_decorator

@log_decorator
def load_data(data: pd.DataFrame, output_path: str, output_name: str) -> None:
    """
    Salva um DataFrame em um arquivo CSV no caminho especificado.

    Se o diretório de saída não existir, ele será criado automaticamente.
    
    Parameters:
    ----------
    data : pd.DataFrame
        DataFrame a ser salvo como CSV.
    output_path : str
        Caminho do diretório onde o arquivo CSV será salvo.
    output_name : str, opcional
        Nome do arquivo CSV (padrão: 'vendas_processadas.csv').

    Returns:
    -------
    None
        A função não retorna nenhum valor. O DataFrame é salvo como um arquivo CSV.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file: str = os.path.join(output_path, output_name)
    
    data.to_csv(output_file, index = False)