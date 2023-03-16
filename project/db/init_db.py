from settings import settings
import clickhouse_connect
from logger import log


class InitDB:
    db_list = ['crude_data', 'proc_data', 'res_data']

    def __init__(self) -> None:
        self.db_client = clickhouse_connect.get_client(
            host=settings.db_host, username=settings.db_admin_login, password=settings.db_admin_password)

    def init_db(self):
        # --- CREATE DATABASES ---
        responce = self.db_client.command('SHOW DATABASES')
        exists_db = responce.split()

        for db_name in InitDB.db_list:
            if db_name not in exists_db:
                # DROP DATABASE IF EXISTS temporary_db
                log.info(f'Create database:\n {db_name}')
                self.db_client.command(
                    f"CREATE DATABASE IF NOT EXISTS {db_name} ENGINE = Memory COMMENT 'a database with crude data'")

        responce = self.db_client.command('SHOW DATABASES')
        log.info(f'Exists database: {responce}')

        # --- CREATE USER WITH DB ACCESS ---
        # create a standart user with access to InitDB.db_list databases
        self.db_client.command(
            f"CREATE USER OR REPLACE {settings.db_login} IDENTIFIED WITH plaintext_password BY '{settings.db_password}'")
        for db_name in InitDB.db_list:
            self.db_client.command(
                f'GRANT ALL ON {db_name}.* TO {settings.db_login} WITH GRANT OPTION')
