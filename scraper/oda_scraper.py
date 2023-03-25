from scraper.base_scraper import BaseScraper
from concurrent.futures import ThreadPoolExecutor
import bs4
import time
from utils.logging import get_logger
import sys
from utils.request_helper import is_success_response, fetch_link

logger = get_logger()


class OdaScraper(BaseScraper):
    """
    Scraper class for Oda
    """

    def extract(self, soup: bs4.BeautifulSoup) -> None:
        products = soup.findAll('div', {'class': 'product-list-item'})
        for product in products:
            price = product.find("p", {'class': 'price'}).get_text().strip().encode(
                "ascii", errors="ignore").decode()
            name = product.find("div", {'class': 'name-main'}).get_text()
            name_extra = product.find("div", {'class': 'name-extra'}).get_text().strip(
            ).encode(
                "ascii", errors="ignore").decode()
            self.product_list[name] = {"Name Extra": name_extra, "Price": price}

    def extract_link(self, tag: bs4.element.Tag) -> None:
        link = tag.find('a', href=True)
        if link is None or link["href"] in self.visited_links:
            return
        self.visited_links.add(link["href"])
        logger.info("Fetching link : " + link["href"])
        response = fetch_link(self.root_url + link['href'])
        if is_success_response(response):
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            self.extract(soup)
            # h4_tags = soup.findAll('h4', {'class': 'child-category-headline'})
            # for h4_tag in h4_tags:
            #     self.extract_link(h4_tag)

    def scrape(self) -> None:
        logger.info("Fetching Oda data...")
        start_time = time.time() * 1000

        response = fetch_link(self.index_url)
        if not response:
            return
        try:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
        except:
            logger.error("Unable to parse HTML", "{0}".format(sys.exc_info()[0]))
            return

        url_tags = soup.findAll('li', {'class': 'product-category'})

        with ThreadPoolExecutor(4) as executor:
            _ = [executor.submit(self.extract_link, url_tag) for url_tag in url_tags]
        for url_tag in url_tags:
            self.extract_link(url_tag)
        seconds = (time.time() * 1000) - start_time
        logger.info(
            "Done fetching Oda data in {0}ms. .\n".format(format(seconds, '.2f')))

    def export(self):
        super().export()
