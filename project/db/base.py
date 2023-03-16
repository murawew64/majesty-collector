from settings import settings
from logger import log
import clickhouse_connect


class DBWorker:

    def __init__(self) -> None:
        self.client = clickhouse_connect.get_client(
            host=settings.db_host, username=settings.db_login, password=settings.db_password, database='crude_data')

    def create_table(self, table_name: str, table_sql: str, drop_table=False):
        try:
            if drop_table:
                # Если мне нужно удалить таблицу, то все равно существовала она до этого или нет
                log.debug(f'Drop table {table_name}')
                self.client.command(f'DROP TABLE IF EXISTS {table_name}')
            else:
                # Если удалять таблицу не требуется, тогда не следует создавать таблицу
                if table_name not in self.client.command(f'SHOW TABLES'):
                    log.debug(f'Create table {table_name}')
                else:
                    return

            self.client.command(table_sql)

        except Exception as e:
            log.error(f'Create table error: {e}')

# from clickhouse_driver.connection import Connection
# from clickhouse_driver import Client

#  return 8443 if secure else 8123
# conn = Connection('185.86.144.234', port=8123, database='<DATABASE>', user='<USERNAME>', password='<PASSWORD>')

# http://185.86.144.234:8123/play
# for http use http://185.86.144.234:8123/
