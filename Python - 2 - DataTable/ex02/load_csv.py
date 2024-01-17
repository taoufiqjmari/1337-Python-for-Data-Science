import pandas as pd


def load(path: str):
    # Read the data using pandas
    data = pd.read_csv(path)
    print(f'Loading dataset of dimensions {data.shape}')

    return data
