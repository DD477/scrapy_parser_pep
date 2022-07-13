from collections import defaultdict
import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
COLUMNS = ['Статус,Количество']


class PepParsePipeline:
    def __init__(self):
        self.pep_sum = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        dir_path = BASE_DIR / 'results'
        dir_path.mkdir(exist_ok=True)
        now = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now}.csv'
        file_path = dir_path / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv_writer = csv.writer(f,
                                    dialect='unix')
            total = sum(self.pep_sum.values())
            csv_writer.writerows(
                [COLUMNS, *self.pep_sum.items(), ['Total', total]])
