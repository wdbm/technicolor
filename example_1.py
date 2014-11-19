import logging
import technicolor as technicolor

def main():

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(technicolor.ColorisingStreamHandler())

    log.debug('message at level DEBUG')
    log.info('message at level INFO')
    log.warning('message at level WARNING')
    log.error('message at level ERROR')
    log.critical('message at level CRITICAL')
 
if __name__ == '__main__':
    main()
