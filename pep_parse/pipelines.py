import collections
import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DIR_PATH = BASE_DIR / 'results'


class PepParsePipeline:
    pep_sum = collections.defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        self.pep_sum[status] += 1
        return item

    def close_spider(self, spider):
        DIR_PATH.mkdir(exist_ok=True)
        now = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'status_summary_{now}.csv'
        file_path = DIR_PATH / file_name
        columns = ['Статус,Количество']
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv_writer = csv.writer(f,
                                    dialect='unix')
            total = sum(self.pep_sum.values())
            csv_writer.writerows(
                [columns, *self.pep_sum.items(), ['Total', total]])
