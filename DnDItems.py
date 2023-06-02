from enum import Enum, auto
from DnDData import DnDSimpleWeapons, DnDMartialWeapons, DnDSimpleRangedWeapons, DnDMartialRangedWeapons


class DnDItemType(Enum):
    Equipment_Pack = auto()
    Common_Item = auto()
    Usable_Items = auto()
    Clothes = auto()
    Arcane_Focus = auto()
    Druidic_Focus = auto()
    Holy_Symbols = auto()


class DnDItemObject:
    def __init__(self, name, item_type, cost, weight, description):
        self.name = name
        self.item_type = item_type
        self.weight = weight
        self.cost = cost
        self.description = description


class DnDContainerObject:
    def __init__(self, name, cost, capacity, weight, description):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.capacity = capacity
        self.description = description


class DnDItem(Enum):
    Burglars_Pack = auto()
    Diplomats_Pack = auto()
    Dungeoneers_Pack = auto()
    Entertainers_Pack = auto()
    Explorers_Pack = auto()
    Priests_Pack = auto()
    Scholars_Pack = auto()
    Abacus = auto()
    Bedroll = auto()
    Bell = auto()
    Blanket = auto()
    Block_and_Tackle = auto()
    Book = auto()
    Candle = auto()
    Chain = auto()
    Chalk = auto()
    Component_Pouch = auto()
    Fishing_Tackle = auto()
    Grappling_Hook = auto()
    Hammer = auto()
    Hourglass = auto()
    Ink = auto()
    Ink_Pen = auto()
    Ladder = auto()
    Lock = auto()
    Magnifying_Glass = auto()
    Mess_Kit = auto()
    Miners_Pick = auto()
    Paper = auto()
    Parchment = auto()
    Perfume = auto()
    Piton = auto()
    Pole = auto()
    Rations = auto()
    Rope_Hemp = auto()
    Rope_Silk = auto()
    Sealing_Wax = auto()
    Shovel = auto()
    Signal_Whistle = auto()
    Signet_Ring = auto()
    Sledgehammer = auto()
    Spellbook = auto()
    Iron_Spikes = auto()
    Spyglass = auto()
    Tent = auto()
    Whetstone = auto()
    Acid_Vial = auto()
    Alchemists_Fire_Flask = auto()
    Antitoxin = auto()
    Ball_Bearings = auto()
    Caltrops = auto()
    Climbers_Kit = auto()
    Crowbar = auto()
    Healers_Kit = auto()
    Holy_Water_Flask = auto()
    Hunting_Trap = auto()
    Lamp = auto()
    Bullseye_Lantern = auto()
    Hooded_Lantern = auto()
    Oil_Flask = auto()
    Basic_Poison_Vial = auto()
    Potion_of_Healing = auto()
    Tinderbox = auto()
    Torch = auto()
    Common_Clothes = auto()
    Costume = auto()
    Fine_Clothes = auto()
    Robes = auto()
    Travelers_Clothes = auto()
    Crystal = auto()
    Orb = auto()
    Rod = auto()
    Staff = auto()
    Wand = auto()
    Sprig_of_Mistletoe = auto()
    Totem = auto()
    Wooden_Staff = auto()
    Yew_Wand = auto()
    Amulet = auto()
    Emblem = auto()
    Reliquary = auto()


