# Isabella
# D&D Characters

from DnDCharacter import *
from DnDCharacterDatabase import *

# initialise variables

# functions
# separate file for DnDCharacter details
# Character Creation:
def createcharacter():
    race = None
    classtype = None
    background = None
    align = None
    while race == None:
        print(f"What is your character's race?")
        for race in DnDRace:
            print(f"{race.value}: {race.name}")
        race = input()
        race = convert_to_dnd_race(race)
    while classtype == None:
        print(f"What is your character's class?")
        for c in DnDClass:
            print(f"{c.value}: {c.name}")
        classtype = input()
        classtype = convert_to_dnd_class(classtype)
    name = input("What is your character's name?\n")
    while background == None:
        print(f"What is your character's background?")
        for b in DnDBackground:
            print(f"{b.value}: {b.name}")
        background = input()
        background = convert_to_dnd_background(background)
    while align == None:
        print(f"What is your character's alignment?")
        for a in DnDAlignment:
            print(f"{a.value}: {a.name}")
        align = input()
        align = convert_to_dnd_alignment(align)
    character = DnDCharacter(name, race, classtype, background, align)
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
