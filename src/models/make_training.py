from src.models.pipeline import train_pipeline

import logging
import pandas as pd

import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings('ignore', category=ConvergenceWarning)


def main():
    """
    Runs training pipeline, save model, perform cross validation, report metrics
    """
    logger = logging.getLogger(__name__)

    logger.info('Reading processed train data...')
    train_df = pd.read_csv('data/processed/train_df.csv')

    logger.info('Starting training pipeline...')
    pipeline, metrics = train_pipeline(train_df, logger)

    logger.info('Pipeline info:')
    logger.info(f'{str(pipeline)}')
    logger.info('Report info:')
    logger.info(f'{str(metrics)}')

    logger.info('Done!')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
