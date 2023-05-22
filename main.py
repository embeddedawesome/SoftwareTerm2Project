from DnDCharacter import DnDCharacter, DnDRace, DnDClass, DnDBackground, convert_to_dnd_race, convert_to_dnd_background, convert_to_dnd_class, convert_to_dnd_alignment


# Character Creation:
def createcharacter():
    race = input(f"What is your character's race? {DnDRace._member_names_}\n")
    race = convert_to_dnd_race(race)
    classtype = input(f"What is your character's class? {DnDClass._member_names_}\n")
    classtype = convert_to_dnd_class(classtype)
    name = input("What is your character's name?\n")
    background = input(f"What is your character's background? {DnDBackground._member_names_}\n")
    background = convert_to_dnd_background(background)
    align = input("What is your character's alignment (eg. CN, LG...)?\n")
    align = convert_to_dnd_alignment(align)
    character = DnDCharacter(name, race, classtype, background, align)
    return character


# View Character:
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
    print(f"AC = {character.AC}")
    print(f"CON = {character.con}")


# Run Project
if __name__ == "__main__":
    character = None
    while True:
        action = input("Create, View, Edit, or Reset? ")
        if action.lower() == "create":
            character = createcharacter()
        elif action.lower() == "view":
            viewcharacter(character)
        elif action.lower() == "reset":
            character.reset()
            print("Character Reset")