dnd_items = {
    DnDItem.Burglars_Pack: DnDItemObject("Burglar's Pack", DnDItemType.Equipment_Pack, "16 gp", None,
                                         "Backpack, a bag of 1,000 ball bearings, 10 feet of string, a bell, 5 candles, a crowbar, a hammer, 10 pitons, a hooded lantern, 2 flasks of oil, 5 days rations, a tinderbox and a waterskin. The pack also has 50 feet of hempen rope strapped to the side of it."),
    DnDItem.Diplomats_Pack: DnDItemObject("Diplomat's Pack", DnDItemType.Equipment_Pack, "39 gp", None,
                                          "Chest, 2 cases for maps and scrolls, a set of fine clothes, a bottle of ink, an ink pen, a lamp, 2 flasks of oil, 5 sheets of paper, a vial of perfume, sealing wax, and soap."),
    DnDItem.Dungeoneers_Pack: DnDItemObject("Dungeoneer's Pack", DnDItemType.Equipment_Pack, "12 gp", None,
                                            "Backpack, a crowbar, a hammer, 10 pitons, 10 torches, a tinderbox, 10 days of rations, and a waterskin. The pack also has 50 feet of hempen rope strapped to the side of it."),
    DnDItem.Entertainers_Pack: DnDItemObject("Entertainer's Pack", DnDItemType.Equipment_Pack, "40 gp", None,
                                             "Backpack, a bedroll, 2 costumes, 5 candles, 5 days of rations, a waterskin, and a disguise kit."),
    DnDItem.Explorers_Pack: DnDItemObject("Explorer's Pack", DnDItemType.Equipment_Pack, "10 gp", None,
                                          "Backpack, a bedroll, a mess kit, a tinderbox, 10 torches, 10 days of rations, and a waterskin. The pack also has 50 feet of hempen rope strapped to the side of it."),
    DnDItem.Priests_Pack: DnDItemObject("Priest's Pack", DnDItemType.Equipment_Pack, "19 gp", None,
                                        "Backpack, a blanket, 10 candles, a tinderbox, an alms box, 2 blocks of incense, a censer, vestments, 2 days of rations, and a waterskin."),
    DnDItem.Scholars_Pack: DnDItemObject("Scholar's Pack", DnDItemType.Equipment_Pack, "40 gp", None,
                                         "Backpack, a book of lore, a bottle of ink, an ink pen, 10 sheets of parchment, a little bag of sand, and a small knife."),
    DnDItem.Abacus: DnDItemObject("Abacus", DnDItemType.Common_Item, "2 gp", "2 lb.", ""),
    DnDItem.Bedroll: DnDItemObject("Bedroll", DnDItemType.Common_Item, "1 gp", "2 lb.", ""),
    DnDItem.Bell: DnDItemObject("Bell", DnDItemType.Common_Item, "1 gp", None, ""),
    DnDItem.Blanket: DnDItemObject("Blanket", DnDItemType.Common_Item, "5 sp", "5 lb.", ""),
    DnDItem.Block_and_Tackle: DnDItemObject("Block and Tackle", DnDItemType.Common_Item, "1 gp", "5 lb.",
                                            "A set of pulleys with a cable threaded through them and a hook to attach to objects, a block and tackle allows you to hoist up to four times the weight you can normally lift."),
    DnDItem.Book: DnDItemObject("Book", DnDItemType.Common_Item, "25 gp", "5 lb.",
                                "A book might contain poetry, historical accounts, information pertaining to a particular field of lore, diagrams and notes on gnomish contraptions, or just about anything else that can be represented sing text or pictures. A book of spells is a spellbook."),
    DnDItem.Candle: DnDItemObject("Candle", DnDItemType.Common_Item, "1 cp", None,
                                  "For 1 hour, a candle sheds bright light in a 5-foot radius and dim light for another 5 feet."),
    DnDItem.Chain: DnDItemObject("Chain (10 ft)", DnDItemType.Common_Item, "5 gp", "10 lb.",
                                 "A chain has 10 hit points. It can be burst with a successful DC 20 Strength check."),
    DnDItem.Chalk: DnDItemObject("Chalk (1 pc)", DnDItemType.Common_Item, "1 cp", None, ""),
    DnDItem.Component_Pouch: DnDItemObject("Component Pouch", DnDItemType.Common_Item, "25 gp", "2 lb.",
                                           "A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost (as indicated in a spell's description)."),
    DnDItem.Fishing_Tackle: DnDItemObject("Fishing Tackle", DnDItemType.Common_Item, "1 gp", "4 lb.",
                                          "This kit includes a wooden rod, silken line, corkwood bobbers, steel hooks, lead sinkers, velvet lures, and narrow netting."),
    DnDItem.Grappling_Hook: DnDItemObject("Grappling Hook", DnDItemType.Common_Item, "2 gp", "4 lb.", ""),
    DnDItem.Hammer: DnDItemObject("Hammer", DnDItemType.Common_Item, "1 gp", "3 lb.", ""),
    DnDItem.Hourglass: DnDItemObject("Hourglass", DnDItemType.Common_Item, "25 gp", "1 lb.", ""),
    DnDItem.Ink: DnDItemObject("Ink (1 oz)", DnDItemType.Common_Item, "10 gp", None, ""),
    DnDItem.Ink_Pen: DnDItemObject("Ink Pen", DnDItemType.Common_Item, "2 cp", None, ""),
    DnDItem.Ladder: DnDItemObject("Ladder (10 ft)", DnDItemType.Common_Item, "1 sp", "25 lb.", ""),
    DnDItem.Lock: DnDItemObject("Lock", DnDItemType.Common_Item, "10 gp", "1 lb.",
                                "A key is provided with the lock. Without the key, a creature proficient with thieves' tools can pick this lock with a successful DC 15 Dexterity check. Your DM may decide that better locks are available for higher prices."),
    DnDItem.Magnifying_Glass: DnDItemObject("Magnifying Glass", DnDItemType.Common_Item, "100 gp", None,
                                            "This lens allows a closer look at small objects. It is also useful as a substitute or flint and steel when starting fires. Lighting a fire with a magnifying glass requires light as bright as sunlight to focus, tinder to ignite, and about 5 minutes for the fire to ignite. A magnifying glass grants advantage on any ability check made to appraise or inspect an item that is small or highly detailed."),
    DnDItem.Mess_Kit: DnDItemObject("Mess Kit", DnDItemType.Common_Item, "2 sp", "1 lb.",
                                    "This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl."),
    DnDItem.Miners_Pick: DnDItemObject("Miner's Pick", DnDItemType.Common_Item, "2 gp", "10 lb.", ""),
    DnDItem.Paper: DnDItemObject("Paper (1 pc)", DnDItemType.Common_Item, "2 sp", None, ""),
    DnDItem.Parchment: DnDItemObject("Parchment (1 sheet)", DnDItemType.Common_Item, "1 sp", None, ""),
    DnDItem.Perfume: DnDItemObject("Perfume (vial)", DnDItemType.Common_Item, "5 gp", None, ""),
    DnDItem.Piton: DnDItemObject("Piton", DnDItemType.Common_Item, "5 cp", "0.25 lb.", ""),
    DnDItem.Pole: DnDItemObject("Pole (10 ft)", DnDItemType.Common_Item, "5 cp", "7 lb.", ""),
    DnDItem.Rations: DnDItemObject("Rations (1 day)", DnDItemType.Common_Item, "5 sp", "2 lb.",
                                   "Rations consist of dry foods suitable for extended travel, including jerky, dried fruit, hardtack, and nuts."),
    DnDItem.Rope_Hemp: DnDItemObject("Rope - Hemp (50 ft)", DnDItemType.Common_Item, "1 gp", "10 lb.",
                                     "Rope, whether made of hemp or silk, has 2 hit points and can be burst with a DC 17 Strength check."),
    DnDItem.Rope_Silk: DnDItemObject("Rope - Silk (50 ft)", DnDItemType.Common_Item, "10 gp", "5 lb.",
                                     "Rope, whether made of hemp or silk, has 2 hit points and can be burst with a DC 17 Strength check."),
    DnDItem.Sealing_Wax: DnDItemObject("Sealing Wax", DnDItemType.Common_Item, "5 sp", None, ""),
    DnDItem.Shovel: DnDItemObject("Shovel", DnDItemType.Common_Item, "2 gp", "5 lb.", ""),
    DnDItem.Signal_Whistle: DnDItemObject("Signal Whistle", DnDItemType.Common_Item, "5 cp", None, ""),
    DnDItem.Signet_Ring: DnDItemObject("Signet Ring", DnDItemType.Common_Item, "5 gp", None, ""),
    DnDItem.Sledgehammer: DnDItemObject("Sledgehammer", DnDItemType.Common_Item, "2 gp", "10 lb.", ""),
    DnDItem.Spellbook: DnDItemObject("Spellbook", DnDItemType.Common_Item, "50 gp", "3 lb.",
                                     "Essential for wizards, a spellbook is a leather-bound tome with 100 blank vellum pages suitable for recording spells."),
    DnDItem.Iron_Spikes: DnDItemObject("Spikes - Iron (10)", DnDItemType.Common_Item, "1 gp", "5 lb.", ""),
    DnDItem.Spyglass: DnDItemObject("Spyglass", DnDItemType.Common_Item, "1000 gp", "1 lb.",
                                    "Objects viewed through a spyglass are magnified to twice their size."),
    DnDItem.Tent: DnDItemObject("Tent - 2 person", DnDItemType.Common_Item, "2 gp", "20 lbs.", ""),
    DnDItem.Whetstone: DnDItemObject("Whetstone", DnDItemType.Common_Item, "1 cp", "1 lb.", ""),
    DnDItem.Acid_Vial: DnDItemObject("Acid (vial)", DnDItemType.Usable_Items, "25 gp", "1 lb.",
                                     "As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact. In either case, make a ranged attack against a creature or object, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage."),
    DnDItem.Alchemists_Fire_Flask: DnDItemObject("Alchemist's Fire (flask)", DnDItemType.Usable_Items, "50 gp", "1 lb.",
                                                 "This sticky, adhesive fluid ignites when exposed to air. As an action, you can throw this flask up to 20 feet, shattering it on impact. Make a ranged attack against a creature or object, treating the alchemist's fire as an improvised weapon. On a hit, the target takes 1d4 fire damage at the start of each of its turns. A creature can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames."),
    DnDItem.Antitoxin: DnDItemObject("Antitoxin (vial)", DnDItemType.Usable_Items, "50 gp", None,
                                     "A creature that drinks this vial of liquid gains advantage on saving throws against poison for 1 hour. It confers no benefits to undead or constructs."),
    DnDItem.Ball_Bearings: DnDItemObject("Ball Bearings (bag of 1,000)", DnDItemType.Usable_Items, "1 gp", "2 lb.",
                                         "As an action, you can spill these tiny balls from their pouch to cover a level area 10 feet square. A creature moving across the covered area must succeed on a DC 10 Dexterity saving throw or all prone. A creature moving through the area at half speed doesn't need to make the saving throw."),
    DnDItem.Caltrops: DnDItemObject("Caltrops (bag of 20)", DnDItemType.Usable_Items, "1 gp", "2 lb.",
                                    "As an action, you can spread a single bag of caltrops to cover a 5-foot-square area. Any creature that enters the area must succeed on a DC 15 Dexterity saving throw or stop moving and take 1 piercing damage. Until the creature regains at least 1 hit point, its walking speed is reduced by 10 feet. A creature moving through the area at half speed doesn't need to make the saving throw."),
    DnDItem.Climbers_Kit: DnDItemObject("Climber's Kit", DnDItemType.Usable_Items, "25 gp", "12 lb.",
                                        "A climber's kit includes special pitons, boot tips, gloves, and a harness. You can use the climber's kit as an action to anchor yourself; when you do, you can't fall more than 25 feet from the point where you anchored yourself, and you can't climb more than 25 feet away from that point without undoing the anchor."),
    DnDItem.Crowbar: DnDItemObject("Crowbar", DnDItemType.Usable_Items, "2 gp", "5 lb.",
                                   "Using a crowbar grants advantage to Strength checks where the crowbar's leverage can be applied."),
    DnDItem.Healers_Kit: DnDItemObject("Healer's Kit", DnDItemType.Usable_Items, "5 gp", "3 lb.",
                                       "This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check."),
    DnDItem.Holy_Water_Flask: DnDItemObject("Holy Water (flask)", DnDItemType.Usable_Items, "25 gp", "1 lb.",
                                            "As an action, you can splash the contents of this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. In either case, make a ranged attack against a target creature, treating the holy water as an improvised weapon. If the target is a fiend or undead, it takes 2d6 radiant damage. A cleric or paladin may create holy water by performing a special ritual. The ritual takes 1 hour to perform, uses 25 gp worth of powdered silver, and requires the caster to expend a 1st-level spell slot."),
    DnDItem.Hunting_Trap: DnDItemObject("Hunting Trap", DnDItemType.Usable_Items, "5 gp", "25 lb.",
                                        "When you use your action to set it, this trap forms a saw-toothed steel ring that snaps shut when a creature steps on a pressure plate in the center. The trap is affixed by a heavy chain to an immobile object, such as a tree or a spike driven into the ground. A creature that steps on the plate must succeed on a DC 13 Dexterity saving throw or take 1d4 piercing damage and stop moving. Thereafter, until the creature breaks free of the trap, its movement is limited by the length of chain (typically 3 feet long). A creature can use its action to make a DC 13 Strength check, freeing itself or another creature within its reach on a success. Each failed check deals 1 piercing damage to the trapped creature."),
    DnDItem.Lamp: DnDItemObject("Lamp", DnDItemType.Usable_Items, "5 sp", "1 lb.",
                                "A lamp casts bright light in a 15-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil."),
    DnDItem.Bullseye_Lantern: DnDItemObject("Lantern - Bullseye", DnDItemType.Usable_Items, "10 gp", "2 lb.",
                                            "A bullseye lantern casts bright light in a 60-foot cone and dim light for an additional 60 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil."),
    DnDItem.Hooded_Lantern: DnDItemObject("Lantern - Hooded", DnDItemType.Usable_Items, "5 gp", "2 lb.",
                                          "A hooded lantern casts bright light in a 30-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. As an action, you can lower the hood, reducing the light to dim light in a 5-foot radius."),
    DnDItem.Oil_Flask: DnDItemObject("Oil (flask)", DnDItemType.Usable_Items, "1 sp", "1 lb.",
                                     "Oil usually comes in a clay flask that holds 1 pint. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. if lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn."),
    DnDItem.Basic_Poison_Vial: DnDItemObject("Poison, basic (vial)", DnDItemType.Usable_Items, "100 gp", None,
                                             "You can use the poison in this vial to coat one slashing or piercing weapon or up to three pieces of ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must make a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying."),
    DnDItem.Potion_of_Healing: DnDItemObject("Potion of Healing (common)", DnDItemType.Usable_Items, "50 gp", "0.5 lb.",
                                             ""),
    DnDItem.Tinderbox: DnDItemObject("Tinderbox", DnDItemType.Usable_Items, "5 sp", "1 lb.",
                                     "This small container holds flint, fire steel, an tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch — or anything else with abundant, exposed fuel — takes an action. Lighting any other fire takes 1 minutes."),
    DnDItem.Torch: DnDItemObject("Torch", DnDItemType.Usable_Items, "1 cp", "1 lb.",
                                 "A torch burns for 1 hour, providing bright light in a 20-foot radius and dim light for an additional 20 feet. If you make a melee attack with a burning torch and hit, it deals 1 fire damage."),
    DnDItem.Common_Clothes: DnDItemObject("Common Clothes", DnDItemType.Clothes, "5 sp", "3 lb.", ""),
    DnDItem.Costume: DnDItemObject("Costume", DnDItemType.Clothes, "5 gp", "4 lb.", ""),
    DnDItem.Fine_Clothes: DnDItemObject("Fine Clothes", DnDItemType.Clothes, "15 gp", "6 lb.", ""),
    DnDItem.Robes: DnDItemObject("Robes", DnDItemType.Clothes, "1 gp", "4 lb.", ""),
    DnDItem.Travelers_Clothes: DnDItemObject("Traveler's Clothes", DnDItemType.Clothes, "2 gp", "4 lb.", ""),
    DnDItem.Crystal: DnDItemObject("Crystal", DnDItemType.Arcane_Focus, "10 gp", "1 lb.", ""),
    DnDItem.Orb: DnDItemObject("Orb", DnDItemType.Arcane_Focus, "20 gp", "3 lb.", ""),
    DnDItem.Rod: DnDItemObject("Rod", DnDItemType.Arcane_Focus, "10 gp", "2 lb.", ""),
    DnDItem.Staff: DnDItemObject("Staff", DnDItemType.Arcane_Focus, "5 gp", "4 lb.", ""),
    DnDItem.Wand: DnDItemObject("Wand", DnDItemType.Arcane_Focus, "10 gp", "1 lb.", ""),
    DnDItem.Sprig_of_Mistletoe: DnDItemObject("Sprig of Mistletoe", DnDItemType.Druidic_Focus, "1 gp", None, ""),
    DnDItem.Totem: DnDItemObject("Totem", DnDItemType.Druidic_Focus, "1 gp", None, ""),
    DnDItem.Wooden_Staff: DnDItemObject("Wooden Staff", DnDItemType.Druidic_Focus, "5 gp", "4 lb.", ""),
    DnDItem.Yew_Wand: DnDItemObject("Yew Wand", DnDItemType.Druidic_Focus, "10 gp", "1 lb.", ""),
    DnDItem.Amulet: DnDItemObject("Amulet", DnDItemType.Holy_Symbols, "5 gp", "1 lb.", ""),
    DnDItem.Emblem: DnDItemObject("Emblem", DnDItemType.Holy_Symbols, "5 gp", None, ""),
    DnDItem.Reliquary: DnDItemObject("Reliquary", DnDItemType.Holy_Symbols, "5 gp", "2 lb.", ""),
}


