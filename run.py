import asyncio
from project import collect_data


def main():
    # TODO: Add Cron job
    asyncio.run(collect_data())


if __name__ == '__main__':
    main()
