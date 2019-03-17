
# Running
```python3 makeBOMCSV.py```
# Output
The goal is to create a .csv file that can be uploaded to [Octopart's BoM tool](https://octopart.com/?gclid=CjwKCAjwvbLkBRBbEiwAChbckYErg0g5MBmfPbIuRUB2AkxwPabDayXfQrtHbfq3w-aEmAeb_xOHTRoC0g4QAvD_BwE).  [BoMforOctopart.csv](https://github.com/BitKnitting/Kicad_to_Octopart_BOM_csv/blob/master/venv/lib/BoMforOctopart.csv) is an example of the .csv file created from [din_power_atm90e26.xml](https://github.com/BitKnitting/Kicad_to_Octopart_BOM_csv/blob/master/venv/lib/din_power_atm90e26.xml).  
# Inputs
__For this release, the input files are hardcoded.  You will need to change these to fit whatever schematic you're working with__
* __The BoM XML file__ - The main input file is the BoM XML file created __from within eeSchema.__ I highlight this in bold because there is a way to create a BoM within PCBNew.   From previous lives, I have installed different BoM plugins.  I use Bom2csv...because that is what I have used in the past.  This generates a Bom file with the extension .xml. This next step is a bit kludgy... I copy the .xml file into the directory where all the python scripts are located...currently this is the lib directory of this project.
* __The jellybean file__ - The jellybean file (JBParts.csv) holds the relationship between a simple symbol (like C for capacitor + value...say 0.1µ with a manufacturers part number).e.g.:
```
Category,Value,PN,
C,.1u,CC0805KRX7R8BB104,
```
I copied one into the venv directory.  These files are littered all over my hard drive.  I copied the what I believed to be the most recent.
# Inventory
A ways back I had the bright idea to figure out what parts I already had so I didn't order more than needed.  This could be implemented better, but what it does is for the parts that are needed to build the PCB, it creates a file called ```inventory_DoW_Month_Day_Time.csv``` with entries that should be copy/pasted over the entries in ```inventory.csv``` giving the new quantity once the PCBs have used the ones in the list.  The CSV BoM Octopart file will not include parts that are in the inventory.

# Using VS Code
I use VS Code. I hadn't used it for Python before.  I followed the steps in [the python tutorial for VS Code](https://code.visualstudio.com/docs/python/python-tutorial).  Once I had the "hello world" running from the command line, I followed the steps in the post to get debugging working.
* Had the Python extension for VS Code installed.
## venv
* Created a venv right under the ```KICAD_TO_OCTOPART_BOM_CSV``` directory:  ```python3 -m venv venv --prompt kicad_octopart```
* Activate the venv: ```source venv/bin/activate```
* Note: the prompt is now: ```(kicad_octopart) macbook-pro-6:Kicad_to_Octopart_BOM_csv mj$```
* Once all packages were installed, I went back to the command line with the command ```deactivate```.  I then created a requirements.txt file with the command ```pip3 freeze > requirements.txt```.  To recreate the venv, create the venv as discussed above.  Then activate.  Then run the command ```pip3 install -r requirements.txt```

* Started VS Code from the prompt: ```code .```  At this point, the IDE is working within the venv directory.
* Select the Python interpreter to use from the Command Palette (I use F1 to open).  The command is ```Python:Select Interpreter```.  I picked the venv's:  ```./venv/bin/python```
