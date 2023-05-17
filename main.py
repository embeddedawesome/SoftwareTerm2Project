from DnDCharacter import DnDCharacter, DnDRace, DnDClass, DnDAlignment


#Character Creation:
def createcharacter():
    race = input(f"What is your character's race? {[x.name for x in DnDRace]}")
    race = DnDRace[race.title()]
    classtype = input("What is your character's class? ")
    name = input("What is your character's name? ")
    bg = input("What is your character's background? ")
    align = input("What is your character's alignment (eg. CN, LG...)? ")
    character = DnDCharacter(name, race, classtype, bg, align)
    return character


#View Character:
def viewcharacter(character):
    print(f'Race = {character.race.name}')
    print(f'Class = {character.classtype.name if isinstance(character.classtype, DnDClass) else character.classtype}')
    print(f'Name = {character.name}')
    print(f'Background = {character.bg}')
    print(f'Alignment = {character.align.name if isinstance(character.align, DnDAlignment) else character.align}')
    print(f'Level = {character.level}')
    print(f'HP = {character.HP}')
    print(f'AC = {character.AC}')
    print(f'CON = {character.con}')


#Run Project
if __name__ == "__main__":
    character = None
    while True:
        action = input('Create, View, Edit, or Reset? ')
        if action.lower() == 'create':
            character = createcharacter()
        elif action.lower() == 'view':
            viewcharacter(character)
        elif action.lower() == 'reset':
            character.reset()
            print('Character Reset')