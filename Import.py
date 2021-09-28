import os


f = open('importNPC.txt', 'r')
w = open('NPCs.py', 'a')


print(f.readline())

for _ in range(25):
    line = f.readline().rstrip('\n')
    description = ''
    name = line
    minDmg = ''
    maxDmg = ''
    hp = ''
    magicka = ''
    weapon = ''
    inventory= ''
    className = name.replace(' ','')
    print('class {}(NPC):\n\tdef __init__(self):\n\t\tsuper().__init__(name=\'{}\', hp=\'{}\', minDmg={}, maxDmg={}, magicka={}, weapon={}, inventory={})\n\n'.format(className, name, hp, minDmg, maxDmg, magicka, weapon, inventory))
   

w.close()



