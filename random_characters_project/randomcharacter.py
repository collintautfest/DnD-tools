'''
This program randomly generates a new character with a race, subclass, class, level, and character details
'''
import random
import sys


def random_class():
    """
    Generates a random class
    """
    
    rand_class_pool = ['Artificer','Barbarian','Bard','Blood Hunter', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    global rand_class_num
    rand_class_num = random.randint(0, len(rand_class_pool)-1)
    char_class = rand_class_pool[rand_class_num]
    return char_class

def random_sub_class(randomclass): # you'll need to use random class return value as a parameter
    """
    Generates a random subclass based on the class
    """
    subclass_pool = [['Alchemist','Armorer','Artillerist','Battle Smith'], ['Path of the Ancestral Guardian', 'Path of the Battlerager', 'Path of the Beast', 'Path of the Berserker','Path of the Storm Herald', 'Path of the Totem Warrior', 'Path of Wild Magic', 'Path of the Zealot'], ['College of Creation', 'College of Eloquence', 'College of Glamour', 'College of Lore', 'College of Spirits', 'College of Swords', 'College of Valor', 'College of Whispers'], ['Order of the Ghostslayer', 'Order of the Lycan', 'Order of the Mutant', 'Order of the Profane Soul'],  ['Arcana Domain', 'Death Domain', 'Forge Domain', 'Grave Domain', 'Knowledge Domain', 'Life Domain', 'Light Domain', 'Nature Domain', 'Order Domain', 'Peace Domain', 'Tempest Domain', 'Trickery Domain', 'Twilight Domain', 'War Domain'], ['Circle of Dreams', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepherd', 'Circle of Spores', 'Circle of Stars', 'Circle of Wildfire'], ['Arcane Archer', 'Banneret', 'Battle Master', 'Cavalier', 'Champion', 'Echo Knight', 'Eldritch Knight', 'Psi Warrior', 'Rune Knight', 'Samurai'], ['Way of Mercy', 'Way of the Ascendant Dragon', 'Way of the Astral Self', 'Way of the Drunken Master', 'Way of the Four Elements', 'Way of the Kensei', 'Way of the Long Death', 'Way of the Open Hand', 'Way of Shadow', 'Way of the Sun Soul'], ['Oath of the Ancients', 'Oath of Conquest', 'Oath of the Crown', 'Oath of Devotion', 'Oath of Glory', 'Oath of Redemption', 'Oath of Vengeance', 'Oath of the Watchers', 'Oathbreaker'], ['Beast Master Conclave', 'Drakewarden', 'Fey Wanderer', 'Gloom Stalker Conclave', 'Horizon Walker Conclave', 'Hunter Conclave', 'Monster Slayer Conclave', 'Swarmkeeper'], ['Arcane Trickster', 'Assassin', 'Inquisitive', 'Mastermind', 'Phantom', 'Scout', 'Soulknife', 'Swashbuckler', 'Thief'], ['Aberrant Mind', 'Clockwork Soul', 'Draconic Bloodline', 'Divine Soul', 'Lunar Sorcery', 'Shadow Magic', 'Storm Sorcery', 'Storm Sorcery'],['Archfey', 'Celestial', 'Fathomless', 'Fiend', 'The Genie', 'Great Old One', 'Hexblade', 'Undead', 'Undying'], ['School of Abjuration', 'School of Bladesinging', 'School of Chronurgy', 'School of Conjuration', 'School of Divination', 'School of Enchantment', 'School of Evocation', 'School of Graviturgy', 'School of Illusion', 'School of Necromancy', 'Order of Scribes', 'School of Transmutation','School of War Magic']]
    # the entire goddam subclass pool

    if randomclass == 'Artificer':
        pointer = 0
    
    if randomclass == 'Barbarian':
        pointer = 1

    if randomclass == 'Bard':
        pointer = 2

    if randomclass == 'Blood Hunter':
        pointer = 3

    if randomclass == 'Cleric':
        pointer = 4
    
    if randomclass == 'Druid':
        pointer = 5

    if randomclass == 'Fighter':
        pointer = 6

    if randomclass == 'Monk':
        pointer = 7

    if randomclass == 'Paladin':
        pointer = 8
        
    if randomclass == 'Ranger':
        pointer = 9
    
    if randomclass == 'Rogue':
        pointer = 10
        
    if randomclass == 'Sorcerer':
        pointer = 11
    
    if randomclass == 'Warlock':
        pointer = 12

    if randomclass == 'Wizard':
        pointer = 13

    global random_sub_num  
    random_sub_num = random.randint(0, len(subclass_pool[pointer])-1)
    random_sub_gen = subclass_pool[pointer][random_sub_num]
    return random_sub_gen

def random_race():
    """
    Generates a random race for the character
    """
    standard_races = ['Dragonborn', 'Dwarf', 'Elf',  'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling']
    # you need to incorporate sub races
    custom_race = ['Custom Lineage']
    exotic_lineages = ['Aarakocra', 'Aasimar', 'Changeling', 'Deep Gnome', 'Duergar', 'Eladrin', 
                       'Fairy', 'Firbolg', 'Genasi (Air)', 'Genasi (Earth)', 'Genasi (Fire)', 'Genasi (Water)',
                       'Githyanki', 'Githzerai', 'Goliath', 'Harengon', 'Kenku', 'Locathah', 'Owlin', 'Satyr', 'Sea Elf',
                       'Shadar-Kai', 'Tabaxi', 'Tortle', 'Triton', 'Verdan']
    monstrous_lineages = ['Bugbear', 'Centaur', 'Goblin', 'Grung', 'Hobgoblin', 'Kobold', 'Lizardfolk', 'Minotaur',
                          'Orc', 'Shifter', 'Yuan-Ti']
    setting_lineages = ['Kender', 'Kalashtar', 'Warforged', 'Aetherborn', 'Aven', 'Khenra', 'Kor', 'Merfolk',
                        'Naga', 'Siren', 'Vampire', 'Dhamphir', 'Hexblood', 'Reborn', 'Loxodon', 'Simic Hybrid', 'Vedalken',
                        'Astral Elf', 'Autognome', 'Giff', 'Hadozee', 'Plasmoid', 'Thri-kreen']
    global randracelist
    randracelist = random.randint(0, 3)
    if randracelist == 0:
        lst = standard_races + custom_race
    if randracelist == 1:
        lst = exotic_lineages
    if randracelist == 2:
        lst = monstrous_lineages
    if randracelist == 3:
        lst = setting_lineages
    global rand_race
    rand_race = random.randint(0, len(lst)-1)

    return lst[rand_race]

def random_background():
    background_pool = ['Acolyte','Anthropologist','Archaeologist', 'Athlete', 'Charlatan','City Watch', 'Clan Crafter', 'Cloistered Scholar',
                       'Courtier', 'Criminal', 'Entertainer', 'Faceless', 'Faction Agent', 'Far Traveler', 'Feylost', 'Fisher', 'Folk Hero',
                       'Gladiator', 'Guild Artisan', 'Guild Merchant', 'Haunted One', 'Hermit', 'House Agent', 'Inheritor', 'Investigator',
                       'Knight', 'Knight of the Order', 'Marine', 'Mercenary Veteran', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor',
                       'Shipwright', 'Smuggler', 'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin', 'Uthgardt Tribe Member', 'Waterdhavian Noble',
                       'Witchlight Hand']
    global randum
    randum = random.randint(0, len(background_pool)-1)
    return background_pool[randum]

def random_gender():
    # character gender function
    ## Nonbinary and other genders can be added as needed, just add it to the pool
    gender_pool = ['Male', 'Female', 'femboy (male)', 'tomboy (female)']
    global gendrand
    gendrand = random.randint(0, len(gender_pool)-1)
    return gender_pool[gendrand]

def random_color():
    # using rgb until I can swap to hexcode
   return 'rgb('+ str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ',' + str(random.randint(0,255)) + ')'

def main():
    randomclass = random_class()
    subclass = random_sub_class(randomclass)
    race = random_race()
    gender = random_gender()
    color = random_color()
    print('Gender: '+ str(gender))
    print('Class: ' + str(randomclass))
    print('Subclass: ' + str(subclass))
    print('Level: ' + str(random.randint(1, 20)))
    print('Race: ' + str(race))
    print('Background: ' + random_background())
    print('Main Color: ' + str(color))
    print('savestate: '+ str(rand_class_num) + ' ' + str(random_sub_num) + ' ' + str(randracelist) + 
          ' ' + str(rand_race) + ' ' + str(randum) + ' ' + str(gendrand))

    print('Would you like to save to txt? (y/n)')
    # add user input detection, and make it crash proof
    # additionally add a regen feature
    usinput = input()
    if (usinput == "y"):
        file = open('/Users/Collin/Downloads/' + str(race) + ', ' + str(randomclass) + '.txt', 'wt')
        sys.stdout = file

        print('Gender: '+ str(gender))
        print('Class: ' + str(randomclass))
        print('Subclass: ' + str(subclass))
        print('Level: ' + str(random.randint(1, 20)))
        print('Race: ' + str(race))
        print('Background: ' + random_background())
        print('Main Color: ' + str(color))
        print('savestate: '+ str(rand_class_num) + ' ' + str(random_sub_num) + ' ' + str(randracelist) + 
              ' ' + str(rand_race) + ' ' + str(randum) + ' ' + str(gendrand)) 
        file.close()
    


main()