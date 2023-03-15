from logger import log
from .collectors import KSInflation, RosstatInflation, WorldBankGDP, CountryCodes

sources_classes = [
    KSInflation,
    RosstatInflation,
    WorldBankGDP,
    CountryCodes
]


async def collect_data():
    for source_class in sources_classes:
        source = source_class()
        try:
            await source.collect()
        except Exception as e:
            log.error(
                f'Some exception was ocurred {e}; Class type - {type(source_class)}')
