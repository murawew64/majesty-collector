import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(pathname)s %(lineno)d - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
