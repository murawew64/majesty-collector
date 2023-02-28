import requests
from .base import BaseCollector
from datetime import datetime
from logger import log
import os


class KSInflation(BaseCollector):

    def __init__(self) -> None:
        self.directory = './data'

    def pull(self):
        ts = int(datetime.now().timestamp())
        link = 'https://cbr.ru/Queries/UniDbQuery/DownloadExcel/132934?Posted=True&From=17.09.2012&To=27.02.2023&FromDate=09%2F17%2F2013&ToDate=02%2F27%2F2023'
        responce = requests.get(link, allow_redirects=True)

        if responce.status_code != 200:
            log.error(f'Status code: {responce.status_code}')
        else:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            with open(f'{self.directory}/ks_inflation_{ts}.xlsx', 'wb') as f:
                f.write(responce.content)

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