class DnDContainer(Enum):
    Backpack = auto()
    Barrel = auto()
    Basket = auto()
    Bucket = auto()
    Crossbow_Bolt_Case = auto()
    Map_Scroll_Case = auto()
    Chest = auto()
    Flask_Tankard = auto()
    Glass_Bottle = auto()
    Jug = auto()
    Iron_Pot = auto()
    Pouch = auto()
    Quiver = auto()
    Sack = auto()
    Vial = auto()
    Waterskin = auto()


dnd_containers = {
    DnDContainer.Backpack: DnDContainerObject("Backpack", "2 gp", "1 cubic foot/30 pounds of gear", "5 lb.",
                                              "You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack."),
    DnDContainer.Barrel: DnDContainerObject("Barrel", "2 gp", "40 gallons liquid, 4 cubic feet solid", "70 lb.", ""),
    DnDContainer.Basket: DnDContainerObject("Basket", "4 sp", "2 cubic feet/40 pounds of gear", "2 lb.", ""),
    DnDContainer.Bucket: DnDContainerObject("Bucket", "5 cp", "3 gallons liquid, 1/2 cubic foot solid", "2 lb.", ""),
    DnDContainer.Crossbow_Bolt_Case: DnDContainerObject("Case, Crossbow Bolt", "1 gp", "20 crossbow bolts", "1 lb.",
                                                        ""),
    DnDContainer.Map_Scroll_Case: DnDContainerObject("Case, Map/Scroll", "1 gp",
                                                     "ten rolled-up sheets of paper of five rolled-up sheets of parchment",
                                                     "1 lb.", ""),
    DnDContainer.Chest: DnDContainerObject("Chest", "5 gp", "12 cubic feet/300 pounds of gear", "25 lb.", ""),
    DnDContainer.Flask_Tankard: DnDContainerObject("Flask or Tankard", "2 cp", "1 pint liquid", "1 lb.", ""),
    DnDContainer.Glass_Bottle: DnDContainerObject("Glass Bottle", "2 gp", "1.5 pints liquid", "2 lb.", ""),
    DnDContainer.Jug: DnDContainerObject("Jug or Pitcher", "2 cp", "1 gallon liquid", "4 lb.", ""),
    DnDContainer.Iron_Pot: DnDContainerObject("Pot, iron", "2 gp", "1 gallon liquid", "10 lb", ""),
    DnDContainer.Pouch: DnDContainerObject("Pouch", "5 sp", "1/5 cubic foot/6 pounds of gear", "1 lb.",
                                           "A cloth or leather pouch can hold up to 20 sling bullets or 50 blowgun needles, among other things. A compartmentalized pouch for holding spell components is called a component pouch."),
    DnDContainer.Quiver: DnDContainerObject("Quiver", "1 gp", "20 arrows", "1 lb.", ""),
    DnDContainer.Sack: DnDContainerObject("Sack", "1 cp", "1 cubic foot/30 pounds of gear", "0.5 lb.", ""),
    DnDContainer.Vial: DnDContainerObject("Vial", "1 gp", "4 ounces liquid", None, ""),
    DnDContainer.Waterskin: DnDContainerObject("Waterskin", "2 sp", "4 pints liquid", "5 lb. (full)", ""),
}


