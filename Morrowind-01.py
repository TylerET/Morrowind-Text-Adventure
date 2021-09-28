import random as rd
import time

def DP(): #Dialog Pause
    time.sleep(0.2)
    
def getName():
    global NAME
    print('????: \"Wake up, we\'re here. Why are you shaking? Are you ok? Wake up.\"')
    DP()
    print('<You wake up on the floor of a boat, in a small store room.>')
    print('<Before you stands a scarred Dark Elf.>')
    DP()
    print('Jiub: \"Stand up...\"')
    DP()
    print('Jiub: \"there you go. You were dreaming. What\'s your name?\"\n')
    DP()
    NAME = input('Your Name: ')
    DP()
    print('\nJiub: \"Well, not even last night\'s storm could wake you ' 
          + NAME + '.')
    print('Jiub: I heard them say we\'ve reached Morrowind, I\'m sure they\'ll let us go.\"')
    DP()
    print('<You hear the sound of footsteps outside the room.>')
    DP()
    print('Jiub: \"Quiet, here comes the guard.\"')
    time.sleep(.5)
    print('<An armored Imperial guard enters the store room.>')
    time.sleep(.5)
    print('Guard: \"This is where you get off, come with me.\"')
    DP()
    print('<With a wave of his hand, the guard turns and exits the store room.>')
    time.sleep(1)
    startBoat()

def startBoat():
    print('\n<The Prophecy begins. Your actions are now your own.>')
    DP()
    progress = False
    while progress == False:
        cmd = input('<What do you do?>: ')
        if 'follow' in cmd:
            print('<You follow the guard though the gallery of the ship.>')
            DP()
            print('<The ship\'s gallery is dimly lit, with only a few cots and barrels to adorn it.>')
            progress = True
       
        elif 'punch' in cmd or 'Punch' in cmd or 'attack' in cmd or 'Attack' in cmd or 'kill' in cmd  or 'Kill' in cmd:
            if 'Jiub' in cmd or 'jiub' in cmd:
                print('<You strike Jiub.>')
                DP()
                print('<Jiub falls backwards, his neck landing on the edge of a barrel.>')
                DP()
                print('<You have cursed the world with Cliff Racers forever.>')
                progress = True
            elif 'guard' in cmd or 'Guard' in cmd:
                print('<You attack the guard.>')
                DP()
                print('<Before you can land a punch, the guard thrust his sword into your abdomen.>')
                DP()
                print('<You have died.>')
                progress = True
            else:
                cmd = input('Who do you want to attack?: ')
                if 'Jiub' in cmd or 'jiub' in cmd:
                    print('<You strike Jiub>')
                    DP()
                    print('<Jiub falls backwards, his neck landing on the edge of a barrel>')
                    DP()
                    print('<You have cursed the world with Cliff Racers forever.>')
                    progress = True
                elif 'guard' in cmd or 'Guard' in cmd:
                    print('<You attack the guard.>')
                    DP()
                    print('<Before you can land a punch, the guard thrust his sword into your abdomen.>')
                    DP()
                    print('<You have died.>')
                    progress = True
                else:
                    print('I don\'t understand that command.')
                    DP()
        else:
            print('I don\'t understand that command.')
            DP()
            
            
            
    
        

    

    
getName()





