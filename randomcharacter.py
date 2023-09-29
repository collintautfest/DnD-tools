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