class DnDWeaponObject:
    def __init__(self, name, cost, damage, damage_type, weight, properties):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.weight = weight
        self.properties = properties


dnd_simple_weapons = {
    DnDSimpleWeapons.Club: DnDWeaponObject('Club', '1 sp', '1d4', 'bludgeoning', '2 lb.', 'Light'),
    DnDSimpleWeapons.Dagger: DnDWeaponObject('Dagger', '2 gp', '1d4', 'piercing', '1 lb.',
                                             'Finesse, light, thrown (range 20/60)'),
    DnDSimpleWeapons.Greatclub: DnDWeaponObject('Greatclub', '2 sp', '1d8', 'bludgeoning', '10 lb.', 'Two-handed'),
    DnDSimpleWeapons.Handaxe: DnDWeaponObject('Handaxe', '5 gp', '1d6', 'slashing', '2 lb.',
                                              'Light, thrown (range 20/60)'),
    DnDSimpleWeapons.Javelin: DnDWeaponObject('Javelin', '5 sp', '1d6', 'piercing', '2 lb.', 'Thrown (range 30/120)'),
    DnDSimpleWeapons.Light_hammer: DnDWeaponObject('Light Hammer', '2 sp', '1d4', 'bludgeoning', '2 lb.',
                                                   'Light, thrown (range 20/60)'),
    DnDSimpleWeapons.Mace: DnDWeaponObject('Mace', '5 gp', '1d6', 'bludgeoning', '4 lb.', ''),
    DnDSimpleWeapons.Quarterstaff: DnDWeaponObject('Quarterstaff', '2 sp', '1d6', 'bludgeoning', '4 lb.',
                                                   'Versatile (1d8)'),
    DnDSimpleWeapons.Sickle: DnDWeaponObject('Sickle', '1 gp', '1d4', 'slashing', '2 lb.', 'Light'),
    DnDSimpleWeapons.Spear: DnDWeaponObject('Spear', '1 gp', '1d6', 'piercing', '3 lb.',
                                            'Thrown (range 20/60), versatile (1d8)'),
}

