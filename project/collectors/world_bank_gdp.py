import requests
from .base import BaseCollector
from datetime import datetime
from logger import log
import os


class WorldBankGDP(BaseCollector):
    '''
    Origins:
    https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators
    '''

    def __init__(self) -> None:
        self.directory = './data'

    def pull(self):
        pass

    def push(self):
        pass

    def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True
