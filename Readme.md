
# Using VS Code
I use VS Code. I hadn't used it for Python before.  I followed the steps in [the python tutorial for VS Code](https://code.visualstudio.com/docs/python/python-tutorial).  Once I had the "hello world" running from the command line, I followed the steps in the post to get debugging working.
* Had the Python extension for VS Code installed.
* Created a venv right under the ```KICAD_TO_OCTOPART_BOM_CSV``` directory:  ```python3 -m venv venv --prompt kicad_octopart```
* Activate the venv: ```source venv/bin/activate```
* Note: the prompt is now: ```(kicad_octopart) macbook-pro-6:Kicad_to_Octopart_BOM_csv mj$```
* Started VS Code from the prompt: ```code .```  At this point, the IDE is working within the venv directory.
* Select the Python interpreter to use from the Command Palette (I use F1 to open).  The command is ```Python:Select Interpreter```.  I picked the venv's:  ```./venv/bin/python```
# Inputs
* __The BoM XML file__ - The main input file is the BoM XML file created from within eeSchema. From previous lives, I have installed different BoM plugins.  I use Bom2csv...because that is what I have used in the past.  This generates a Bom file with the extension .xml.  I copy this file into the directory where all the python scripts are located...because it seems easier (if not the laziest).
* __The jellybean file__ - The jellybean file (JBParts.csv) holds the relationship between a simple symbol (like C for capacitor + value...say 0.1µ with a manufacturers part number).e.g.:
```
Category,Value,PN,
C,.1u,CC0805KRX7R8BB104,
```
I copied one into the venv directory.  These files are littered all over my hard drive.  I copied the largest
