import logging
import logging.config
import yaml

with open('conf/logger_rotation.yaml', mode='r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

import time
for _ in range(1000):
    logger = logging.getLogger('samplelogger')
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')

    time.sleep(1)