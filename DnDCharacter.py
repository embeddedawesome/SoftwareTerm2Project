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
        self.race = race
        self.level = 1
        self.HP = 1
        self.AC = 0
        self.languages = []
        self.proficiencies = []
        self.classtype = None
        self.set_class(classtype)
        self.con = 2
        self.background = background
        self.align = align
        self.set_race(race)

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
        self.proficiencies = "N/A"

    # Class Conditions
    def set_class(self, classtype: DnDClass):
        if not isinstance(classtype, DnDClass):
            raise ValueError("Class is not a DnDClass")
        if self.classtype is not None:
            raise ValueError("Can only set class once")
        self.classtype = classtype
        match classtype:

            #Barbarian Conditions
            case DnDClass.Barbarian:
                self.HP = 12
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                #Shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialWeapons)
                self.proficiencies.append(DnDProficiencies.Strength)
                self.proficiencies.append(DnDProficiencies.Constitution)
                #choose 2 from list

                #choice1 = input('Would you like a greataxe or a different martial melee weapon? ')
                #if choice1 == 'greataxe':
                #   self.weapons.append(DnDMartialWeapons.Greataxe)
                #elif choice1 == 'different martial melee weapon':
                #    self.weapons.append(DnDMartialWeapons.(input('Which weapon? '))

            #Bard Conditions
            case DnDClass.Bard:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialRangedWeapons.Hand_crossbow)
                self.proficiencies.append(DnDMartialWeapons.Longsword)
                self.proficiencies.append(DnDMartialWeapons.Rapier)
                self.proficiencies.append(DnDMartialWeapons.Shortsword)
                #3 musical instruments of your choice
                self.proficiencies.append(DnDProficiencies.Dexterity)
                self.proficiencies.append(DnDProficiencies.Charisma)
                #any 3 skills

            #Cleric Conditions
            case DnDClass.Cleric:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                #shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDProficiencies.Wisdom)
                self.proficiencies.append(DnDProficiencies.Charisma)
                #2 skills from list

            #Druid Conditions
            case DnDClass.Druid:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                #shields (no armour made of metal)
                self.proficiencies.append(DnDSimpleWeapons.Club)
                self.proficiencies.append(DnDSimpleWeapons.Dagger)
                self.proficiencies.append(DnDSimpleRangedWeapons.Dart)
                self.proficiencies.append(DnDSimpleWeapons.Javelin)
                self.proficiencies.append(DnDSimpleWeapons.Mace)
                self.proficiencies.append(DnDSimpleWeapons.Quarterstaff)
                self.proficiencies.append(DnDMartialWeapons.Scimitar)
                self.proficiencies.append(DnDSimpleWeapons.Sickle)
                self.proficiencies.append(DnDSimpleRangedWeapons.Sling)
                self.proficiencies.append(DnDSimpleWeapons.Spear)
                self.proficiencies.append(DnDMiscTools.Herbalism_kit)
                self.proficiencies.append(DnDProficiencies.Intelligence)
                self.proficiencies.append(DnDProficiencies.Wisdom)
                #2 skills from list

            #Monk Conditions
            case DnDClass.Monk:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialWeapons.Shortsword)
                #1 artisan tool or musical instrument
                self.proficiencies.append(DnDProficiencies.Strength)
                self.proficiencies.append(DnDProficiencies.Dexterity)
                #2 skills from list

            #Rogue Conditions
            case DnDClass.Rogue:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialRangedWeapons.Hand_crossbow)
                self.proficiencies.append(DnDMartialWeapons.Longsword)
                self.proficiencies.append(DnDMartialWeapons.Rapier)
                self.proficiencies.append(DnDMartialWeapons.Shortsword)
                self.proficiencies.append(DnDMiscTools.Thieves_tools)
                self.proficiencies.append(DnDProficiencies.Dexterity)
                self.proficiencies.append(DnDProficiencies.Intelligence)
                #4 skills from list

            #Warlock Conditions
            case DnDClass.Warlock:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDProficiencies.Wisdom)
                self.proficiencies.append(DnDProficiencies.Charisma)
                #2 skills from list

            #Artificer Conditions
            case DnDClass.Artificer:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                #Shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMiscTools.Thieves_tools)
                self.proficiencies.append(DnDArtisanTools.Tinkers_tools)
                #One type of artisan tool
                self.proficiencies.append(DnDProficiencies.Constitution)
                self.proficiencies.append(DnDProficiencies.Intelligence)
                #Choose 2 skills from list

            #Fighter Conditions
            case DnDClass.Fighter:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                self.proficiencies.append(DnDHeavyArmour)
                #Shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialWeapons)
                self.proficiencies.append(DnDProficiencies.Strength)
                self.proficiencies.append(DnDProficiencies.Constitution)
                #2 skills from list

            #Paladin Conditions
            case DnDClass.Paladin:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                self.proficiencies.append(DnDHeavyArmour)
                #Shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialWeapons)
                self.proficiencies.append(DnDProficiencies.Wisdom)
                self.proficiencies.append(DnDProficiencies.Charisma)
                #2 skills from list

            #Ranger Conditions
            case DnDClass.Ranger:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies.append(DnDLightArmour)
                self.proficiencies.append(DnDMediumArmour)
                #shields
                self.proficiencies.append(DnDSimpleWeapons)
                self.proficiencies.append(DnDMartialWeapons)
                self.proficiencies.append(DnDProficiencies.Strength)
                self.proficiencies.append(DnDProficiencies.Dexterity)
                #3 skills from list

            #Sorcerer Conditions
            case DnDClass.Sorcerer:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies.append(DnDSimpleWeapons.Dagger)
                self.proficiencies.append(DnDSimpleRangedWeapons.Dart)
                self.proficiencies.append(DnDSimpleRangedWeapons.Sling)
                self.proficiencies.append(DnDSimpleWeapons.Quarterstaff)
                self.proficiencies.append(DnDSimpleRangedWeapons.Light_crossbow)
                self.proficiencies.append(DnDProficiencies.Constitution)
                self.proficiencies.append(DnDProficiencies.Charisma)
                #2 skills from list

            #Wizard Conditions
            case DnDClass.Wizard:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies.append(DnDSimpleWeapons.Dagger)
                self.proficiencies.append(DnDSimpleRangedWeapons.Dart)
                self.proficiencies.append(DnDSimpleRangedWeapons.Sling)
                self.proficiencies.append(DnDSimpleWeapons.Quarterstaff)
                self.proficiencies.append(DnDSimpleRangedWeapons.Light_crossbow)
                self.proficiencies.append(DnDProficiencies.Intelligence)
                self.proficiencies.append(DnDProficiencies.Wisdom)
                #2 skills from list

    #Race Conditions
    def set_race(self, race: DnDRace):
        match race:

            #Tiefling Conditions
            case DnDRace.Tiefling:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Infernal)

            #Half Orc Conditions
            case DnDRace.Half_Orc:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Orc)

            #Half Elf Conditions
            case DnDRace.Half_Elf:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Elvish)

            #Dragonborn Conditions
            case DnDRace.Dragonborn:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Draconic)

            #Dwarf Conditions
            case DnDRace.Dwarf:
                self.speed = '25ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Dwarvish)

            #Elf Conditions
            case DnDRace.Elf:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Elvish)

            #Gnome Conditions
            case DnDRace.Gnome:
                self.speed = '25ft'
                self.size = 'Small'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Gnomish)

            #Halfling Conditions
            case DnDRace.Halfling:
                self.speed = '25ft'
                self.size = 'Small'
                self.languages.append(DnDLanguages.Common)
                self.languages.append(DnDLanguages.Halfling)

            #Human Conditions
            case DnDRace.Human:
                self.speed = '30ft'
                self.size = 'Medium'
                self.languages.append(DnDLanguages.Common)