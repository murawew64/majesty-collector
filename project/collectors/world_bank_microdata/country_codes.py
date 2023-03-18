from project.collectors.base import BaseCollector
from datetime import datetime
from logger import log
import os
import csv
import httpx
from settings import settings
from project.db.base import DBWorker
import numpy as np
import pandas as pd


class CountryCodes(BaseCollector):
    '''
    Origins:
    https://microdata.worldbank.org/api-documentation/catalog/index.html#operation/CatalogSearch
    Collect actual country codes.
    '''

    def __init__(self) -> None:
        self.directory = settings.path_to_data_folder
        self.table_name = 'wb_country_code'

    async def init_tables(self):
        '''
        Create all tables to store data in database.
        '''
        table_sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}
        (
            `countryid` Int32,
            `name`      String,
            `iso`       String
        )
        ENGINE = MergeTree
        ORDER BY countryid
        """

        self.db = DBWorker()
        # SHOW TABLES FROM crude_data
        self.db.create_table('wb_country_code', table_sql)

    def _write_csv_file(self, csv_data, filename):
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(
                file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow(['countryid', 'name', 'iso'])
            for dt in csv_data:
                csv_writer.writerow([dt['countryid'], dt['name'], dt['iso']])

    async def pull(self):
        dt = datetime.now()
        ts = int(dt.timestamp())

        link = f'http://microdata.worldbank.org/index.php/api/catalog/country_codes'
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

            return_data = responce.json()
            if return_data['status'] != 'success':
                log.error(f'Error status {return_data.get("status")}')
                return
            # to push
            self.pull_data = return_data['country_codes']

            # save to csv
            filename = f'{self.directory}/country_codes.csv'
            self._write_csv_file(return_data['country_codes'], filename)

            log.info(f'Create file {filename}')

    async def push(self):
        df = pd.DataFrame(self.pull_data)
        self.db.client.insert_df(table=self.table_name, df=df)

    async def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True
