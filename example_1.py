#!/usr/bin/env python

import logging
import technicolor

def main():

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(technicolor.ColorisingStreamHandler())

    log.debug("message at level DEBUG")
    log.info("message at level INFO")
    log.warning("message at level WARNING")
    log.error("message at level ERROR")
    log.critical("message at level CRITICAL")

    log.info("using a function...")
    function_1(1, 2, c = 3)
    log.info("using the function again...")
    function_1(2, 3)
    log.info("using the function again, this time via another function...")
    function_2()

# Use a decorator to indicate that the function use should be logged.
@technicolor.log
def function_1(
    a,
    b,
    c = 4,
    d = 5,
    e = 6
    ):
    return(a + b + c + d + e)
 
def function_2():
    return(function_1(1, 3))
 
if __name__ == '__main__':
    main()
