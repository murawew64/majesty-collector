from settings import settings
# from clickhouse_driver.connection import Connection
# from clickhouse_driver import Client

import clickhouse_connect
client = clickhouse_connect.get_client(
    host=settings.db_host, username=settings.db_login, password=settings.db_password)


responce = client.command('SHOW DATABASES')
print(responce)

#  return 8443 if secure else 8123
# conn = Connection('185.86.144.234', port=8123, database='<DATABASE>', user='<USERNAME>', password='<PASSWORD>')

# http://185.86.144.234:8123/play
# for http use http://185.86.144.234:8123/
