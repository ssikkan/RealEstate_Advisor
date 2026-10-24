from pathlib import Path
import pandas as pd

ROOT= Path(__file__).resolve().parent[1]
DATA_PATH= ROOT/"data"/"raw"/"real_estate_data.csv"

def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found at {DATA_PATH}")
    df =pd.read_csv(DATA_PATH)
    return df

if __name__ == "__main__":
    df=load_data()