dnd_simple_ranged_weapons = {
    DnDSimpleRangedWeapons.Light_crossbow: DnDWeaponObject('Crossbow, Light', '25 gp', '1d8', 'piercing', '5 lb.',
                                                           'Ammunition (range 80/320), loading, two-handed'),
    DnDSimpleRangedWeapons.Dart: DnDWeaponObject('Dart', '5 cp', '1d4', 'piercing', '0.25 lb.',
                                                 'Finesse, thrown (range 20/60)'),
    DnDSimpleRangedWeapons.Shortbow: DnDWeaponObject('Shortbow', '25 gp', '1d6', 'piercing', '2 lb.',
                                                     'Ammunition (range 80/320), two-handed'),
    DnDSimpleRangedWeapons.Sling: DnDWeaponObject('Sling', '1 sp', '1d4', 'bludgeoning', 'None',
                                                  'Ammunition (range 30/120)'),
}

# DnDWeapon('Martial Melee Weapons', 'Cost,'Damage','','Weight','Properties')
dnd_martial_melee_weapons = {
    DnDMartialWeapons.Battleaxe: DnDWeaponObject('Battleaxe', '10 gp', '1d8', 'slashing', '4 lb.', 'Versatile (1d10)'),
    DnDMartialWeapons.Flail: DnDWeaponObject('Flail', '10 gp', '1d8', 'bludgeoning', '2 lb.', ''),
    DnDMartialWeapons.Glaive: DnDWeaponObject('Glaive', '20 gp', '1d10', 'slashing', '6 lb.',
                                              'Heavy, reach, two-handed'),
    DnDMartialWeapons.Greataxe: DnDWeaponObject('Greataxe', '30 gp', '1d12', 'slashing', '7 lb.', 'Heavy, two-handed'),
    DnDMartialWeapons.Greatsword: DnDWeaponObject('Greatsword', '50 gp', '2d6', 'slashing', '6 lb.',
                                                  'Heavy, two-handed'),
    DnDMartialWeapons.Halberd: DnDWeaponObject('Halberd', '20 gp', '1d10', 'slashing', '6 lb.',
                                               'Heavy, reach, two-handed'),
    DnDMartialWeapons.Lance: DnDWeaponObject('Lance', '10 gp', '1d12', 'piercing', '6 lb.', 'Reach, special'),
    DnDMartialWeapons.Longsword: DnDWeaponObject('Longsword', '15 gp', '1d8', 'slashing', '3 lb.', 'Versatile (1d10)'),
    DnDMartialWeapons.Maul: DnDWeaponObject('Maul', '10 gp', '2d6', 'bludgeoning', '10 lb.', 'Heavy, two-handed'),
    DnDMartialWeapons.Morningstar: DnDWeaponObject('Morningstar', '15 gp', '1d8', 'piercing', '4 lb.', ''),
    DnDMartialWeapons.Pike: DnDWeaponObject('Pike', '5 gp', '1d10', 'piercing', '18 lb.', 'Heavy, reach, two-handed'),
    DnDMartialWeapons.Rapier: DnDWeaponObject('Rapier', '25 gp', '1d8', 'piercing', '2 lb.', 'Finesse'),
    DnDMartialWeapons.Scimitar: DnDWeaponObject('Scimitar', '25 gp', '1d6', 'slashing', '3 lb.', 'Finesse, light'),
    DnDMartialWeapons.Shortsword: DnDWeaponObject('Shortsword', '10 gp', '1d6', 'piercing', '2 lb.', 'Finesse, light'),
    DnDMartialWeapons.Trident: DnDWeaponObject('Trident', '5 gp', '1d6', 'piercing', '4 lb.',
                                               'Thrown (range 20/60), versatile (1d8)'),
    DnDMartialWeapons.War_pick: DnDWeaponObject('War Pick', '5 gp', '1d8', 'piercing', '2 lb.', ''),
    DnDMartialWeapons.Warhammer: DnDWeaponObject('Warhammer', '15 gp', '1d8', 'bludgeoning', '2 lb.',
                                                 'Versatile (1d10)'),
    DnDMartialWeapons.Whip: DnDWeaponObject('Whip', '2 gp', '1d4', 'slashing', '3 lb.', 'Finesse, reach'),
}

