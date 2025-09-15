import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()

#################LISTS and DICTIONARIES
player_inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
cultist_table = ['enchanted gemstone', 'ruby', 'dagger', 'gold coin', 'gold coin', 'gold coin'] #chance to get 1 of these items, gold coin is very likely... I think Runescape handles droprates like this in typescript
dragon_table = ['dragon dagger', 'dragon sword', 'dragon chainbody', 'dragon battle-axe']

#################Functions
def display_inventory(inventory_ID):
    print('Player\'s Inventory:')
    item_total = 0
    lose_count = 0
    for k, v in inventory_ID.items():
        if ((item_total + v) <= 255) and (v != 0): ###The player has space, and they actually have an item
            print(f'x{v} {k}')
            item_total += v
            logging.debug(f'Added {v} {k} to total, {item_total}')
        elif (item_total + v) > 255:
            lose_count = 0
            while (item_total + v) > 255:
                logging.debug(f'removed 1 {k}. Total {v} {k}.')
                lose_count += 1
                v -= 1
            print(f'x{v} {k}')
            item_total += v
            logging.debug(f'Added {v} {k} to total, {item_total}')
        else:
            logging.debug(f'{k} is at {0}')

        if lose_count > 0:
            print(f'The player was forced to leave x{lose_count} {k}.')

    print('Total Items: ' + str(item_total) + '/255')

def player_action(opponent):
    option = ''
    while option not in ['inventory', 'attack']:
        option = input()

def slay(inventory_ID, creature_table):
    pass



print('Hello and welcome to a quick adventure game.')
print('Objective: Collect four enchanted gemstones from slaying cultists.')
print('\nSetting: You, the player, are on a quest to slay The Terror of Evensborough, a terrible dragon.\nWhile enroute, dragon cultists burst from the shades ready to attack.\nThe light retracts to show what could only be described as an army of cultists.')
print('\n\nAction: What will you do? [Player can input: {inventory or attack}]')
def player_action(opponent)