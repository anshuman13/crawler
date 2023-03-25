import json
import argparse

from scraper.ExportBehavior.export_to_csv import ExportToCsv
from scraper.oda_scraper import OdaScraper
from utils.logging import get_logger
import time

logger = get_logger()


def parse_args():
    parser = argparse.ArgumentParser("Scraper Help function")
    parser.add_argument('--config-file', nargs=1,
                        help="Config file for the scraper",
                        default="sample_config.json",
                        type=argparse.FileType('r'))
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    config = json.load(args.config_file[0])
    start_time = time.time() * 1000

    oda_scraper = OdaScraper(root_url=config["root_url"], index_url=config["index_url"],
                             export_strategy=ExportToCsv())
    oda_scraper.scrape()
    oda_scraper.export()

    seconds = (time.time() * 1000) - start_time
    logger.info("Scraper finished in {0}ms.\n".format(format(seconds, '.2f')))
    logger.debug("Debug logs")


if __name__ == '__main__':
    main()
