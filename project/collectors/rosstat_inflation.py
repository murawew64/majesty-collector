import requests
from .base import BaseCollector
from datetime import datetime
from logger import log
import os


class RosstatInflation(BaseCollector):
    '''
    Origins:
    https://rosstat.gov.ru/statistics/price
    Индексы потребительских цен на товары и услуги по Российской Федерации, месяцы (с 1991 г.)
    '''

    def __init__(self) -> None:
        self.directory = './data'

    def pull(self):
        dt = datetime.now()
        ts = int(dt.timestamp())

        # TODO: check ipc_mes-1 is immutable name
        link = f'https://rosstat.gov.ru/storage/mediabank/ipc_mes-1.xlsx'
        try:
            responce = requests.get(link, allow_redirects=True)
        except Exception as e:
            log.error(e)
            return

        if responce.status_code != 200:
            log.error(f'Status code: {responce.status_code}')
        else:
            if not os.path.exists(self.directory):
                log.info(f'Create dir {self.directory}')
                os.makedirs(self.directory)

            file = f'{self.directory}/rosstat_inflation_{ts}.xlsx'
            with open(file, 'wb') as f:
                f.write(responce.content)
            log.info(f'Create file {file}')

    def push(self):
        pass

    def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True


if __name__ == '__main__':
    cl = KSInflation()
    cl.pull()
