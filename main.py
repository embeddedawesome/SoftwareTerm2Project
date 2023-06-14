# Isabella
# D&D Characters

import enum
from DnDCharacter import *

# initialise variables

# functions
# separate file for DnDCharacter details
# Character Creation:
def createcharacter():
    race = make_decision("What is your character's race?", DnDRace)
    race = convert_to_dnd_race(race)
    classtype = make_decision("What is your character's class?", DnDClass)
    classtype = convert_to_dnd_class(classtype)
    name = input("What is your character's name?\n")
    background = make_decision("What is your character's background?", DnDBackground)
    background = convert_to_dnd_background(background)
    align = make_decision("What is your character's alignment?", DnDAlignment)
    align = convert_to_dnd_alignment(align)
    character = DnDCharacter(name, race, classtype, background, align)
    match classtype:
        case DnDClass.Wizard:
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", [DnDSkills.Arcana, DnDSkills.History, DnDSkills.Insight, DnDSkills.Investigation, DnDSkills.Medicine, DnDSkills.Religion])
            skillprof2 = make_decision("Select another skill", [DnDSkills.Arcana, DnDSkills.History, DnDSkills.Insight, DnDSkills.Investigation, DnDSkills.Medicine, DnDSkills.Religion])
            weapon = make_decision("Select a weapon", [DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Dagger])
            magic_item = make_decision("Select a magic item", [DnDItems.Component_Pouch, DnDItems.Orb, DnDItems.Rod, DnDItems.Wand, DnDItems.Staff, DnDItems.Crystal])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Scholars_pack, DnDEquipmentPacks.Explorers_pack])
            character.inventory += [DnDItems.Spellbook, magic_item, pack]
            character.weapons += [weapon]
            character.proficiencies += [skillprof1, skillprof2]

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
    character = None
    while True:
        action = input("Create, View, Edit, or Reset? ")
        match action.lower()[0]:
            case'c':
                character = createcharacter()
            case'v':
                viewcharacter(character)
            case'r':
                character.reset()
                print("Character Reset")
