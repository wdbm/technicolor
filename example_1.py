import logging
import technicolor as technicolor

def main():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(technicolor.ColorisingStreamHandler())

    logger.debug('message at level DEBUG')
    logger.info('message at level INFO')
    logger.warning('message at level WARNING')
    logger.error('message at level ERROR')
    logger.critical('message at level CRITICAL')
 
if __name__ == '__main__':
    main()