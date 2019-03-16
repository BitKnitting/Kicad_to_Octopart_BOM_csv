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


def makeBOMCSV(outputFrom_bom2csv, jellyBeanFile, numProcesses):
    modifiedBOM2csvFile = replaceJellyBeanParts(
        outputFrom_bom2csv=outputFrom_bom2csv, jellyBeanFile=jellyBeanFile)
    components_by_part_number = getParts(
        modifiedBOM2csvFile=modifiedBOM2csvFile)
    makeBOMfile(components_by_part_number)
