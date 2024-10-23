import pandas as pd  # type: ignore

from decorators.decorators import log_decorator, time_decorador
from funcs.extract import extract_and_consolidate
from funcs.load import load_data
from funcs.transform import transform_data


@time_decorador
@log_decorator
def main():
    input_path: str = './data/raw'

    data: pd.DataFrame = extract_and_consolidate(input_path)
    transformed_data: pd.DataFrame = transform_data(data)
    load_data(transformed_data)

if __name__ == '__main__':
    main()