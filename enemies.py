import random as rd
class Enemy:
    def __init__(self, name, hp, minDmg, maxDmg):
        self.name = name
        self.hp = hp
        self.minDmg = minDmg
        self.maxDmg = maxDmg
 
    def is_alive(self):
        return self.hp > 0
    
    def attack(self):
        eDmg = rd.randint(self.minDmg, self.maxDmg)
        return eDmg
    
class Alit(Enemy):
    def __init__(self):
        super().__init__(name='Alit', hp=30, minDmg=1, maxDmg=9)
        
class Alit_Diseased(Enemy):
    def __init__(self):
        super().__init__(name='Diseased Alit', hp=30, minDmg=1, maxDmg=9)

class Alit_Blighted(Enemy):
    def __init__(self):
        super().__init__(name='Blighted Alit', hp=105, minDmg=7, maxDmg=21)
        
class Cliff_Racer(Enemy):
    def __init__(self):
        super().__init__(name='Cliff Racer', hp=45, minDmg=3, maxDmg=8)
        
class Cliff_Racer_Diseased(Enemy):
    def __init__(self):
        super().__init__(name='Diseased Cliff Racer', hp=45, minDmg=3, maxDmg=8)
        
class Cliff_Racer_Blighted(Enemy):
    def __init__(self):
        super().__init__(name='Blighted Cliff Racer', hp=90, minDmg=6, maxDmg=18)
        
class Dreugh(Enemy):
    def __init__(self):
        super().__init__(name='Dreugh', hp=60, minDmg=5, maxDmg=15)
        
class Dreugh_Warlord(Enemy):
    def __init__(self):
        super().__init__(name='Dreugh Warlord', hp=200, minDmg=1, maxDmg=10)
        
class Guar(Enemy):
    def __init__(self):
        super().__init__(name='Guar', hp=38, minDmg=1, maxDmg=9)
        
class Guar_Wild(Enemy):
    def __init__(self):
        super().__init__(name='Wild Guar', hp=38, minDmg=1, maxDmg=9)
        
class Guar_Pack(Enemy):
    def __init__(self):
        super().__init__(name='Pack Guar', hp=38, minDmg=1, maxDmg=9)
        
class Guar_Corky(Enemy):
    def __init__(self):
        super().__init__(name='Corky', hp=38, minDmg=3, maxDmg=9)
        
class Guar_Tarvyn(Enemy):
    def __init__(self):
        super().__init__(name="Tarvyn's Guar", hp=38, minDmg=3, maxDmg=9)
        
class Guar_Rollie(Enemy):
    def __init__(self):
        super().__init__(name="Rollie the Guar", hp=38, minDmg=10, maxDmg=25)
        
class Guar_White(Enemy):
    def __init__(self):
        super().__init__(name="The White Guar", hp=38, minDmg=10, maxDmg=25)
                
class Kagouti(Enemy):
    def __init__(self):
        super().__init__(name='Kagouti', hp=45, minDmg=4, maxDmg=12)

class Kagouti_Mating(Enemy):
    def __init__(self):
        super().__init__(name='Mating Kagouti', hp=45, minDmg=5, maxDmg=15)
        
class Kagouti_Diseased(Enemy):
    def __init__(self):
        super().__init__(name='Diseased Kagouti', hp=45, minDmg=4, maxDmg=12)
        
class Kagouti_Blighted(Enemy):
    def __init__(self):
        super().__init__(name='Blighted Kagouti', hp=45, minDmg=8, maxDmg=24)
    
class MudCrab(Enemy):
    def __init__(self):
        super().__init__(name="Mudcrab", hp=15, minDmg=1, maxDmg=5)
        
class MudCrab_Diseased(Enemy):
    def __init__(self):
        super().__init__(name="Diseased Mudcrab", hp=15, minDmg=1, maxDmg=5)
        
class Netch(Enemy):
    def __init__(self):
        super().__init__(name='Netch', hp=45, minDmg=1, maxDmg=20)
        
class Netch_Giant_Bull(Enemy):
    def __init__(self):
        super().__init__(name='Giant Bull Netch', hp=250, minDmg=8, maxDmg=25)

class Nix_Hound(Enemy):
    def __init__(self):
        super().__init__(name='Nix-Hound', hp=23, minDmg=1, maxDmg=6)
        
class Nix_Hound_Blighted(Enemy):
    def __init__(self):
        super().__init__(name='Blighted Nix-Hound', hp=68, minDmg=6, maxDmg=18)

class Rat(Enemy):
    def __init__(self):
        super().__init__(name='Rat', hp=23, minDmg=1, maxDmg=2)
        
class Rat_Cave(Enemy):
    def __init__(self):
        super().__init__(name='Cave Rat', hp=23, minDmg=1, maxDmg=10)
        
class Rat_Sewer(Enemy):
    def __init__(self):
        super().__init__(name='Telvanni Sewer Rat', hp=23, minDmg=1, maxDmg=6)
        
class Rat_Diseased(Enemy):
    def __init__(self):
        super().__init__(name='Diseased Rat', hp=23, minDmg=2, maxDmg=6)

class Shalk(Enemy):
    def __init__(self):
        super().__init__(name='Shalk', hp=38, minDmg=6, maxDmg=18)

class Shalk_Diseased(Enemy):
    def __init__(self):
        super().__init__(name='Diseased Shalk', hp=38, minDmg=6, maxDmg=18)
        
class Shalk_Blighted(Enemy):
    def __init__(self):
        super().__init__(name='Blighted Shalk', hp=80, minDmg=10, maxDmg=30)

class SlaughterFish(Enemy):
    def __init__(self):
        super().__init__(name='Slaughterfish', hp=15, minDmg=1, maxDmg=5)
        
class SlaughterFish_Small(Enemy):
    def __init__(self):
        super().__init__(name='small Slaughterfish', hp=23, minDmg=1, maxDmg=6)
        
class SlaughterFish_OldBlueFin(Enemy):
    def __init__(self):
        super().__init__(name='Old Blue Fin', hp=68, minDmg=1, maxDmg=25)
        




