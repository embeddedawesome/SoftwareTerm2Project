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
                character.weapons += [DnDSimpleWeapons.Handaxe]
            character.inventory += [DnDEquipmentPacks.Explorers_Pack]
            character.weapons += [weapon1, weapon2, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin]
        case DnDClass.Bard:
            weapon = make_decision("Select primary weapon", [DnDMartialWeapons.Rapier, DnDMartialWeapons.Longsword, DnDSimpleWeapons])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Diplomats_Pack, DnDEquipmentPacks.Entertainers_Pack])
            instrument = make_decision("Select an instrument", ["Lute", "Other musical instrument"])
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
            character.inventory += [DnDLightArmour.Leather_armour, DnDEquipmentPacks.Explorers_Pack, *[item for item in DnDItem if dnd_items[item].item_type == DnDItemType.Druidic_Focus]]
            character.weapons += [weapon1, weapon2]
        case DnDClass.Fighter:
            
        case DnDClass.Wizard:
            weapon = make_decision("Select a weapon", [DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Dagger])
            magic_item = make_decision("Select a magic item", [DnDItem.Component_Pouch, *[item for item in DnDItem if dnd_items[item].item_type == DnDItemType.Arcane_Focus] ])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Scholars_Pack, DnDEquipmentPacks.Explorers_Pack])
            character.inventory += [DnDItem.Spellbook, magic_item, pack]
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
    if isinstance(constraints, enum.EnumType):
        options += [(i.name.replace("_", " "), i) for i in constraints]
    elif isinstance(constraints, list):
        # If the constraint is a list of entries, iterate through each entry
        for i in constraints:
            # If the entry is a value of an Enum class, we print its name
            if isinstance(constraints[i], enum.Enum):
                options += [(constraints[i].name.replace("_", " "), constraints[i])]
            if isinstance(constraints[i], enum.EnumType):
                options += [(j.name.replace("_", " "), j) for j in constraints[i]]
            else:
                options += [(constraints[i], constraints[i])]

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
        if answer.isdigit() and int(answer) < len(options):
            return options[int(answer)][1]
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
