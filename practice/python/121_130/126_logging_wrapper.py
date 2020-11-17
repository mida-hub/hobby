import logging
import logging.config
import datetime

logging.config.fileConfig('conf/logger_wapper.conf')
logger = logging.getLogger(__name__)

from wrapper_logging import WrapperLogging

wrapper_logging = WrapperLogging(__file__)

class Hoge:
    @wrapper_logging.common
    def add(self, x, y):
        return x + y

    @wrapper_logging.common
    def main(self):
        calc = self.add(1, 2)
        return calc

def main():
    # main 処理なので、__name__ には、root が入る
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    hoge = Hoge()
    hoge.main()

if __name__ == '__main__':
    main()
