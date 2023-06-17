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
        case DnDClass.Artificer:
            artificer_skills = [DnDSkills.Arcana, DnDSkills.History, DnDSkills.Investigation, DnDSkills.Medicine, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Sleight_of_hand]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", artificer_skills)
            skillprof2 = make_decision("Select another skill", [i for i in artificer_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", DnDSimpleWeapons)
            weapon2 = make_decision("Select another weapon", DnDSimpleWeapons)
            armor = make_decision("Select armor", [DnDLightArmour.Studded_leather_armour, DnDMediumArmour.Scale_mail_armour])
            character.inventory += [(20, DnDAmmunition.Crossbow_Bolts), DnDMiscTools.Thieves_tools, DnDEquipmentPacks.Dungeoneers_pack, armor]
            character.weapons += [DnDSimpleRangedWeapons.Light_crossbow, weapon1, weapon2]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Barbarian:
            barbarian_skills = [DnDSkills.Animal_handling, DnDSkills.Athletics, DnDSkills.Intimidation, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Survival]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", barbarian_skills)
            skillprof2 = make_decision("Select another skill",[i for i in barbarian_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons])
            weapon2 = make_decision("Select another weapon. If you choose Handaxe, you get 2 of them.", [DnDSimpleWeapons])
            if weapon2 == DnDSimpleWeapons.Handaxe:
                weapon2 = (2, DnDSimpleWeapons.Handaxe)
            character.inventory += [DnDEquipmentPacks.Explorers_pack]
            character.weapons += [weapon1, weapon2, (4, DnDSimpleWeapons.Javelin)]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Bard:
            skillprof1 = make_decision("Select a skill (you will need to choose 3 in total", DnDSkills)
            skillprof2 = make_decision("Select another skill", [i for i in DnDSkills if i != skillprof1])
            skillprof3 = make_decision("Select another skill", [i for i in DnDSkills if (i != skillprof1 and i != skillprof2)])
            weapon = make_decision("Select a weapon",
                                   [DnDMartialWeapons.Rapier, DnDMartialWeapons.Longsword, DnDSimpleWeapons])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Diplomats_pack, DnDEquipmentPacks.Entertainers_pack])
            instrument = make_decision("Select an instrument", [DnDMusicalInstruments])
            character.inventory += [DnDLightArmour.Leather_armour, pack, instrument]
            character.weapons += [weapon, DnDSimpleWeapons.Dagger]
            character.proficiencies += [skillprof1, skillprof2, skillprof3]

        case DnDClass.Cleric:
            cleric_skills = [DnDSkills.History, DnDSkills.Insight, DnDSkills.Medicine, DnDSkills.Persuasion, DnDSkills.Religion]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", cleric_skills)
            skillprof2 = make_decision("Select another skill", [i for i in cleric_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", [DnDSimpleWeapons.Mace, DnDMartialWeapons.Warhammer])
            weapon2 = make_decision("Select another weapon",
                                    [DnDSimpleRangedWeapons.Light_crossbow, DnDSimpleWeapons])
            armor = make_decision("Select armor",
                                  [DnDLightArmour.Leather_armour, DnDMediumArmour.Scale_mail_armour,
                                   DnDHeavyArmour.Chain_mail_armour])
            holy_symbol = make_decision("Select a holy symbol", [DnDItems.Amulet, DnDItems.Emblem, DnDItems.Reliquary])
            if weapon2 == DnDSimpleRangedWeapons.Light_crossbow:
                character.inventory += [(20,DnDAmmunition.Crossbow_Bolts)]
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Priests_pack, DnDEquipmentPacks.Explorers_pack])
            character.inventory += [DnDShields.Shield, pack, armor, holy_symbol]
            character.weapons += [weapon1, weapon2]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Druid:
            druid_skills = [DnDSkills.Arcana, DnDSkills.Animal_handling, DnDSkills.Insight, DnDSkills.Medicine, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Religion, DnDSkills.Survival]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", druid_skills)
            skillprof2 = make_decision("Select another skill", [i for i in druid_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons.Scimitar, DnDSimpleWeapons])
            weapon2 = make_decision("Select another weapon", [DnDShields.Shield, DnDSimpleWeapons])
            focus = make_decision("Select a Druidic focus", [DnDItems.Sprig_of_Mistletoe, DnDItems.Totem, DnDItems.Wooden_Staff, DnDItems.Yew_Wand])
            character.inventory += [DnDLightArmour.Leather_armour, DnDEquipmentPacks.Explorers_pack, focus]
            character.weapons += [weapon1, weapon2]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Fighter:
            fighter_skills = [DnDSkills.Acrobatics, DnDSkills.Animal_handling, DnDSkills.Athletics, DnDSkills.History, DnDSkills.Insight, DnDSkills.Intimidation, DnDSkills.Perception, DnDSkills.Survival]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", fighter_skills)
            skillprof2 = make_decision("Select another skill", [i for i in fighter_skills if i != skillprof1])
            armour = make_decision("Select armour. Light armour also receives Longbow and 20 arrows",
                                   [DnDHeavyArmour.Chain_mail_armour, DnDLightArmour.Leather_armour])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons])
            weapon2 = make_decision("Select another weapon or shield", [DnDMartialWeapons, DnDShields.Shield])
            ranged_weapon = make_decision("Select a ranged weapon", [DnDSimpleRangedWeapons.Light_crossbow, (2,DnDSimpleWeapons.Handaxe)])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            if ranged_weapon == DnDSimpleRangedWeapons.Light_crossbow:
                character.inventory += [(20, DnDAmmunition.Crossbow_Bolts)]
            if armour == DnDLightArmour.Leather_armour:
                character.weapons += [DnDMartialRangedWeapons.Longbow]
                character.inventory += [(20, DnDAmmunition.Arrows)]
            character.inventory += [DnDLightArmour.Leather_armour, pack]
            character.weapons += [weapon1, weapon2, ranged_weapon]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Monk:
            monk_skills = [DnDSkills.Acrobatics, DnDSkills.Athletics, DnDSkills.History, DnDSkills.Insight, DnDSkills.Religion, DnDSkills.Stealth]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", monk_skills)
            skillprof2 = make_decision("Select another skill", [i for i in monk_skills if i != skillprof1])
            weapon = make_decision("Select a weapon", [DnDMartialWeapons.Shortsword, DnDSimpleWeapons])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            character.inventory += [pack]
            character.weapons += [weapon, (10, DnDSimpleRangedWeapons.Dart)]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Paladin:
            paladin_skills = [DnDSkills.Athletics, DnDSkills.Insight, DnDSkills.Intimidation, DnDSkills.Medicine, DnDSkills.Persuasion, DnDSkills.Religion]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", paladin_skills)
            skillprof2 = make_decision("Select another skill", [i for i in paladin_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons])
            weapon2 = make_decision("Select another weapon or shield", [DnDMartialWeapons, DnDShields.Shield])
            weapon3 = make_decision("Select a simple weapon (Javelin will receive 5x Javelin)", [DnDSimpleWeapons])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            holy_symbol = make_decision("Select a holy symbol", [DnDItems.Amulet, DnDItems.Emblem, DnDItems.Reliquary])
            if weapon3 == DnDSimpleWeapons.Javelin:
                weapon3 = (5, DnDSimpleWeapons.Javelin)
            character.inventory += [DnDHeavyArmour.Chain_mail_armour, pack, holy_symbol]
            character.weapons += [weapon1, weapon2, weapon3]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Ranger:
            ranger_skills = [DnDSkills.Animal_handling, DnDSkills.Athletics, DnDSkills.Insight, DnDSkills.Investigation, DnDSkills.Nature, DnDSkills.Perception, DnDSkills.Stealth, DnDSkills.Survival]
            skillprof1 = make_decision("Select first skill (you will need to choose 3 in total", ranger_skills)
            skillprof2 = make_decision("Select second skill", [i for i in ranger_skills if i != skillprof1])
            skillprof3 = make_decision("Select third skill", [i for i in ranger_skills if (i != skillprof1 and i != skillprof2)])
            armour = make_decision("Select armour", [DnDMediumArmour.Scale_mail_armour, DnDLightArmour.Leather_armour])
            weapon = make_decision("Select a weapon", [(2,DnDMartialWeapons.Shortsword), [(2,i) for i in DnDSimpleWeapons]])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            character.inventory += [pack, armour, (20, DnDAmmunition.Arrows)]
            character.weapons += [weapon, DnDMartialRangedWeapons.Longbow]
            character.proficiencies += [skillprof1, skillprof2, skillprof3]

        case DnDClass.Rogue:
            rogue_skills = [DnDSkills.Acrobatics, DnDSkills.Athletics, DnDSkills.Deception, DnDSkills.Insight, DnDSkills.Intimidation, DnDSkills.Investigation, DnDSkills.Perception, DnDSkills.Performance, DnDSkills.Persuasion, DnDSkills.Sleight_of_hand, DnDSkills.Stealth]
            skillprof1 = make_decision("Select first skill (you will need to choose 4 in total", rogue_skills)
            skillprof2 = make_decision("Select second skill", [i for i in rogue_skills if i != skillprof1])
            skillprof3 = make_decision("Select third skill",
                                       [i for i in rogue_skills if (i != skillprof1 and i != skillprof2)])
            skillprof4 = make_decision("Select fourth skill",
                                       [i for i in rogue_skills if (i != skillprof1 and i != skillprof2 and i != skillprof3)])
            weapon1 = make_decision("Select a weapon", [DnDMartialWeapons.Rapier, DnDMartialWeapons.Shortsword])
            weapon2 = make_decision("Select another weapon", [DnDSimpleRangedWeapons.Shortbow, DnDMartialWeapons.Shortsword])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Burglars_pack, DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            if weapon2 == DnDSimpleRangedWeapons.Shortbow:
                character.inventory += [(20, DnDAmmunition.Arrows)]
            character.inventory += [DnDLightArmour.Leather_armour, pack, DnDMiscTools.Thieves_tools]
            character.weapons += [weapon1, weapon2, (2, DnDSimpleWeapons.Dagger)]
            character.proficiencies += [skillprof1, skillprof2, skillprof3, skillprof4]

        case DnDClass.Sorcerer:
            sorceror_skills = [DnDSkills.Arcana, DnDSkills.Deception, DnDSkills.Insight, DnDSkills.Intimidation, DnDSkills.Persuasion, DnDSkills.Religion]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", sorceror_skills)
            skillprof2 = make_decision("Select another skill", [i for i in sorceror_skills if i != skillprof1])
            weapon = make_decision("Select a weapon", [DnDSimpleRangedWeapons.Light_crossbow, DnDSimpleWeapons])
            magic_item = make_decision("Select a magical tool or focus", [DnDItems.Component_Pouch, DnDItems.Crystal, DnDItems.Orb, DnDItems.Rod, DnDItems.Staff, DnDItems.Wand])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Explorers_pack])
            if weapon == DnDSimpleRangedWeapons.Light_crossbow:
                character.inventory += [(20, DnDAmmunition.Crossbow_Bolts)]
            character.inventory += [pack, magic_item]
            character.weapons += [weapon, (2, DnDSimpleWeapons.Dagger)]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Warlock:
            warlock_skills = [DnDSkills.Arcana, DnDSkills.Deception, DnDSkills.History, DnDSkills.Intimidation, DnDSkills.Investigation, DnDSkills.Nature, DnDSkills.Religion]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", warlock_skills)
            skillprof2 = make_decision("Select another skill", [i for i in warlock_skills if i != skillprof1])
            weapon1 = make_decision("Select a weapon", [DnDSimpleRangedWeapons.Light_crossbow, DnDSimpleWeapons])
            weapon2 = make_decision("Select another weapon", [DnDSimpleWeapons])
            magic_item = make_decision("Select a magical tool or focus",
                                       [DnDItems.Component_Pouch, DnDItems.Crystal, DnDItems.Orb, DnDItems.Rod,
                                        DnDItems.Staff, DnDItems.Wand])
            pack = make_decision("Select a pack",
                                 [DnDEquipmentPacks.Dungeoneers_pack, DnDEquipmentPacks.Scholars_pack])
            if weapon1 == DnDSimpleRangedWeapons.Light_crossbow:
                character.inventory += [(20, DnDAmmunition.Crossbow_Bolts)]
            character.inventory += [DnDLightArmour.Leather_armour, pack, magic_item]
            character.weapons += [weapon2, weapon2, (2, DnDSimpleWeapons.Dagger)]
            character.proficiencies += [skillprof1, skillprof2]

        case DnDClass.Wizard:
            wizard_skills = [DnDSkills.Arcana, DnDSkills.History, DnDSkills.Insight, DnDSkills.Investigation, DnDSkills.Medicine, DnDSkills.Religion]
            skillprof1 = make_decision("Select a skill (you will need to choose 2 in total", wizard_skills)
            skillprof2 = make_decision("Select another skill", [i for i in wizard_skills if i != skillprof1])
            weapon = make_decision("Select a weapon", [DnDSimpleWeapons.Quarterstaff, DnDSimpleWeapons.Dagger])
            magic_item = make_decision("Select a magic item", [DnDItems.Component_Pouch, DnDItems.Orb, DnDItems.Rod, DnDItems.Wand, DnDItems.Staff, DnDItems.Crystal])
            pack = make_decision("Select a pack", [DnDEquipmentPacks.Scholars_pack, DnDEquipmentPacks.Explorers_pack])
            character.inventory += [DnDItems.Spellbook, magic_item, pack]
            character.weapons += [weapon]
            character.proficiencies += [skillprof1, skillprof2]

    return character

