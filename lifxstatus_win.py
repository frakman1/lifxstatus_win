import lazylights
import time
import os
import sys
import math
import binascii
from colour import Color
import pyautogui 
from colorama import Fore
import subprocess

import time

#screenshots take about 3~4 seconds to process. This will add to the period 
PERIOD = 5                    # how often to poll

#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address.
def createBulb(ip, macString, port = 56700):
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------

#Set your bulbs' real MAC addresses and IP addresses here:
myBulb1 = createBulb('192.168.1.XX','XX:XX:XX:XX:XX:XX')  
myBulb2 = createBulb('192.168.1.XX','XX:XX:XX:XX:XX:XX')  

#lazylights requires a 'set' of bulbs as input
bulbs1=[myBulb1,myBulb2]
c = Color("white")

while True:
    print "---------------------------------------------------------------------------------------------------------"
    print (time.strftime("%m/%d/%Y at %H:%M:%S"))
    try:
        lazylights.set_state(bulbs1,c.hue*360,(c.saturation),1,3500,(3000),False)

    except Exception as e:
        print "Ignoring error:"
        print str(e)
        continue
    
    time.sleep(PERIOD)  
#------------------------------------------------------------------------------------------------------------    
    try:
        iconFound = pyautogui.locateOnScreen('C:\\Python27\\lifxaway\\busy.png') 
        if (iconFound):
            print Fore.RED + "FOUND BUSY ICON. CODE RED!"
            c = Color("red")
            continue
    except Exception as e:
        print "Ignoring error:"
        print str(e)
        continue
#------------------------------------------------------------------------------------------------------------        
    try:
        iconFound = pyautogui.locateOnScreen('C:\\Python27\\lifxaway\\available.png') 
        if (iconFound):
            print Fore.RED + "FOUND AVAILABLE ICON. GREEN SHEEN!"
            c = Color("green")
            continue
    except Exception as e:
        print "Ignoring error:"
        print str(e)
        continue
#------------------------------------------------------------------------------------------------------------
        
    try:
        iconFound = pyautogui.locateOnScreen('C:\\Python27\\lifxaway\\away.png') 
        if (iconFound):
            print Fore.RED + "FOUND AWAY ICON. MELLOW YELLOW!"
            c = Color("yellow")
            continue
    except Exception as e:
        print "Ignoring error:"
        print str(e)
        continue
#------------------------------------------------------------------------------------------------------------        
        
 
    