'''
This program randomly generates a new character with a race, subclass, class, level, and character details
'''
import random
def random_class():
    """
    Generates a random class
    """
    rand_class_pool = ['Artificer','Barbarian','Bard','Blood Hunter', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    rand_class_num = random.randint(0, len(rand_class_pool)-1)
    char_class = rand_class_pool[rand_class_num]
    return char_class

def random_sub_class(randomclass): # you'll need to use random class return value as a parameter
    """
    Generates a random subclass based on the class
    """
    if randomclass == 'Artificer':
        subclass_pool = ['Alchemist','Armorer','Artillerist','Battle Smith']
    
    if randomclass == 'Barbarian':
        subclass_pool = ['Path of the Ancestral Guardian', 'Path of the Battlerager', 'Path of the Beast', 'Path of the Berserker',
                         'Path of the Storm Herald', 'Path of the Totem Warrior', 'Path of Wild Magic', 'Path of the Zealot']
    
    if randomclass == 'Bard':
        subclass_pool = ['College of Creation', 'College of Eloquence', 'College of Glamour', 'College of Lore', 'College of Spirits',
                         'College of Swords', 'College of Valor', 'College of Whispers']
    
    if randomclass == 'Blood Hunter':
        subclass_pool = ['Order of the Ghostslayer', 'Order of the Lycan', 'Order of the Mutant', 'Order of the Profane Soul']
    
    if randomclass == 'Cleric':
        subclass_pool = ['Arcana Domain', 'Death Domain', 'Forge Domain', 'Grave Domain', 'Knowledge Domain', 'Life Domain',
                         'Light Domain', 'Nature Domain', 'Order Domain', 'Peace Domain', 'Tempest Domain', 'Trickery Domain',
                         'Twilight Domain', 'War Domain']
    
    if randomclass == 'Druid':
        subclass_pool = ['Circle of Dreams', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepherd', 'Circle of Spores',
                         'Circle of Stars', 'Circle of Wildfire']
    
    if randomclass == 'Fighter':
        subclass_pool = ['Arcane Archer', 'Banneret', 'Battle Master', 'Cavalier', 'Champion', 'Echo Knight', 'Eldritch Knight', 
                         'Psi Warrior', 'Rune Knight', 'Samurai']
    
    if randomclass == 'Monk':
        subclass_pool = ['Way of Mercy', 'Way of the Ascendant Dragon', 'Way of the Astral Self', 'Way of the Drunken Master', 
                         'Way of the Four Elements', 'Way of the Kensei', 'Way of the Long Death', 'Way of the Open Hand', 
                         'Way of Shadow', 'Way of the Sun Soul']
        
    if randomclass == 'Paladin':
        subclass_pool = ['Oath of the Ancients', 'Oath of Conquest', 'Oath of the Crown', 'Oath of Devotion', 'Oath of Glory',
                         'Oath of Redemption', 'Oath of Vengeance', 'Oath of the Watchers', 'Oathbreaker']
        
    if randomclass == 'Ranger':
        subclass_pool = ['Beast Master Conclave', 'Drakewarden', 'Fey Wanderer', 'Gloom Stalker Conclave', 'Horizon Walker Conclave', 
                         'Hunter Conclave', 'Monster Slayer Conclave', 'Swarmkeeper']
    
    if randomclass == 'Rogue':
        sublcass_pool = ['Arcane Trickster', 'Assassin', 'Inquisitive', 'Mastermind', 'Phantom', 'Scout', 'Soulknife',
                         'Swashbuckler', 'Thief']
        
    if randomclass == 'Sorcerer':
        subclass_pool = ['Aberrant Mind', 'Clockwork Soul', 'Draconic Bloodline', 'Divine Soul', 'Lunar Sorcery', 'Shadow Magic', 
                         'Storm Sorcery', 'Storm Sorcery']
    
    if randomclass == "Warlock":
        subclass_pool = ['Archfey', 'Celestial', 'Fathomless', 'Fiend', 'The Genie', 'Great Old One', 'Hexblade', 'Undead', 'Undying']

    