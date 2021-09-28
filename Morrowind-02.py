import random as rd
import os
import time
from NPCs import *
from items import *
from enemies import *

list = ['punch', 'kill', 'attack']

def intro():
    dialog = open("intro.txt", "r")
    for _ in range(5):
        print(dialog.readline())
        time.sleep(1)
    NAME = input('Your name is: ')
    print()
    for _ in range(7):
        print(dialog.readline())
        time.sleep(1)        
    print()
    print('<The Prophecy begins. Your actions are now your own>')
    
def choice():
    choice = input('> ')
    choice = choice.lower()
    return choice

def startBoat():
    cmd = choice()
    if cmd in list:
        print('YES')
    else:
        print('NOOOOOO')
        
   
#intro()
startBoat()


