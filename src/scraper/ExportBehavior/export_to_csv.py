from typing import Dict

from scraper.ExportBehavior.export_behavior import ExportBehavior
from datetime import datetime
import pandas as pd


class ExportToCsv(ExportBehavior):
    """
    Save data: format csv.
    Used by: Oda
    """

    def export(self, data: Dict) -> None:
        current_time = datetime.now()
        current_timestamp = current_time.now().strftime('%y-%m-%d %H:%M:%S')
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.reset_index().rename(columns={'index': 'Name'})
        df.to_csv(f"results/results_{current_timestamp}.csv", index=False)
