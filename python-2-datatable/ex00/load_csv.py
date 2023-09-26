import pandas as pd


def load(path: str) -> pd.DataFrame:
    """function to load dataset"""
    try:
        dataset = pd.read_csv(path)
        num_rows, num_cols = dataset.shape
        print("Loading dataset of dimensions",
              f"({num_rows}, {num_cols})")
        return dataset
    except FileNotFoundError:
        print("Error: File not found")
    except pd.errors.EmptyDataError:
        print("Error: Empty file")
    except Exception as e:
        print(f"Error: {str(e)}")
    return None
