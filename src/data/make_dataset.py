# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import requests
import json


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    logging.log(msg='Downloading historical price data...', level=logging.INFO)

    res = requests.get('https://api.binance.us/api/v3/klines?symbol=ETHUSD&interval=1s&limit=1000')
    with open(project_dir / 'data/raw/ETH-USD.json', 'w+', encoding='utf-8') as f:
        f.write(res.text)
        f.close()
        logging.log(msg='Download complete.', level=logging.INFO)

    main()
