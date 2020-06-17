import logging
import logging.config
import yaml

with open('conf/logger.yaml', mode='r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('sampleLogger')

logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')