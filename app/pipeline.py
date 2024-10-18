import pandas as pd # type: ignore
from extract import extract_and_consolidate
from transform import transform_data

def main():
    input_path = './data/raw'
    data: pd.DataFrame = extract_and_consolidate(input_path)
    print(transform_data(data))

if __name__ == '__main__':
    main()