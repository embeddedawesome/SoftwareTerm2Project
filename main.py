
#Character Core
class DnDCharacter():
    def __init__(self, name, race, classtype, bg, align):
        self.name = name
        self.race = race
        self.level = 1
        self.HP = 1
        self.AC = 0
        self.classtype = classtype
        self.set_class(classtype)
        self.con = 2
        self.bg = bg
        self.align = align

    # Delete Character:
    def reset(self):
        self.race = 'N/A'
        self.classtype = 'N/A'
        self.name = 'N/A'
        self.level = 'N/A'
        self.HP = 'N/A'
        self.AC = 'N/A'
        self.con = 'N/A'
        self.bg = 'N/A'
        self.align = 'N/A'

    #Level 1 Health Calculations
    def set_class(self, classtype):
        if classtype.lower == 'barbarian':
            self.HP = 12
        elif classtype.lower == 'bard' or 'cleric' or 'druid' or 'monk' or 'rogue' or 'warlock' or 'artificer':
            self.HP = 8
        elif classtype.lower == 'fighter' or 'paladin' or 'ranger':
            self.HP = 10
        elif classtype.lower == 'sorcerer' or 'wizard':
            self.HP = 6
        else:
            self.HP = 'N/A'


#Character Creation:
def createcharacter():
    race = input("What is your character's race? ")
    classtype = input("What is your character's class? ")
    name = input("What is your character's name? ")
    bg = input("What is your character's background? ")
    align = input("What is your character's alignment (eg. CN, LG...)? ")
    character = DnDCharacter(name, race, classtype, bg, align)
    return character


#View Character:
def viewcharacter(character):
    print(f'Race = {character.race}')
    print(f'Class = {character.classtype}')
    print(f'Name = {character.name}')
    print(f'Background = {character.bg}')
    print(f'Alignment = {character.align}')
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