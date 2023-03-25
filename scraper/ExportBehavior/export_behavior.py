from abc import abstractmethod, ABC
from typing import Dict


class ExportBehavior(ABC):
    """
    Defining interface for export functionality of scraped data
    """

    @abstractmethod
    def export(self, data: Dict):
        pass
