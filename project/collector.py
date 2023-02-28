from .collectors import KSInflation

sources_classes = [KSInflation]


def collect_data():
    for source_class in sources_classes:
        source = source_class()
        source.collect()
