import pandas as pd


def load(path: str):
    """Loading a CSV file to a DataFrame"""
    try:
        data = pd.read_csv(path)
        print(f'Loading dataset of dimensions {data.shape}')

        return data
    except Exception as e:
        print(e)
        return None
