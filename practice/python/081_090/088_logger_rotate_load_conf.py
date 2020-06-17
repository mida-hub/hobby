import logging
import logging.config

logging.config.fileConfig(fname='conf/logger_rotation.conf')

import time
for _ in range(1000):
    logger = logging.getLogger('samplelogger')
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')

    time.sleep(1)