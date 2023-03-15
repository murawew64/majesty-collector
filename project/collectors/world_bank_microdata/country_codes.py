import requests
from ..base import BaseCollector
from datetime import datetime
from logger import log
import os
import csv


class CountryCodes(BaseCollector):
    '''
    Origins:
    https://microdata.worldbank.org/api-documentation/catalog/index.html#operation/CatalogSearch
    Collect actual country codes.
    '''

    def __init__(self) -> None:
        self.directory = './data'

    def _write_csv_file(self, csv_data):
        with open(f'{self.directory}/country_codes.csv', mode='w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(
                file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow(['countryid', 'name', 'iso'])
            for dt in csv_data:
                csv_writer.writerow([dt['countryid'], dt['name'], dt['iso']])

    def pull(self):
        dt = datetime.now()
        ts = int(dt.timestamp())

        link = f'http://microdata.worldbank.org/index.php/api/catalog/country_codes'
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

            return_data = responce.json()
            if return_data['status'] != 'success':
                log.error(f'Error status {return_data.get("status")}')
                return

            self._write_csv_file(return_data['country_codes'])

            log.info(f'Create file {"Output file"}')

    def push(self):
        pass

    def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True
