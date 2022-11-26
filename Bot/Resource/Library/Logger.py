import logging

class Logger():
    
    def __init__(self) -> None:
        logger = logging.getLogger('info_example')
        logger.setLevel(logging.INFO)

        # create console handler and set level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter(fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s', datefmt="%Y-%m-%d %H:%M:%S", style='%')

        # add formatter to console_handler
        console_handler.setFormatter(formatter)

        # add console_handler to logger
        logger.addHandler(console_handler)
        
logger = Logger()