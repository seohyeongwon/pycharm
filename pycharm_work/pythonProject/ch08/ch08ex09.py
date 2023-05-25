import logging

logging.basicConfig(level=logging.DEBUG)

deb_logger = logging.getLogger('deb_log')
deb_logger.setLevel(logging.DEBUG)

lfh = logging.FileHandler('debug.log')
lfh.setLevel(logging.DEBUG)

deb_logger.addHandler(lfh)

logging.debug("deb log mess - con")
deb_logger.debug("deb log mess - file")