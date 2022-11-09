import logging

logging.basicConfig(filename="Logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Just an information")