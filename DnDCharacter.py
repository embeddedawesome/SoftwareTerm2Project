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
    Commom = auto()
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

#Viewing Race
def convert_to_dnd_race(race):
    if isinstance(race, DnDRace):
        return race
    elif isinstance(race, int) and race in DnDRace._value2member_map_:
        return DnDRace(race)
    elif isinstance(race, str) and race.title() in DnDRace._member_names_:
        return DnDRace[race.title()]

    return None

#Viewing Class
def convert_to_dnd_class(classtype):
    if isinstance(classtype, DnDClass):
        return classtype
    elif isinstance(classtype, int) and classtype in DnDClass._value2member_map_:
        return DnDClass(classtype)
    elif isinstance(classtype, str) and classtype.title() in DnDClass._member_names_:
        return DnDClass[classtype.title()]

    return None

#Viewing Background
def convert_to_dnd_background(background):
    if isinstance(background, DnDBackground):
        return background
    elif isinstance(background, int) and background in DnDBackground._value2member_map_:
        return DnDBackground(background)
    elif isinstance(background, str) and background.title().replace(" ", "_") in DnDBackground._member_names_:
        return DnDBackground[background.title().replace(" ", "_")]

    return None

#Viewing Alignment
def convert_to_dnd_alignment(alignment):
    if isinstance(alignment, DnDAlignment):
        return alignment
    elif isinstance(alignment, int) and alignment in DnDAlignment._value2member_map_:
        return DnDAlignment(alignment)
    elif isinstance(alignment, str):
        alignment = alignment.title().replace(" ", "_")
        if alignment in DnDAlignment._member_names_:
            return DnDAlignment[alignment]
        else:
            alignment = alignment.lower()
            match alignment[0]:
                case 'c':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Chaotic_Good
                        case 'n':
                            return DnDAlignment.Chaotic_Neutral
                        case 'e':
                            return DnDAlignment.Chaotic_Evil
                case 't':
                    if alignment[1] == 'n':
                        return DnDAlignment.True_Neutral
                    return
                case 'l':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Lawful_Good
                        case 'n':
                            return DnDAlignment.Lawful_Neutral
                        case 'e':
                            return DnDAlignment.Lawful_Evil
                case 'n':
                    match alignment[1]:
                        case 'g':
                            return DnDAlignment.Neutral_Good
                        case 'n':
                            return DnDAlignment.True_Neutral
                        case 'e':
                            return DnDAlignment.Neutral_Evil
    return None


# Character Core
class DnDCharacter:
    def __init__(
        self, name: str, race: DnDRace, classtype: DnDClass, background, align: DnDAlignment
    ):
        self.name = name
        self.race = None
        self.level = 1
        self.HP = 1
        self.AC = 0
        self.classtype = None
        self.set_class(classtype)
        self.con = 2
        self.background = None
        self.align = align
        self.set_size(race)
        self.set_speed(race)
        self.set_language(race, classtype, background)

    # Delete Character:
    def reset(self):
        self.race = "N/A"
        self.classtype = "N/A"
        self.name = "N/A"
        self.level = "N/A"
        self.HP = "N/A"
        self.AC = "N/A"
        self.con = "N/A"
        self.background = "N/A"
        self.align = "N/A"
        self.size = "N/A"
        self.speed = "N/A"
        self.languages = "N/A"

    # Class Conditions
    def set_class(self, classtype: DnDClass):
        if not isinstance(classtype, DnDClass):
            raise ValueError("Class is not a DnDClass")
        if self.classtype is not None:
            raise ValueError("Can only set class once")
        self.classtype = classtype

        #Barbarian Conditions
        if classtype == DnDClass.Barbarian:
            self.HP = 12
            self.prof_bonus = 2

        elif classtype in [
            DnDClass.Bard,
            DnDClass.Cleric,
            DnDClass.Druid,
            DnDClass.Monk,
            DnDClass.Rogue,
            DnDClass.Warlock,
            DnDClass.Artificer,
        ]:
            self.HP = 8
        elif classtype in [DnDClass.Fighter, DnDClass.Paladin, DnDClass.Ranger]:
            self.HP = 10
        elif classtype in [DnDClass.Sorcerer, DnDClass.Wizard]:
            self.HP = 6
        else:
            self.HP = "N/A"

    #Determining Size
    def set_size(self, race: DnDRace):
        if not isinstance(race, DnDRace):
            raise ValueError("Race is not a DnDRace")
        if self.race is not None:
            raise ValueError("Can only set race once")
        self.race = race
        if race in [
            DnDRace.Dwarf,
            DnDRace.Elf,
            DnDRace.Human,
            DnDRace.Dragonborn,
            DnDRace.Half_Elf,
            DnDRace.Half_Orc,
            DnDRace.Tiefling
        ]:
            self.size = 'Medium'
        elif race in [
            DnDRace.Halfling,
            DnDRace.Gnome
        ]:
            self.size = 'Small'
        else:
            self.size = "N/A"

    #Determining Speed
    def set_speed(self, race: DnDRace):
        if race in [
            DnDRace.Elf,
            DnDRace.Human,
            DnDRace.Dragonborn,
            DnDRace.Half_Elf,
            DnDRace.Half_Orc,
            DnDRace.Tiefling
        ]:
            self.speed = '30ft'
        elif race in [
            DnDRace.Halfling,
            DnDRace.Gnome,
            DnDRace.Dwarf
        ]:
            self.speed = '25ft'
        else:
            self.speed = "N/A"

    #Determining Languages
    def set_language(self, race: DnDRace, classtype: DnDClass, background: DnDBackground):
        if not isinstance(background, DnDBackground):
            raise ValueError("Background is not a DnDBackground")
        if self.background is not None:
            raise ValueError("Can only set background once")
        self.background = background
        self.languages = DnDLanguages.Common
        if race == DnDRace.Tiefling:
            self.languages.appendDnDLanguages.Infernal

    def set_race(self, race: DnDRace):
        match race:
            case DnDRace.Tiefling:
                self.speed = 0
                self.size = 0
            case DnDRace.Half_Orc:
                self.speed = 0
                self.size = 0
            case DnDRace.Half_Elf: