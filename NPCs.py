import random as rd
from items import *
class NPC:
    def __init__(self, name, hp, minDmg, maxDmg, magicka, weapon, inventory):
        self.name = name
        self.hp = hp
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.magicka = magicka
        self.weapon = weapon
        self.inventory = inventory
        self.equip()
        
    def __str__(self):
        return "{}\n=====\nHP: {}\nMagicka: {}\nDamage:{}-{}\nWeapon: {}\n".format(self.name, self.hp, self.magicka, self.minDmg, self.maxDmg, self.weapon.name)
        
 
    def is_alive(self):
        return self.hp > 0
    
    def attack(self):
        self.equip()
        eDmg = rd.randint(self.minDmg, self.maxDmg)
        return eDmg
    
    def equip(self):
        self.minDmg, self.maxDmg = self.weapon.minDmg, self.weapon.maxDmg
        
    def describe(self):
        return 'You see an ' + self.name + ' wielding a ' + self.weapon.name + '.'
    
class ImperialGuard(NPC):
    def __init__(self):
        super().__init__(name='Imperial Guard', hp=285, minDmg= 0, maxDmg= 0, magicka=110, weapon= ImperialBroadsword(), inventory= [ImperialBroadsword(), 'Imperial Breastplate', '6 Gold'])
        

