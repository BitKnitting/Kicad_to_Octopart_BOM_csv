#
# makeBOMCSV.py
#
# The main entry point to making a Bom CSV file that can be fed into the Octopart BoM UI.
#
import logging
logger = logging.getLogger(__name__)
from replaceJellyBeanParts import replaceJellyBeanParts
from makeBOMfile import makeBOMfile
from getParts import getParts
from utils import openInputFile

NUM_PROCESSES = 30  # Maximum number of parallel web-scraping processes.


def makeBOMCSV(outputFrom_bom2csv, jellyBeanFile, numProcesses):
    modifiedBOM2csvFile = replaceJellyBeanParts(
        outputFrom_bom2csv=outputFrom_bom2csv, jellyBeanFile=jellyBeanFile)
    components_by_part_number = getParts(
        modifiedBOM2csvFile=modifiedBOM2csvFile)
    makeBOMfile(components_by_part_number)
###############################################################################
# Main entrypoint.
###############################################################################


def main():
    outputFrom_bom2csv = openInputFile('din_power_atm90e26.xml')
    jellyBeanFile = openInputFile('JBParts.csv')
    makeBOMCSV(outputFrom_bom2csv, jellyBeanFile, NUM_PROCESSES)


if __name__ == '__main__':
    main()
