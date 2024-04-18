import xml.etree.ElementTree as ET
import os
import time
import art
art.tprint('HACK PENTAGON')
tree = ET.parse('start-config.xml')
root = tree.getroot()
print('starting hack, please wait...')
time.sleep(8)
os.system('python3 hack.py')
