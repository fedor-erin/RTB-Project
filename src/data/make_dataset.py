import click
import logging

from src.data.preprocessing import read_data, process_raw, save_df


@click.command()
@click.argument('mode')
def main(mode):
    """
    Runs data processing scripts to turn raw data from (../raw) into cleaned data (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Making a dataset from raw data')

    if mode == 'train':
        file_name = 'training_data'
    elif mode == 'test':
        file_name = 'test_data'
    else:
        raise Exception(f'Wrong mode={mode}! Should be train or test.')

    df = read_data(f'data/raw/{file_name}.csv.gz')
    logger.info('Raw data is read')

    df = process_raw(df, mode)
    logger.info('Raw data is processed')

    save_df(df, mode)
    logger.info('Processed data is saved')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