dnd_martial_ranged_weapons = {
    DnDMartialRangedWeapons.Blowgun: DnDWeaponObject('Blowgun', '10 gp', '1', 'piercing', '1 lb.',
                                                     'Ammunition (range 25/100), loading'),
    DnDMartialRangedWeapons.Hand_crossbow: DnDWeaponObject('Crossbow, Hand', '75 gp', '1d6', 'piercing', '3 lb.',
                                                           'Ammunition (range 30/120), light, loading'),
    DnDMartialRangedWeapons.Heavy_crossbow: DnDWeaponObject('Crossbow, Heavy', '50 gp', '1d10', 'piercing', '18 lb.',
                                                            'Ammunition (range 100/400), heavy, loading, two-handed'),
    DnDMartialRangedWeapons.Longbow: DnDWeaponObject('Longbow', '50 gp', '1d8', 'piercing', '2 lb.',
                                                     'Ammunition (range 150/600), heavy, two-handed'),
    DnDMartialRangedWeapons.Net: DnDWeaponObject('Net', '1 gp', 'None', 'None', '3 lb.',
                                                 'Special, thrown (range 5/15)'),
}


class DnDAmmunition(Enum):
    Arrows = auto()
    Blowgun_Needles = auto()
    Crossbow_Bolts = auto()
    Sling_Bullets = auto()


class DnDAmmunitionObject:
    def __init__(self, name, cost, weight, number):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.number = number


# DnDAmmunition('Ammunition', 'Cost,'Weight','Number')
dnd_ammunition = {
    DnDAmmunition.Arrows: DnDAmmunitionObject('Arrows', '1 gp', '1lb.', 20)
    DnDAmmunition.Blowgun_Needles: DnDAmmunitionObject('Blowgun Needles', '1 gp', '1lb.', 50)
    DnDAmmunition.Crossbow_Bolts: DnDAmmunitionObject('Crossbow Bolts', '1 gp', '1.5lb', 20)
    DnDAmmunition.Sling_Bullets: DnDAmmunitionObject('Sling Bullets', '4 cp', '1.5lb', 20)
}
