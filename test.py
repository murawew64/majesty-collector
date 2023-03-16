from project.collector import CountryCodes
from project import InitDB


def main():
    # handler = CountryCodes()
    # handler.collect()
    db = InitDB()
    db.init_db()


if __name__ == '__main__':
    main()
