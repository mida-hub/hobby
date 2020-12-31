import logging
import logging.config
import test_logging

def main():
    # main 処理なので、__name__ には、root が入る
    logging.config.fileConfig('conf/logger.conf')
    logger = logging.getLogger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    test_logging.do_something()

if __name__ == '__main__':
    main()
