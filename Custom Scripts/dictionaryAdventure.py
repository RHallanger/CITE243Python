import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()

#################LISTS and DICTIONARIES
player_inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1, 'enchanted gemstone': 0, 'dragon summoning stone': 0}
cultist_table = ['enchanted gemstone', 'ruby', 'dagger', 'gold coin', 'gold coin', 'gold coin'] #chance to get 1 of these items, gold coin is very likely... I think Runescape handles droprates like this in typescript
dragon_table = ['dragon dagger', 'dragon sword', 'dragon chainbody', 'dragon battle-axe'] #Although unusable, it is cool to get something still...

#################Functions

#This builds the player's inventory display and performs an inventory insanity check, if they get 255 it is technically a softlockable as it is possible to delete enchanted gemstones.
def display_inventory(inventory_ID):
    print('Player\'s Inventory:')
    item_total = 0
    lose_count = 0
    for k, v in inventory_ID.items():

        ###The player has space, and they actually have an item for it to display
        if ((item_total + v) <= 255) and (v != 0):
            print(f'x{v} {k}')
            item_total += v
            logging.debug(f'Added {v} {k} to total, {item_total}')

        ###Inventory is too full, force the player to drop the last loaded item, end of the list, most likely important.
        elif (item_total + v) > 255:
            lose_count = 0
            while (item_total + v) > 255:
                logging.debug(f'removed 1 {k}. Total {v} {k}.')
                lose_count += 1
                v -= 1
            print(f'x{v} {k}')
            item_total += v
            logging.debug(f'Added {v} {k} to total, {item_total}')

        #Just here to track what keys are loaded into the dictionary
        else:
            logging.debug(f'{k} is at {0}')

        #Player representation of what they had to ditch.
        if lose_count > 0:
            print(f'Your inventory is too full, you were forced to leave x{lose_count} {k}.')

    print('Total Items: ' + str(item_total) + '/255')

#This is juist a selector menu to swap between quitting, inventory, and attacking.
def player_action(inventory_ID, opponent_table, opponent):
    option = ''
        
    #Player input for menu select
    while option not in ['inventory', 'attack', 'quit']:
        option = input('> ')
        option = option.lower()
        if option not in ['inventory', 'attack', 'quit']:
            print('invalid option')

    #Closes the game...
    if option == 'quit':
        quit()

    #Performs an inventory loop to display the player's inventory... technically they can have an infinite amount of items until they look at their inventory.
    elif option == 'inventory':
        display_inventory(inventory_ID)

    #Just straight up slays the enemy.
    elif option == 'attack':
        slay(inventory_ID, opponent_table, opponent)

#Picks a random drop from the creature's drop table and adds it to player's inventory, and finishes the game if it is a dragon.
def slay(inventory_ID, creature_table, str_creature):
    drop_table_end = len(creature_table)
    drop_value = random.randint(0, drop_table_end-1)
    logging.debug(f'random value = {drop_value}.')
    drop = creature_table[drop_value]

    #This is to handle keys not already present.
    if drop not in inventory_ID.keys():
        inventory_ID.setdefault(drop, 1)
    #If they are present, add 1 to it's value
    else:
        inventory_ID[drop] += 1
    print(f'You kill the {str_creature} and receive a {drop}.')

    #Dragon check...
    if str_creature == 'dragon':
        print('After slaying the dragon, you lob off one of the horns to return to the commissioner.')
        inventory_ID.setdefault('dragon horn', 1)
        print('You have slayed the dragon!')
        print('The end...')
        quit()



###############STORY
print('Hello and welcome to a quick adventure game.')
print('Objective: Collect four enchanted gemstones from slaying cultists.')
print('\nSetting: You, the player, are on a quest to slay The Terror of Evensborough, a terrible dragon.\nWhile enroute, dragon cultists burst from the shades ready to attack.\nThe light expands to show what could only be described as an army of cultists.')
print('Please note that there is not really much functionality with the inventory...')
#Catch the player until they have all of the enchanted stones.
while player_inventory['dragon summoning stone'] == 0:
    #Check if the player has enough gemstones to encounter the dragon.
    if player_inventory['enchanted gemstone'] >= 3:
        player_inventory['enchanted gemstone'] -= 3
        player_inventory['dragon summoning stone'] += 1
        break
    print('A cultist steps out from the brush and attacks you!')
    print('\n\nAction: What will you do? [Player can input: {inventory, attack, or quit}]')
    player_action(player_inventory, cultist_table, 'cultist')

print('Three stones in your pouch begin emmitting light and fusing together.')
print('The cultists begin scattering and running away, but what could it mean?')
print('With a bolt of lightning, a dragon appears before you, the night sky has turned to red with fire.')

#This is basically a catch for the player if they check their inventory.
while 'dragon horn' not in player_inventory.keys():
    print('\n\nAction: What will you do? [Player can input: {inventory, attack, or quit}]')
    player_action(player_inventory, dragon_table, 'dragon')