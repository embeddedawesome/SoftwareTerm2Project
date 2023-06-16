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
    classtype = make_decision("What is your character's class?", DnDClass)
    name = input("What is your character's name?\n")
    background = make_decision("What is your character's background?", DnDBackground)
    align = make_decision("What is your character's alignment?", DnDAlignment)
    character = DnDCharacter(name, race, classtype, background, align)
    match classtype:
        case DnDClass.Barbarian:
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total",[DnDSkills.Animal_handling, DnDSkills.Athletics, DnDSkills.Intimidation, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Survival])
            skillprof2 = make_decision("Select another skill",[DnDSkills.Animal_handling, DnDSkills.Athletics, DnDSkills.Intimidation, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Survival])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons.Battleaxe, DnDMartialWeapons.Flail, DnDMartialWeapons.Glaive, DnDMartialWeapons.Greataxe, DnDMartialWeapons.Greatsword, DnDMartialWeapons.Halberd, DnDMartialWeapons.Lance, DnDMartialWeapons.Longsword, DnDMartialWeapons.Maul, DnDMartialWeapons.Morningstar, DnDMartialWeapons.Pike, DnDMartialWeapons.Rapier, DnDMartialWeapons.Scimitar, DnDMartialWeapons.Shortsword, DnDMartialWeapons.Trident, DnDMartialWeapons.War_pick, DnDMartialWeapons.Warhammer, DnDMartialWeapons.Whip])
            weapon2 = make_decision("Select another weapon. If you choose Handaxe, you get 2 of them.", [DnDSimpleWeapons.Club, DnDSimpleWeapons.Dagger, DnDSimpleWeapons.Greatclub, DnDSimpleWeapons.Handaxe, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Light_hammer, DnDSimpleWeapons.Mace, DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Sickle, DnDSimpleWeapons.Spear])
            character.inventory += [DnDEquipmentPacks.Explorers_pack]
            character.weapons += [weapon1, weapon2, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin, DnDSimpleWeapons.Javelin]
            character.proficiencies += [skillprof1, skillprof2]

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
    # Generate the option list
    options = []
    if isinstance(constraints, enum.EnumType):
        options += [(i.name.replace("_", " "), i) for i in constraints]
    elif isinstance(constraints, list):
        # If the constraint is a list of entries, iterate through each entry
        for i in constraints:
            # If the entry is a value of an Enum class, we print its name
            if isinstance(i, enum.Enum):
                options += [(make_string(i), i)]
            elif isinstance(i, enum.EnumType):
                options += [(make_string(j), j) for j in i]
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
        if answer.isdigit() and int(answer) < len(options):
            return options[int(answer)][1]
        else:
            for o in options:
                if answer.lower() == o[0].lower():
                    return o[1]

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
