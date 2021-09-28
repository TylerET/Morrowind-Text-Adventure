class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin made of gold.",
                         value=self.amt)
	
#########
#Weapons#
#########
class Weapon(Item):
    def __init__(self, name, description, value, minDmg, maxDmg, weight):
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.weight = weight
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}-{}\nWeight: {}".format(self.name, self.description, self.value, self.minDmg, self.maxDmg, self.weight)
    
#########
#Default#
#########

class BareHands(Weapon):
    def __init__(self):
        super().__init__(name="Bare Hands",
                         description="Sometimes all you need is your bare hands.",
                         value=0,
                         minDmg=1, maxDmg=2, weight=0)
	
class BareClaws(Weapon):
    def __init__(self):
        super().__init__(name="Bare Claws",
                         description="Sometimes all you need is your claws.",
                         value=0,
                         minDmg=2, maxDmg=5, weight=0)
 
###################
#One-handed Swords#
###################

class ImperialBroadsword(Weapon):
    def __init__(self):
        super().__init__(name="Imperial Broadsword",
                         description="A steel broadsword used by the Imperial Legion.",
                         value=60,
                         minDmg=6, maxDmg=12, weight=12.0)

class IronSaber(Weapon):
    def __init__(self):
        super().__init__(name="Iron Saber",
                         description="An iron saber with some rust.",
                         value=24,
                         minDmg=5, maxDmg=18, weight=15.0)
        
class IronBroadsword(Weapon):
    def __init__(self):
        super().__init__(name="Iron Broadsword",
                         description="An iron broadsword",
                         value=30,
                         minDmg=4, maxDmg=12, weight=12.0)

class IronLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Iron Longsword",
                         description="An iron longsword",
                         value=40,
                         minDmg=4, maxDmg=16, weight=20.0)

class SteelSaber(Weapon):
    def __init__(self):
        super().__init__(name="Steel Saber",
                         description="A steel saber",
                         value=48,
                         minDmg=5, maxDmg=20, weight=15.0)
        
class SteelBroadsword(Weapon):
    def __init__(self):
        super().__init__(name="Steel Broadsword",
                         description="A steel broadsword",
                         value=60,
                         minDmg=4, maxDmg=14, weight=12.0)
        
class SteelLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Steel Longsword",
                         description="A steel longsword",
                         value=80,
                         minDmg=4, maxDmg=18, weight=20.0)
        
class NordicBroadsword(Weapon):
    def __init__(self):
        super().__init__(name="Nordic Broadsword",
                         description="A nordic broadsword",
                         value=95,
                         minDmg=6, maxDmg=18, weight=15.0)
        
class SteelKatana(Weapon):
    def __init__(self):
        super().__init__(name="Steel Katana",
                         description="A steel Katana",
                         value=100,
                         minDmg=3, maxDmg=20, weight=18.0)

class SilverLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Silver Longsword",
                         description="A silver longsword",
                         value=160,
                         minDmg=1, maxDmg=20, weight=16.0)
        
class GlassLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Glass Longsword",
                         description="A longsword made of glass",
                         value=16000,
                         minDmg=4, maxDmg=30, weight=12.0)

class EbonyBroadsword(Weapon):
    def __init__(self):
        super().__init__(name="Ebony Broadsword",
                         description="An ebony broadsword",
                         value=15000,
                         minDmg=4, maxDmg=26, weight=24.0)
        
class EbonyLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Ebony Longsword",
                         description="An ebony longsword",
                         value=20000,
                         minDmg=1, maxDmg=37, weight=40.0)
        
class DaedricLongsword(Weapon):
    def __init__(self):
        super().__init__(name="Daedric Longsword",
                         description="A daedric longsword",
                         value=40000,
                         minDmg=2, maxDmg=44, weight=60.0)
        
class DaedricKatana(Weapon):
    def __init__(self):
        super().__init__(name="Daedric Katana",
                         description="A daedric katana",
                         value=50000,
                         minDmg=3, maxDmg=44, weight=54.0)
###################
#One-handed Axes#
###################
	
class ChitinWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Chitin War Axe', description='', value=19, minDmg=1, maxDmg=11, weight=12.0)

class IronWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Iron War Axe', description='', value=30, minDmg=1, maxDmg=18, weight=24.0)

class SteelWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Steel War Axe', description='', value=60, minDmg=1, maxDmg=18, weight=24.0)

class SteelWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Steel War Axe', description='', value=60, minDmg=1, maxDmg=20, weight=24.0)

class SilverWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Silver War Axe', description='', value=120, minDmg=1, maxDmg=20, weight=19.2)

class DwarvenWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven War Axe', description='', value=450, minDmg=1, maxDmg=24, weight=24.0)

class GlassWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Glass War Axe', description='', value=12000, minDmg=1, maxDmg=33, weight=14.4)

class EbonyWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Ebony War Axe', description='', value=15000, minDmg=1, maxDmg=37, weight=48.0)

class DaedricWarAxe(Weapon):
	def __init__(self):
		super().__init__(name='Daedric War Axe', description='', value=30000, minDmg=1, maxDmg=44, weight=72.0)
		
###################
#Two-handed Axes#
###################

class MinersPick(Weapon):
	def __init__(self):
		super().__init__(name="Miner's Pick", description='', value=8, minDmg=3, maxDmg=7, weight=20.0)

class IronBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Iron Battle Axe', description='', value=50, minDmg=1, maxDmg=32, weight=30.0)

class NordicBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Nordic Battle Axe', description='', value=60, minDmg=1, maxDmg=30, weight=30.0)

class SteelBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Steel Battle Axe', description='', value=100, minDmg=1, maxDmg=36, weight=30.0)

class DwarvenBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Battle Axe', description='', value=750, minDmg=1, maxDmg=35, weight=30.0)

class OrcishBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Orcish Battle Axe', description='', value=2000, minDmg=17, maxDmg=28, weight=15.0)

