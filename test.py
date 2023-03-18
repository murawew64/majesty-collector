from project.collector import CountryCodes
from project import InitDB
import asyncio


async def main():
    handler = CountryCodes()
    await handler.collect()
    # db = InitDB()
    # db.init_db()


if __name__ == '__main__':
    asyncio.run(main())
