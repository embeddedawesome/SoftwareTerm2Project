from enum import Enum, auto

#Race names
class DnDRace(Enum):
    Dwarf = auto()
    Elf = auto()
    Halfling = auto()
    Human = auto()
    Dragonborn = auto()
    Gnome = auto()
    Half_Elf = auto()
    Half_Orc = auto()
    Tiefling = auto()

#Class Names
class DnDClass(Enum):
    Artificer = auto()
    Barbarian = auto()
    Bard = auto()
    Cleric = auto()
    Druid = auto()
    Fighter = auto()
    Monk = auto()
    Paladin = auto()
    Ranger = auto()
    Rogue = auto()
    Sorcerer = auto()
    Warlock = auto()
    Wizard = auto()

#Background Names
class DnDBackground(Enum):
    Acolyte = auto()
    Charlatan = auto()
    Criminal = auto()
    Entertainer = auto()
    Folk_Hero = auto()
    Guild_Artisan = auto()
    Hermit = auto()
    Noble = auto()
    Outlander = auto()
    Sage = auto()
    Sailor = auto()
    Soldier = auto()
    Urchin = auto()

#Alignment Names
class DnDAlignment(Enum):
    Lawful_Good = auto()
    Neutral_Good = auto()
    Chaotic_Good = auto()
    Lawful_Neutral = auto()
    True_Neutral = auto()
    Chaotic_Neutral = auto()
    Lawful_Evil = auto()
    Neutral_Evil = auto()
    Chaotic_Evil = auto()

#Language Names
class DnDLanguages(Enum):
    Common = auto()
    Dwarvish = auto()
    Elvish = auto()
    Giant = auto()
    Gnomish = auto()
    Goblin = auto()
    Halfling = auto()
    Orc = auto()
    Abyssal = auto()
    Deep_Speech = auto()
    Draconic = auto()
    Infernal = auto()

#Simple Weapons
class DnDSimpleWeapons(Enum):
    Club = auto()
    Dagger = auto()
    Greatclub = auto()
    Handaxe = auto()
    Javelin = auto()
    Light_hammer = auto()
    Mace = auto()
    Quarterstaff = auto()
    Sickle = auto()
    Spear = auto()

#Simple Ranged Weapons
class DnDSimpleRangedWeapons(Enum):
    Light_crossbow = auto()
    Dart = auto()
    Shortbow = auto()
    Sling = auto()

#Martial Weapons
class DnDMartialWeapons(Enum):
    Battleaxe = auto()
    Flail = auto()
    Glaive = auto()
    Greataxe = auto()
    Greatsword = auto()
    Halberd = auto()
    Lance = auto()
    Longsword = auto()
    Maul = auto()
    Morningstar = auto()
    Pike = auto()
    Rapier = auto()
    Scimitar = auto()
    Shortsword = auto()
    Trident = auto()
    War_pick = auto()
    Warhammer = auto()
    Whip = auto()

#Martial Ranged Weapons
class DnDMartialRangedWeapons(Enum):
    Blowgun = auto()
    Heavy_crossbow = auto()
    Hand_crossbow = auto()
    Longbow = auto()
    Net = auto()

class DnDProficiencies(Enum):
    Shields = auto()
    Strength = auto()
    Dexterity = auto()
    Constitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()

class DnDArtisanTools(Enum):
    Alchemist_supplies = auto()
    Brewers_supplies = auto()
    Calligraphers_supplies = auto()
    Carpenters_tools = auto()
    Cartographers_tools = auto()
    Cobblers_tools = auto()
    Cooks_utensils = auto()
    Glassblowers_tools = auto()
    Jewelers_tools = auto()
    Leatherworkers_tools = auto()
    Masons_tools = auto()
    Painters_supplies = auto()
    Potters_tools = auto()
    Smiths_tools = auto()
    Tinkers_tools = auto()
    Weavers_tools = auto()
    Woodcarvers_tools = auto()

class DnDGamingSets(Enum):
    Dice_set = auto()
    Dragonchess_set = auto()
    Playing_card_set = auto()
    Three_Dragon_Ante_set = auto()

class DnDMusicalInstruments(Enum):
    Bagpipes = auto()
    Drum = auto()
    Dulcimer = auto()
    Flute = auto()
    Lute = auto()
    Lyre = auto()
    Horn = auto()
    Pan_flute = auto()
    Shawm = auto()
    Viol = auto()

class DnDMiscTools(Enum):
    Disguise_kit = auto()
    Forgery_kit = auto()
    Herbalism_kit = auto()
    Navigators_tools = auto()
    Poisoners_kit = auto()
    Thieves_tools = auto()

class DnDLightArmour(Enum):
    Padded_armour = auto()
    Leather_armour = auto()
    Studded_leather_armour = auto()

class DnDMediumArmour(Enum):
    Hide_armour = auto()
    Chain_shirt = auto()
    Scale_mail_armour = auto()
    Spiked_armour = auto()
    Breastplate = auto()
    Halfplate = auto()

class DnDHeavyArmour(Enum):
    Ring_mail_armour = auto()
    Chain_mail_armour = auto()
    Splint_armour = auto()
    Plate_armour = auto()

class DnDEquipmentPacks(Enum):
    Burglars_pack = auto()
    Diplomats_pack = auto()
    Dungeoneers_pack = auto()
    Entertainers_pack = auto()
    Explorers_pack = auto()
    Priests_pack = auto()
    Scholars_pack = auto()

class DnDSkills(Enum):
    Acrobatics = auto()
    Animal_handling = auto()
    Arcana = auto()
    Athletics = auto()
    Deception = auto()
    History = auto()
    Insight = auto()
    Intimidation = auto()
    Investigation = auto()
    Medicine = auto()
    Nature = auto()
    Perception = auto()
    Performance = auto()
    Persuasion = auto()
    Religion = auto()
    Sleight_of_hand = auto()
    Stealth = auto()
    Survival = auto()