def make_string(input):
    if isinstance(input, str):
        return input
    elif isinstance(input, enum.Enum):
        return input.name.replace("_", " ")
    elif isinstance(input, enum.EnumType):
        return ','.join([i.name.replace("_", " ") for i in input])
    elif isinstance(input, tuple):
        if isinstance(input[1], enum.Enum):
            return f"{input[0]}x {input[1].name.replace('_', ' ')}"
        else:
            return f"{input[0]}x {input[1]}"


# View Character by characteristics:
def viewcharacter(character):
    if character == None:
        print("No characters to view")
        return
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
    print(*[make_string(language) for language in character.languages], sep=', ')
    print(f'Proficiencies = ', end='')
    print(*[make_string(proficiency) for proficiency in character.proficiencies], sep=', ')
    print(f'Inventory = ', end='')
    print(*[make_string(inventory) for inventory in character.inventory], sep=', ')
    print(f'Weapons = ', end='')
    print(*[make_string(weapons) for weapons in character.weapons], sep=', ')

# Helper function to ask questions and process answers
def make_decision(question, constraints):
    # Generate the option list
    options = []
    # Make sure constraints is a list
    constraints = [constraints] if not isinstance(constraints, list) else constraints

    # Iterate through the constraints and generate tuples of printable names and values
    for i in constraints:
        # If constraint is an Enum class we process all values
        if isinstance(i, enum.EnumType):
            options += [(make_string(j), j) for j in i]
        # Otherwise we treat the constraint as a string
        else:
            options += [(make_string(i), i)]

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
