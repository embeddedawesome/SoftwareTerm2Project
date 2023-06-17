# Isabella
# D&D Characters
import enum

from DnDCharacter import *
from DnDCharacterDatabase import *
from DnDItems import *
# initialise variables

# functions
# separate file for DnDCharacter details
# Character Creation:
def createcharacter():
    race = make_decision("What is your character's race?", DnDRace)
    classtype = make_decision("What is your character's class?", DnDClass)

    name = input("What is your character's name?\n")

    background = make_decision("What is your character's background?", DnDBackground)
    align = make_decision("What is your character's alignment?", DnDAlignment)

    character = DnDCharacter(name, race, classtype, background, align)

    match classtype:
        case DnDClass.Artificer:
            weapon1 = make_decision("Select first weapon", DnDSimpleWeapons)
            weapon2 = make_decision("Select second weapon", DnDSimpleWeapons)
            armor = make_decision("Select armor", [DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Scale_mail_armour])
            character.inventory += [DnDAmmunition.Crossbow_Bolts, DnDMiscTools.Thieves_tools, DnDEquipmentPacks.Dungeoneers_Pack, armor]
            character.weapons += [DnDSimpleRangedWeapons.Light_crossbow, weapon1, weapon2]
        case DnDClass.Barbarian:
            weapon1 = make_decision("Select primary weapon", DnDMartialWeapons)
            weapon2 = make_decision("Select secondary weapon", DnDSimpleWeapons)
            if weapon2 == DnDSimpleWeapons.Handaxe:
                weapon2 = (DnDSimpleWeapons.Handaxe, 2)
            character.inventory += [DnDEquipmentPacks.Explorers_Pack]
            character.weapons += [weapon1, weapon2, (DnDSimpleWeapons.Javelin, 4)]
        case DnDClass.Bard:
            weapon = make_decision("Select primary weapon", [DnDMartialWeapons.Rapier, DnDMartialWeapons.Longsword, DnDSimpleWeapons])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Diplomats_Pack, DnDEquipmentPacks.Entertainers_Pack])
            instrument = make_decision("Select an instrument", [DnDMusicalInstruments])
            character.inventory += [DnDLightArmour.Leather_armour, pack, instrument]
            character.weapons += [weapon, DnDSimpleWeapons.Dagger]
        case DnDClass.Cleric:
            weapon1 = make_decision("Select primary weapon", [DnDSimpleWeapons.Mace, DnDMartialWeapons.Warhammer])
            armor = make_decision("Select armor",
                                  [DnDLightArmour.Leather_armour, DnDMediumArmour.Scale_mail_armour, DnDHeavyArmour.Chain_mail_armour])
            weapon2 = make_decision("Select secondary weapon", [DnDSimpleRangedWeapons.Light_crossbow, DnDSimpleWeapons])
            if weapon2 == DnDSimpleRangedWeapons.Light_crossbow:
                character.inventory += [DnDAmmunition.Crossbow_Bolts]
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Priests_Pack, DnDEquipmentPacks.Explorers_Pack])
            character.inventory += [DnDShields.Shield, pack, armor]
            character.weapons += [weapon1, weapon2]
        case DnDClass.Druid:
            weapon1 = make_decision("Select primary weapon", [DnDMartialWeapons.Scimitar, DnDSimpleWeapons])
            weapon2 = make_decision("Select secondary weapon", [DnDShields.Shield, DnDSimpleWeapons])
            character.inventory += [DnDLightArmour.Leather_armour, DnDEquipmentPacks.Explorers_Pack, DnDDruidicFocus]
            character.weapons += [weapon1, weapon2]
            
        case DnDClass.Wizard:
            weapon = make_decision("Select a weapon", [DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Dagger])
            magic_item = make_decision("Select a magic item", [DnDCommonItems.Component_Pouch, DnDArcaneFocus ])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Scholars_Pack, DnDEquipmentPacks.Explorers_Pack])
            character.inventory += [DnDCommonItems.Spellbook, magic_item, pack]
            character.weapons += [weapon]

    return character


# View Character by characteristics:
def viewcharacter(character):
    print(f"Race = {character.race.name}")
    print(f'Size = {character.size}')
    print(f'Speed = {character.speed}')
    print(f"Class = {character.classtype.name}")
    print(f"Name = {character.name}")
    print(f"Background = {character.background.name}")
    print(f"Alignment = {character.align.name}")
    print(f"Level = {character.level}")
    print(f"HP = {character.HP}")
    print(f"Proficiency Bonus = +{character.prof_bonus}")
    print(f"AC = {character.AC}")
    print(f"CON = {character.con}")
    print(f'Languages = ', end='')
    print(*[language.name for language in character.languages], sep=', ')
    print(f'Proficiencies = ', end='')
    print(*[proficiency.name for proficiency in character.proficiencies], sep=', ')
    print(f'Inventory = ', end='')
    print(*[inventory.name for inventory in character.inventory], sep=', ')
    print(f'Weapons = ', end='')
    print(*[weapons.name for weapons in character.weapons], sep=', ')


# Helper function to ask questions and process answers
def make_decision(question, constraints):
    # Generate the option list
    options = []

    # Make sure constraints is a list
    constraints = [constraints] if not isinstance(constraints, list) else constraints

    # Iterate through the constraints and generate tuples of printable names and values
    for i in constraints:
        # If constraint is a value of an Enum class, we print its name
        if isinstance(i, enum.Enum):
            options += [(i.name.replace("_", " "), i)]
        # If constraint is an Enum class we process all values
        elif isinstance(i, enum.EnumType):
            options += [(j.name.replace("_", " "), j) for j in i]
        # Otherwise we treat the constraint as a string
        else:
            options += [(i, i)]

    # Keep asking question while we don't have an acceptable answer
    while True:
        # Print the question
        print(question)

        # Print the options
        for i in range(len(options)):
            print(f"{i}: {options[i][0]}")

        # Wait for input
        answer = input()

        # Validate input as per constraints
        # First check if answer is a number matching to one of the answers
        if answer.isdigit() and int(answer) < len(options):
            return options[int(answer)][1]
        # Otherwise compare the answer to each name
        else:
            for o in options:
                if answer.lower() == o[0].lower():
                    return o[1]



# Run Project
#All data is converted to lowercase and matches the first letter of the word to allow shortcuts for the user to use.
if __name__ == "__main__":
    db = DnDCharacterDatabase("characters.pickle")
    while True:
        action = input("Create, View, Edit, Save, or Reset? ").lower()
        if action == "create" or action == "c":
            db.characters.append(createcharacter())
        elif action == "view" or action == "v":
            for character in db.characters:
                print("------------- Character Sheet ------------")
                viewcharacter(character)
                print("------------------------------------------")
        elif action == "reset" or action == "r":
            db.characters.reset()
            print("Characters Reset")
        elif action == "save" or action == "s":
            db.save()
            print("Characters saved")
