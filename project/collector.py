from .collectors import KSInflation, RosstatInflation

sources_classes = [KSInflation, RosstatInflation]


def collect_data():
    for source_class in sources_classes:
        source = source_class()
        source.collect()
