import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'  # format string is quoted
)

logging.debug('hello, debug')
logging.info('info')
logging.warning('this is a warning message')
logging.critical('critical')
logging.error("error")
