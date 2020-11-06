import logging


def do_something():
    logger = logging.getLogger(__name__)
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
