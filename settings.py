import configparser

config = configparser.ConfigParser()
config.read('.env')


class settings:
    path_to_data_folder = config['DEFAULT']['PATH_TO_DATA_FOLDER']
    db_host = config['DEFAULT']['DB_HOST']
    db_login = config['DEFAULT']['DB_LOGIN']
    db_password = config['DEFAULT']['DB_PASSWORD']
