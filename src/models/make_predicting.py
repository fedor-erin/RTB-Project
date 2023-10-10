import logging
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.pipeline import Pipeline

from utils import save_predictions, load_model


def predict(pipeline: Pipeline,
            test_df: pd.DataFrame,
            logger: logging.Logger) -> np.array:
    """
    Make a prediction for a probability of class=1 and save it
    """
    preds = pipeline.predict_proba(test_df)[:, 1]
    version = datetime.now().strftime('%Y%m%d')
    save_predictions(preds, version, logger)
    return preds


def main():
    """
    Runs predicting for test data, save it
    """
    logger = logging.getLogger(__name__)

    logger.info('Reading processed test data...')
    test_df = pd.read_csv('data/processed/test_df.csv')

    logger.info('Loading model...')
    pipeline = load_model(logger)

    logger.info('Predicting...')
    preds = predict(pipeline, test_df, logger)
    logger.info(f'Mean probability is {preds.mean():.3f}')

    logger.info('Done!')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