class DaedricBattleAxe(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Battle Axe', description='', value=50000, minDmg=1, maxDmg=80, weight=90.0)
		
##################
#One-handed Blunt#
##################

class ChitinClub(Weapon):
	def __init__(self):
		super().__init__(name='Chitin Club', description='', value=6, minDmg=3, maxDmg=3, weight=6.0)

class IronClub(Weapon):
	def __init__(self):
		super().__init__(name='Iron Club', description='', value=10, minDmg=4, maxDmg=5, weight=12.0)

class SteelClub(Weapon):
	def __init__(self):
		super().__init__(name='Steel Club', description='', value=20, minDmg=4, maxDmg=5, weight=12.0)

class SpikedClub(Weapon):
	def __init__(self):
		super().__init__(name='Spiked Club', description='', value=18, minDmg=4, maxDmg=5, weight=12.0)

class DreughClub(Weapon):
	def __init__(self):
		super().__init__(name='Dreugh Club', description='', value=200, minDmg=7, maxDmg=8, weight=10.8)

class DaedricClub(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Club', description='', value=10000, minDmg=10, maxDmg=12, weight=36.0)

class IronMace(Weapon):
	def __init__(self):
		super().__init__(name='Iron Mace', description='', value=24, minDmg=1, maxDmg=12, weight=15.0)

class SteelMace(Weapon):
	def __init__(self):
		super().__init__(name='Steel Mace', description='', value=48, minDmg=3, maxDmg=14, weight=15.0)

class DwarvenMace(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Mace', description='', value=60, minDmg=5, maxDmg=17, weight=15.0)

class EbonyMace(Weapon):
	def __init__(self):
		super().__init__(name='Ebony Mace', description='', value=12000, minDmg=7, maxDmg=26, weight=30.0)

class DaedricMace(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Mace', description='', value=24000, minDmg=3, maxDmg=30, weight=45.0)

##################
#Two-handed Blunt#
##################

class IronWarhammer(Weapon):
	def __init__(self):
		super().__init__(name='Iron Warhammer', description='', value=40, minDmg=1, maxDmg=28, weight=32)

class SteelWarhammer(Weapon):
	def __init__(self):
		super().__init__(name='Steel Warhammer', description='', value=80, minDmg=1, maxDmg=32, weight=32)

class DwarvenWarhammer(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Warhammer', description='', value=600, minDmg=1, maxDmg=39, weight=32)

#class OrcWarhammer(Weapon):
	#def __init__(self):
		#super().__init__(name='Orc Warhammer', description=' ', value=1,600, minDmg=1, maxDmg=42, weight=38.4)

class SixthHouseBellHammer(Weapon):
	def __init__(self):
		super().__init__(name='Sixth House Bell Hammer', description='', value=5000, minDmg=1, maxDmg=50, weight=75)

class DaedricWarhammer(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Warhammer', description='', value=30000, minDmg=1, maxDmg=70, weight=96)

########
#Staves#
########

class WoodenStaff(Weapon):
	def __init__(self):
		super().__init__(name='Wooden Staff', description='', value=8, minDmg=3, maxDmg=6, weight=8)

class SteelStaff(Weapon):
	def __init__(self):
		super().__init__(name='Steel Staff', description='', value=28, minDmg=3, maxDmg=7, weight=8)

class SilverStaff(Weapon):
	def __init__(self):
		super().__init__(name='Silver Staff', description='', value=56, minDmg=3, maxDmg=7, weight=6.4)

class DreughStaff(Weapon):
	def __init__(self):
		super().__init__(name='Dreugh Staff', description='', value=400, minDmg=3, maxDmg=10, weight=7.2)

class GlassStaff(Weapon):
	def __init__(self):
		super().__init__(name='Glass Staff', description='', value=5600, minDmg=3, maxDmg=12, weight=4.8)

class EbonyStaff(Weapon):
	def __init__(self):
		super().__init__(name='Ebony Staff', description='', value=7000, minDmg=3, maxDmg=16, weight=16)

class DaedricStaff(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Staff', description='', value=14000, minDmg=3, maxDmg=16, weight=24)

#########
#Daggers#
#########

class IronFork(Weapon):
	def __init__(self):
		super().__init__(name='Iron Fork', description='', value=1, minDmg=3, maxDmg=5, weight=1)

class ChitinDagger(Weapon):
	def __init__(self):
		super().__init__(name='Chitin Dagger', description='', value=6, minDmg=4, maxDmg=4, weight=1.5)

class IronDagger(Weapon):
	def __init__(self):
		super().__init__(name='Iron Dagger', description='A small dagger with some rust.', value=10, minDmg=5, maxDmg=5, weight=3)

class ChitinShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Chitin Shortsword', description='', value=13, minDmg=4, maxDmg=9, weight=4)

class IronTanto(Weapon):
	def __init__(self):
		super().__init__(name='Iron Tanto', description='', value=14, minDmg=6, maxDmg=6, weight=4)

class SteelDagger(Weapon):
	def __init__(self):
		super().__init__(name='Steel Dagger', description='', value=20, minDmg=5, maxDmg=5, weight=3)

class IronShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Iron Shortsword', description='', value=20, minDmg=7, maxDmg=11, weight=8)

class IronWakizashi(Weapon):
	def __init__(self):
		super().__init__(name='Iron Wakizashi', description='', value=24, minDmg=7, maxDmg=12, weight=10)

class SteelTanto(Weapon):
	def __init__(self):
		super().__init__(name='Steel Tanto', description='', value=28, minDmg=6, maxDmg=11, weight=4)

class ImperialShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Imperial Shortsword', description='', value=30, minDmg=6, maxDmg=10, weight=9)

class SilverDagger(Weapon):
	def __init__(self):
		super().__init__(name='Silver Dagger', description='', value=40, minDmg=5, maxDmg=5, weight=2.4)

class SteelShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Steel Shortsword', description='', value=40, minDmg=7, maxDmg=12, weight=8)

class SteelWakizashi(Weapon):
	def __init__(self):
		super().__init__(name='Steel Wakizashi', description='', value=48, minDmg=7, maxDmg=12, weight=10)

class SilverShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Silver Shortsword', description='', value=80, minDmg=7, maxDmg=10, weight=6)

class DwarvenShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Shortsword', description='', value=300, minDmg=8, maxDmg=15, weight=8)

class GlassDagger(Weapon):
	def __init__(self):
		super().__init__(name='Glass Dagger', description='', value=4000, minDmg=6, maxDmg=15, weight=1.8)

class DaedricDagger(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Dagger', description='', value=10000, minDmg=8, maxDmg=12, weight=9)

class EbonyShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Ebony Shortsword', description='', value=10000, minDmg=12, maxDmg=25, weight=16)

class DaedricTanto(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Tanto', description='', value=14000, minDmg=9, maxDmg=20, weight=12)

class DaedricShortsword(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Shortsword', description='', value=20000, minDmg=10, maxDmg=26, weight=24)

class DaedricWakizashi(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Wakizashi', description='', value=48000, minDmg=10, maxDmg=30, weight=30)

###################
#Two-handed Swords#
###################

class IronClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Iron Claymore', description='', value=80, minDmg=1, maxDmg=24, weight=27)

class SteelClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Steel Claymore', description='', value=160, minDmg=1, maxDmg=27, weight=27)

class NordicClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Nordic Claymore', description='', value=180, minDmg=1, maxDmg=30, weight=30)

class SteelDai(Weapon):
	def __init__(self):
		super().__init__(name='Steel Dai', description='', value=20, minDmg=240, maxDmg=1, weight=katana)

class SilverClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Silver Claymore', description='', value=320, minDmg=1, maxDmg=27, weight=21.6)

class DwarvenClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Claymore', description='', value=1200, minDmg=1, maxDmg=33, weight=27)

class GlassClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Glass Claymore', description='', value=32000, minDmg=1, maxDmg=45, weight=16.2)

class DaedricClaymore(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Claymore', description='', value=80000, minDmg=1, maxDmg=60, weight=81)

class DaedricDai(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Dai', description='', value=60, minDmg=120000, maxDmg=1, weight=katana)


########
#Spears#
########


class ChitinSpear(Weapon):
	def __init__(self):
		super().__init__(name='Chitin Spear', description='', value=13, minDmg=5, maxDmg=13, weight=7)

class IronSpear(Weapon):
	def __init__(self):
		super().__init__(name='Iron Spear', description='', value=20, minDmg=6, maxDmg=15, weight=14)

class IronSpear(Weapon):
	def __init__(self):
		super().__init__(name='Iron Spear', description='', value=20, minDmg=5, maxDmg=20, weight=14)

class SteelSpear(Weapon):
	def __init__(self):
		super().__init__(name='Steel Spear', description='', value=40, minDmg=6, maxDmg=17, weight=14)

class IronHalberd(Weapon):
	def __init__(self):
		super().__init__(name='Iron Halberd', description='', value=40, minDmg=5, maxDmg=20, weight=14)

class SteelHalberd(Weapon):
	def __init__(self):
		super().__init__(name='Steel Halberd', description='', value=80, minDmg=5, maxDmg=23, weight=14)

class SilverSpear(Weapon):
	def __init__(self):
		super().__init__(name='Silver Spear', description='', value=80, minDmg=5, maxDmg=23, weight=11.2)

class DwarvenSpear(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Spear', description='', value=300, minDmg=5, maxDmg=21, weight=14)

class DwarvenHalberd(Weapon):
	def __init__(self):
		super().__init__(name='Dwarven Halberd', description='', value=600, minDmg=5, maxDmg=28, weight=24)

class EbonySpear(Weapon):
	def __init__(self):
		super().__init__(name='Ebony Spear', description='', value=10000, minDmg=5, maxDmg=32, weight=28)

class GlassHalberd(Weapon):
	def __init__(self):
		super().__init__(name='Glass Halberd', description='', value=16000, minDmg=5, maxDmg=38, weight=8.4)

class DaedricSpear(Weapon):
	def __init__(self):
		super().__init__(name='Daedric Spear', description='', value=20000, minDmg=6, maxDmg=40, weight=42)

