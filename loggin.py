import logging
import logging.config
import helper
import traceback

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:S')
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('THis is a warning message')
#logging.error('This is an error message')
#logging.critical('THis is a critical message')


logger = logging.getLogger(__name__)

# Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("This is an error")

#logging.config.fileConfig("logging.conf")
#logger = logging.getLogger("simpleExample")
#logger.debug("This is a debug message")


try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as err:
    logging.error(err, exc_info=True)


try:
    b = [4, 5, 6]
    val = a[7]
except:
    logging.error("The error is %s", traceback.format_exc())




