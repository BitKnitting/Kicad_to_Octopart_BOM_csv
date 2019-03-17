
import string
import re
import csv
import logging
import time
from utils import makeFilepath
logger = logging.getLogger(__name__)


def makeBOMfile(parts):
    def getInventoryInfo(part):
        # Prepare the inventory file.
        inventoryFile = makeFilepath("inventory.csv")
        with open(inventoryFile, newline='', encoding='utf-8') as csvfile:
            # DictReader does NOT return a dict object, rather a list of
            # dicts.
            inventoryRows = csv.DictReader(csvfile)
            for row in inventoryRows:
                if (row['Manf#'] == part):
                    # argh..there are chars w/ high values...so...get to
                    # bytes encoded as ascii..then decode to str....
                    descBytes = row['Description'].encode('ascii', 'ignore')
                    descStr = descBytes.decode('utf-8')
                    return(int(row['Quantity']), descStr)
        return -1, ''  # part not found

    # Open the BoM output file for writing.  If there is at least one row of BoM data, the file will be written.  Info messages are printed for those rows that
    # can't be resolved from scraping Digikey.
    fileName = makeFilepath("BoMforOctopart.csv")
    with open(fileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        write_header(csvwriter)
        # Components is an array of components that share the same part number. Sharing the same part number means
        # the value is the same. For example:
        # part_number = CL21F104ZBCNNNC
        # components = [{'ref': 'C3', 'value': '.1u'}, {'ref': 'C1', 'value': '.1u'}]
        #
        # Python 3 does not have iteritems()...so using items()
        #
        # Open an inventory csv file that has the updated number of parts in inventory after this order.
        # The name will be inventory-<today's date and time>.csv
        #
        #
        # MAKE THESE NUMBER OF PCBs
        #
        numPCBs = 25
        trans = str.maketrans(' :', '_-')
        newInventoryFilename = makeFilepath('inventory_' +
                                            time.asctime().translate(trans)+'.csv')
        print(newInventoryFilename)
        with open(newInventoryFilename, 'w', newline='') as csv_file:
            newInventoryCSV = csv.writer(csv_file, delimiter=',')
            newInventoryCSV.writerow(('Manf#', 'Quantity', 'Description'))
            for part_number, components in parts.items():
                if part_number != 'None':
                    # Get the quantity we have in inventory.  If -1 is returned, there is no
                    # row for this part number.
                    # logStr = 'Writing part number: {} with value: {}'.format(part_number,components[0]['value'])
                    quantityNeed = len(components) * numPCBs
                    print('part: ', part_number, ' quantity: ', quantityNeed)
                    quantityHave, description = getInventoryInfo(
                        part_number)
                    if (quantityHave < 0):
                        logger.info(
                            'Part number: {} is not listed in the inventory file.'.format(part_number))
                        # put the number of components figured out from the Kicad xml bom tool.
                        write_row(csvwriter, part_number,
                                  quantityNeed, components, '')
                    elif (quantityHave-quantityNeed >= 0):
                        logger.info('Part number: {} have {} on hand, need {}. '.format(
                            part_number, quantityHave, quantityNeed))
                        # skip writing out to Octopart BoM file because don't need to order.
                        # subtract the quantity used and put new quantity in new inventory csv.
                        s = '****' if quantityHave - \
                            quantityNeed == 0 else str(quantityHave-quantityNeed)
                        newInventoryCSV.writerow(
                            (str(part_number), s, description))
                    else:
                        quantityOrder = abs(quantityHave-quantityNeed)
                        logger.info('Need to order {} more of part number: {}'.format(
                            quantityOrder, part_number))
                        write_row(csvwriter, part_number,
                                  quantityOrder, components, description)
                        # Not sure how many ordered so make it obvious where need to edit...
                        newInventoryCSV.writerow(
                            (str(part_number), '****', description))
                else:
                    print('Skipping part number: {} '.format(
                        part_number))
####################################################################################


def write_header(csvwriter):
    csvwriter.writerow(('Manf Part #', 'Quantity', 'Reference', 'Description'))


def write_row(csvwriter, part_number, quantity, components, description):
    refs = []
    for component in components:
        refs.append(component['ref'])
    refStr = ",".join(refs)
    csvwriter.writerow((str(part_number), str(quantity), refStr, description))
