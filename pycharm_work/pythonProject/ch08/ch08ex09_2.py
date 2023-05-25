import logging
import logging.handlers

deb_logger = logging.getLogger('deb_log')
deb_logger.setLevel(logging.DEBUG)

file = "log.log"
size = 1024
count = 10
lfh = logging.handlers.RotatingFileHandler(filename=file, maxBytes=size, backupCount=count)
lfh.setLevel(logging.DEBUG)

deb_logger.addHandler(lfh)

for i in range(100):
    deb_logger.debug("deb log mess - file")