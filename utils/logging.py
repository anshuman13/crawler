import logging

from utils import settings


def get_logger():

    logging.basicConfig(
        format="%(asctime)s,%(msecs)03d %(levelname)-8s "
        "[%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
        level=settings.default_log_level,
    )

    return logging.getLogger()
