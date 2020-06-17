import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs/loggin_instance.log', encoding='utf-8')

s_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

s_formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
f_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

s_handler.setFormatter(s_formatter)
f_handler.setFormatter(f_formatter)

logger.addHandler(s_handler)
logger.addHandler(f_handler)

logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')

a = 10
b = 0
try:
    c = a / b
except Exception as e:
    logger.error(e, exc_info=True) 