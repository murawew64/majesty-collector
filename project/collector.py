from .collectors import KSInflation, RosstatInflation, WorldBankGDP

sources_classes = [KSInflation, RosstatInflation, WorldBankGDP]


def collect_data():
    for source_class in sources_classes:
        source = source_class()
        source.collect()
