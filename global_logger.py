# Defines a global logging object `logger` for use by all modules in this app.
import logging
import sys
from os import path, mkdir

basedir = path.abspath(path.dirname(__file__))
is_local = 'pycharm' in basedir.lower()
# is_local = True

# Initialize logging
log_level = logging.DEBUG
if is_local:
    log_dir = './logs'
    if not path.exists(log_dir):
        mkdir(log_dir)

    log_file = f'{log_dir}/checkin.log'

    logging.basicConfig(filename=log_file,
                        level=log_level,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='w',
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

else:
    logging.basicConfig(stream=sys.stdout,
                        level=log_level,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)

logger.info("\n=======================================")
logger.info(f"Global logging initialized!  Level: {logger.getEffectiveLevel()}")
logger.info(f"local = {is_local}")
