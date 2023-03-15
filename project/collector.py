import asyncio
from logger import log
from .collectors import KSInflation, RosstatInflation, WorldBankGDP, CountryCodes

sources_classes = [
    KSInflation,
    RosstatInflation,
    WorldBankGDP,
    CountryCodes
]


async def collect_data():
    tasks = []
    for source_class in sources_classes:
        source = source_class()
        # asyncio..ensure_future work too
        tasks.append(asyncio.create_task(source.collect()))

    try:
        responses = await asyncio.gather(*tasks)
    except Exception as e:
        log.error(
            f'Some exception was ocurred {e};')
