#!/usr/bin/env python

import logging

import technicolor

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(technicolor.ColorisingStreamHandler())

def main():
    log.debug("message at level DEBUG")
    log.info("message at level INFO")
    log.warning("message at level WARNING")
    log.error("message at level ERROR")
    log.critical("message at level CRITICAL")
    log.info("use a function that results in an exception...")
    function_1(a = 1)

@technicolor.log
def function_1(a=None):
    try:
        1/0
    except ZeroDivisionError as e:
        #log.critical("exception: " + str(e), exc_info=True)
        log.critical("exception: " + str(e))
        log.exception("traceback:")
    return False
 
if __name__ == '__main__':
    main()
