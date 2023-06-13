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
        case DnDClass.Wizard:
            weapon = make_decision("Select a weapon", [DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Dagger])
            magic_item = make_decision("Select a magic item", [DnDItem.Component_Pouch, *[item for item in DnDItem if dnd_items[item].item_type == DnDItemType.Arcane_Focus] ])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Scholars_Pack, DnDEquipmentPacks.Explorers_Pack])
            character.inventory += [DnDItem.Spellbook, weapon, magic_item, pack]

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
    # Keep asking question while we don't have an acceptable answer
    while True:
        # Print the question
        print(question)

        # Print the options
        if isinstance(constraints, enum.EnumType):
            # If the constraint is an EnumType we iterate through the values
            for i in constraints:
                print(f"{i.value}: {i.name}")
        elif isinstance(constraints, list):
            # If the constraint is a list of entries, iterate through each entry
            for i in range(len(constraints)):
                # If the entry is a value of an Enum class, we print its name
                if isinstance(constraints[i], enum.Enum):
                    print(f"{i}: {constraints[i].name}")
                else:
                    # Otherwise we treat it as a string and print its value
                    print(f"{i}: {constraints[i]}")


        # Wait for input
        answer = input()

        # Validate input as per constraints
        if isinstance(constraints, enum.EnumType):
            # Check if the input is a number we can use as an index
            if answer.isdigit() and int(answer) in constraints._value2member_map_:
                return constraints(int(answer))
            # Check if the string matches
            elif answer.title().replace(" ", "_") in constraints._member_names_:
                return constraints[answer.title().replace(" ", "_")]
        elif isinstance(constraints, list):
            if answer.isdigit() and int(answer) < len(constraints):
                return constraints[int(answer)]
            else:
                for option in constraints:
                    if isinstance(option, str) and answer.lower() == option.lower():
                        return option
                    elif isinstance(option, enum.Enum) and answer.lower().replace(" ", "_") == option.name.lower():
                        return option



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
