import pandas as pd # type: ignore
from funcs.extract import extract_and_consolidate
from funcs.transform import transform_data
from funcs.load import load_data
from decorators.decorators import log_decorator, time_decorador

@time_decorador
@log_decorator
def main():
    input_path: str = './data/raw'
    output_path: str = './data/processed'
    output_name: str = 'vendas_processadas.csv'

    data: pd.DataFrame = extract_and_consolidate(input_path)
    transformed_data: pd.DataFrame = transform_data(data)
    load_data(transformed_data, output_path, output_name)

if __name__ == '__main__':
    main()