import logging
from datetime import datetime


def changeLevel():
    """
    default is warning
    """
    logging.basicConfig(level=logging.INFO)


def writeOnFile():
    logging.basicConfig(filename="mylog.txt", level=logging.INFO)


def writeOnFileWithFormat(logger):
    _fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
    _formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
    _fh.setFormatter(_formatter)
    logger.addHandler(_fh)


def printLog():
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')


def withLogger():
    log = logging.getLogger(__name__)
    log.debug("with logger")


if __name__ == '__main__':
    printLog()
    withLogger()
