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
        race = input(f"What is your character's race? {DnDRace._member_names_}\n")
        race = convert_to_dnd_race(race)
    while classtype == None:
        classtype = input(f"What is your character's class? {DnDClass._member_names_}\n")
        classtype = convert_to_dnd_class(classtype)
    name = input("What is your character's name?\n")
    while background == None:
        background = input(f"What is your character's background? {DnDBackground._member_names_}\n")
        background = convert_to_dnd_background(background)
    while align == None:
        align = input(f"What is your character's alignment? {DnDAlignment._member_names_}\n")
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
    print(*[p.name for p in character.proficiencies], sep=', ')
    print(f'Inventory = {[i.name for i in character.inventory]}')
    print(f'Weapons = {[w.name for w in character.weapons]}')


# Run Project
# all data is converted to lowercase
if __name__ == "__main__":
    db = DnDCharacterDatabase("characters.pickle")
    while True:
        action = input("Create, View, Edit, Save, or Reset? ")
        if action.lower() == "create":
            db.characters.append(createcharacter())
        elif action.lower() == "view":
            for character in db.characters:
                print("------------- Character Sheet ------------")
                viewcharacter(character)
                print("------------------------------------------")
        elif action.lower() == "reset":
            db.characters.reset()
            print("Characters Reset")
        elif action.lower() == "save":
            db.save()
            print("Characters saved")
