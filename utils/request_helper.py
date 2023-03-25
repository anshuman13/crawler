from ratelimiter import RateLimiter
import requests

from utils import settings
from utils.logging import get_logger

logger = get_logger()


@RateLimiter(max_calls=20, period=1)
def fetch_link(link):
    response = None
    try:
        response = requests.get(link, headers=settings.headers)
    except requests.exceptions.ConnectionError as ce:
        logger.info("Failed to connect to '{0}'".format(link), "{0}".format(ce))
    return response


def is_success_response(response):
    if response and response.status_code != 200:
        return False
    return True
