import logging
import technicolor
import example_2_module

def main():

    verbose = True

    global log
    log = logging.getLogger(__name__)
    logging.root.addHandler(technicolor.ColorisingStreamHandler())

    # logging level
    if verbose:
        logging.root.setLevel(logging.DEBUG)
    else:
        logging.root.setLevel(logging.INFO)

    log.info("example INFO message in main")
    log.debug("example DEBUG message in main")
    
    example_2_module.function1()
 
if __name__ == '__main__':
    main()
