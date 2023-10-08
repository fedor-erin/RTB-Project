import logging
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.pipeline import Pipeline

from utils import save_predictions, load_model


def predict(pipeline: Pipeline, test_df: pd.DataFrame) -> np.array:
    """
    Make a prediction for a probability of class=1 and save it
    """
    preds = pipeline.predict_proba(test_df)[:, 1]
    version = datetime.now().strftime('%Y%m%d')
    save_predictions(preds, version)
    return preds


def main():
    """
    Runs predicting for test data, save it
    """
    logger = logging.getLogger(__name__)
    logger.info('Running predicting for test data')

    test_df = pd.read_csv('data/processed/test_df.csv')
    logger.info('Test dataframe is read')

    pipeline = load_model()
    logger.info('Model is loaded')

    preds = predict(pipeline, test_df)
    logger.info(f'Predictions are made and saved. Mean probability is {preds.mean():.3f}')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
