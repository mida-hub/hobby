import logging
import logging.config

logging.config.fileConfig(fname='conf/logger.conf')

logger = logging.getLogger('samplelogger')
logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')