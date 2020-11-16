import logging

logger = logging.getLogger('child')

class WapperLogging:
    def __init__(self, file_name):
        self.file_name = file_name

    def common(self, func):
        def wrapper(obj, *args, **kwds):
            logger.info(f'{self.file_name} START {func.__qualname__} args={args} kwds={kwds}')
            rtn = func(obj, *args, **kwds)
            logger.info(f'{self.file_name} END {func.__qualname__} return {rtn}')
            return rtn
        return wrapper
