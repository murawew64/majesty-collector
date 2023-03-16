from .base import BaseCollector
from datetime import datetime
from logger import log
from settings import settings
import os
import httpx


class WorldBankGDP(BaseCollector):
    '''
    Origins:
    https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators
    '''

    def __init__(self) -> None:
        self.directory = settings.path_to_data_folder

    async def init_tables(self):
        '''
        Create all tables to store data in database.
        '''
        pass

    async def pull(self):
        # async with httpx.AsyncClient() as client:
        #         responce = await client.get(link, follow_redirects=True)
        pass

    async def push(self):
        pass

    async def check_changes(self):
        '''
        True if changes are found else False
        '''
        return True
