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
    logger.info('Running a training pipeline ')

    train_df = pd.read_csv('data/processed/train_df.csv')
    logger.info('Train dataframe is read')

    pipeline, metrics = train_pipeline(train_df, logger)
    logger.info(f'{str(pipeline)}')
    logger.info(f'{str(metrics)}')
    logger.info('Pipeline is done')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
