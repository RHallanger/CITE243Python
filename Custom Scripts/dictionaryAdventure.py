import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()

#################LISTS and DICTIONARIES
player_inventory = {'arrows': 12, 'gold coins': 42, 'rope': 1, 'torch': 6, 'dagger': 1, 'dubious meat': 999}
cultist_table = []
dragon_table = []

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

display_inventory(player_inventory)