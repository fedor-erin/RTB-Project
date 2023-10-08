import pandas as pd

from src.config import CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET

def read_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(
        file_path,
        sep=';',
        header=0,
        compression='gzip',
        parse_dates=['timestamp', 'lastStart']
    )

def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Feature generation
    """
    # add diff in hours between the event and last any campaign start
    data = df.copy()
    data['fromLastStart'] = (data['timestamp'] - data['lastStart']).apply(lambda x: x.total_seconds() / 3600)
    return data

def process_raw(df: pd.DataFrame,
                mode: str = 'train') -> pd.DataFrame:
    """
    Preprocess a raw data into a dataset
    """
    # feature generation
    df = generate_features(df)

    # handling NaNs
    df[CATEGORICAL_FEATURES] = df[CATEGORICAL_FEATURES].fillna(value='Unknown')
    df[NUMERICAL_FEATURES] = df[NUMERICAL_FEATURES].fillna(value=-1)

    # resulting columns
    columns = CATEGORICAL_FEATURES + NUMERICAL_FEATURES
    if mode == 'train':
        columns += [TARGET]

    return df[columns]

def save_df(df: pd.DataFrame,
            mode: str = 'train') -> None:
    """
    Save processed data
    """
    df_path = f'data/processed/{mode}_df.csv'
    df.to_csv(df_path, index=False)
