from enum import Enum, auto

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


#Character Core
class DnDCharacter():
    def __init__(self, name: str, race: DnDRace, classtype: DnDClass, bg, align: DnDAlignment):
        self.name = name
        self.race = race
        self.level = 1
        self.HP = 1
        self.AC = 0
        self.classtype = classtype
        self.set_class(classtype)
        self.con = 2
        self.bg = bg
        self.align = align

    # Delete Character:
    def reset(self):
        self.race = 'N/A'
        self.classtype = 'N/A'
        self.name = 'N/A'
        self.level = 'N/A'
        self.HP = 'N/A'
        self.AC = 'N/A'
        self.con = 'N/A'
        self.bg = 'N/A'
        self.align = 'N/A'

    #Level 1 Health Calculations
    def set_class(self, classtype):
        if classtype.lower == 'barbarian':
            self.HP = 12
        elif classtype.lower in ['bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock', 'artificer']:
            self.HP = 8
        elif classtype.lower in ['fighter', 'paladin', 'ranger']:
            self.HP = 10
        elif classtype.lower in ['sorcerer', 'wizard']:
            self.HP = 6
        else:
            self.HP = 'N/A'