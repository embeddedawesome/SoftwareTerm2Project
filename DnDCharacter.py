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


def convert_to_dnd_race(race):
    if isinstance(race, DnDRace):
        return race
    elif isinstance(race, int) and race in DnDRace._value2member_map_:
        return DnDRace(race)
    elif isinstance(race, str) and race.title() in DnDRace._member_names_:
        return DnDRace[race.title()]

    return None


def convert_to_dnd_class(classtype):
    if isinstance(classtype, DnDClass):
        return classtype
    elif isinstance(classtype, int) and classtype in DnDClass._value2member_map_:
        return DnDClass(classtype)
    elif isinstance(classtype, str) and classtype.title() in DnDClass._member_names_:
        return DnDClass[classtype.title()]

    return None


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
        self, name: str, race: DnDRace, classtype: DnDClass, bg, align: DnDAlignment
    ):
        self.name = name
        self.race = race
        self.level = 1
        self.HP = 1
        self.AC = 0
        self.classtype = None
        self.set_class(classtype)
        self.con = 2
        self.bg = bg
        self.align = align

    # Delete Character:
    def reset(self):
        self.race = "N/A"
        self.classtype = "N/A"
        self.name = "N/A"
        self.level = "N/A"
        self.HP = "N/A"
        self.AC = "N/A"
        self.con = "N/A"
        self.bg = "N/A"
        self.align = "N/A"

    # Level 1 Health Calculations
    def set_class(self, classtype: DnDClass):
        if not isinstance(classtype, DnDClass):
            raise ValueError("Class is not a DnDClass")
        if self.classtype is not None:
            raise ValueError("Can only set class once")
        self.classtype = classtype
        if classtype == DnDClass.Barbarian:
            self.HP = 12
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