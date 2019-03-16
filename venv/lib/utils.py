
import logging
from os.path import dirname, join
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
##################################################################


def openInputFile(inputFilename):
    # Start with a filepath made from our current directory
    current_dir = dirname(__file__)
    file_path = join(current_dir, inputFilename)
    # The logging article: http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python gave good advice on doing a traceback.
    try:
        return open(file_path)
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logging.error('failed to open file named %s',
                      inputFilename, exc_info=True)
        exit


def makeFilepath(inputFilename):
    current_dir = dirname(__file__)
    return(join(current_dir,inputFilename))
