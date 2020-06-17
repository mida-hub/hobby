"""
    ログの出力デフォルトのログレベルはwarning
    critical:重大なエラー
    error:エラー
    warning:警告
    info:情報
    debug:デバッグ情報
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs/sample.log',
                    filemode='w',
                    format='%(asctime)s-%(process)s-%(levelname)s-%(message)s'
                    )
logging.debug('debug log')
logging.info('info log')
logging.warning('warning log')
logging.error('error log')
logging.critical('critical log')

user = 'Taro'
logging.error(f'{user} raised error')

a = 10
b = 0
try:
    c = a / b
except Exception as e:
    logging.error(e, exc_info=True)