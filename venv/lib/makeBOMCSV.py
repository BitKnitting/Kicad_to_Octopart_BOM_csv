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


def makeBOMCSV(outputFrom_bom2csv, jellyBeanFile, numPCBs):
    modifiedBOM2csvFile = replaceJellyBeanParts(
        outputFrom_bom2csv=outputFrom_bom2csv, jellyBeanFile=jellyBeanFile)
    components_by_part_number = getParts(
        modifiedBOM2csvFile=modifiedBOM2csvFile)
    makeBOMfile(components_by_part_number, numPCBs)
###############################################################################
# Main entrypoint.
###############################################################################


def main():
    # Get number of PCBs that you'll be making:
    notAnumber = True
    while (notAnumber):
        userInputPCBs = input("Enter number of PCBs:")
        try:
            numPCBs = int(userInputPCBs)
            notAnumber = False
        except ValueError:
            print('{} is not a number.  Please enter a number.'.format(userInputPCBs))

    # Get which eeschema Bom XML to work with
    inputFilename = input("Enter BoM XML filepath:")
    # openInputFile will exit the app if the file can't be opened.
    outputFrom_bom2csv = openInputFile(inputFilename)
    jellyBeanFile = openInputFile('JBParts.csv')
    makeBOMCSV(outputFrom_bom2csv, jellyBeanFile, numPCBs)


if __name__ == '__main__':
    main()
