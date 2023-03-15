from .base import BaseCollector
from datetime import datetime
from logger import log
import os
import httpx
from settings import settings


class KSInflation(BaseCollector):
    '''
    Origins:
    https://cbr.ru/hd_base/infl/
    '''

    def __init__(self) -> None:
        self.directory = settings.path_to_data_folder

    async def pull(self):
        dt = datetime.now()
        ts = int(dt.timestamp())
        dt_date = dt.strftime("%d.%m.%Y")
        day, month, year = dt_date.split('.')

        link = f'https://cbr.ru/Queries/UniDbQuery/DownloadExcel/132934?Posted=True&From=17.09.2013&\
            To={dt_date}&FromDate=09%2F17%2F2013&ToDate={month}%2F{day}%2F{year}'
        try:
            async with httpx.AsyncClient() as client:
                responce = await client.get(link, follow_redirects=True)
        except Exception as e:
            log.error(e)
            return

        if responce.status_code != 200:
            log.error(f'Status code: {responce.status_code}')
        else:
            if not os.path.exists(self.directory):
                log.info(f'Create dir {self.directory}')
                os.makedirs(self.directory)

            file = f'{self.directory}/ks_inflation_{ts}.xlsx'
            with open(file, 'wb') as f:
                f.write(responce.content)
            log.info(f'Create file {file}')

    async def push(self):
        pass

    async def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True
