from DnDData import *

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
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDSimpleWeapons, DnDMartialWeapons, DnDProficiencies.Strength, DnDProficiencies.Constitution)
                #Shields
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
                self.proficiencies += (DnDLightArmour, DnDSimpleWeapons, DnDMartialRangedWeapons.Hand_crossbow, DnDMartialWeapons.Longsword,DnDMartialWeapons.Rapier,DnDMartialWeapons.Shortsword, DnDProficiencies.Dexterity, DnDProficiencies.Charisma)
                #3 musical instruments of your choice
                #any 3 skills

            #Cleric Conditions
            case DnDClass.Cleric:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDSimpleWeapons, DnDProficiencies.Wisdom, DnDProficiencies.Charisma)
                #shields
                #2 skills from list

            #Druid Conditions
            case DnDClass.Druid:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDMartialWeapons.Scimitar, DnDSimpleWeapons.Sickle, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Spear, DnDMiscTools.Herbalism_kit, DnDProficiencies.Intelligence, DnDProficiencies.Wisdom)
                #shields (no armour made of metal)
                #2 skills from list

            #Monk Conditions
            case DnDClass.Monk:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDSimpleWeapons, DnDMartialWeapons.Shortsword, DnDProficiencies.Strength, DnDProficiencies.Dexterity)
                #1 artisan tool or musical instrument
                #2 skills from list

            #Rogue Conditions
            case DnDClass.Rogue:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDSimpleWeapons, DnDMartialRangedWeapons.Hand_crossbow, DnDMartialWeapons.Longsword, DnDMartialWeapons.Rapier, DnDMartialWeapons.Shortsword, DnDMiscTools.Thieves_tools, DnDProficiencies.Dexterity, DnDProficiencies.Intelligence)
                #4 skills from list

            #Warlock Conditions
            case DnDClass.Warlock:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDSimpleWeapons, DnDProficiencies.Wisdom, DnDProficiencies.Charisma)
                #2 skills from list

            #Artificer Conditions
            case DnDClass.Artificer:
                self.HP = 8
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDSimpleWeapons, DnDMiscTools.Thieves_tools, DnDArtisanTools.Tinkers_tools, DnDProficiencies.Constitution, DnDProficiencies.Intelligence)
                #Shields
                #One type of artisan tool
                #Choose 2 skills from list

            #Fighter Conditions
            case DnDClass.Fighter:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDHeavyArmour, DnDSimpleWeapons, DnDMartialWeapons, DnDProficiencies.Strength, DnDProficiencies.Constitution)
                #Shields
                #2 skills from list

            #Paladin Conditions
            case DnDClass.Paladin:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDHeavyArmour, DnDSimpleWeapons, DnDMartialWeapons, DnDProficiencies.Wisdom, DnDProficiencies.Charisma)
                #Shields
                #2 skills from list

            #Ranger Conditions
            case DnDClass.Ranger:
                self.HP = 10
                self.prof_bonus = 2
                self.proficiencies += (DnDLightArmour, DnDMediumArmour, DnDSimpleWeapons, DnDMartialWeapons, DnDProficiencies.Strength, DnDProficiencies.Dexterity)
                #shields
                #3 skills from list

            #Sorcerer Conditions
            case DnDClass.Sorcerer:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies += (DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Quarterstaff, DnDSimpleRangedWeapons.Light_crossbow, DnDProficiencies.Constitution, DnDProficiencies.Charisma)
                #2 skills from list

            #Wizard Conditions
            case DnDClass.Wizard:
                self.HP = 6
                self.prof_bonus = 2
                self.proficiencies += (DnDSimpleWeapons.Dagger, DnDSimpleRangedWeapons.Dart, DnDSimpleRangedWeapons.Sling, DnDSimpleWeapons.Quarterstaff, DnDSimpleRangedWeapons.Light_crossbow, DnDProficiencies.Intelligence, DnDProficiencies.Wisdom)
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