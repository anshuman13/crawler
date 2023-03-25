from os import path, makedirs


class BaseScraper:
    """
    Base class for Scraper
    """

    def __init__(self, root_url: str, index_url: str, export_strategy=None):
        self.root_url = root_url
        self.index_url = self.root_url + index_url
        self.product_list = {}
        self.visited_links = set()
        self._export_strategy = export_strategy
        if not path.exists('results'):
            makedirs('results')

    @property
    def export_strategy(self):
        return self._export_strategy

    @export_strategy.setter
    def export_strategy(self, export_strategy):
        self._export_strategy = export_strategy

    def export(self):
        self._export_strategy.export(self.product_list)
