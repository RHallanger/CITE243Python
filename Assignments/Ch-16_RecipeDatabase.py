"""
===========================================================
Program Name: 
Author: Robert Hallanger
Date: 2025-10-27
Description:
    This program performs [brief description of functionality].
    It is designed to [specific purpose or goal].
    
Usage:
    Run the script using Python 3.14. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import sqlite3
connect = sqlite3.connect('recipes.db', isolation_level=None)
connect.execute('CREATE TABLE IF NOT EXISTS recipe (dish TEXT NOT NULL, ingredients TEXT) STRICT')

def options():
    print('Recipe Database Menu:')
    print('1) List All Recipes')
    print('2) Add New Recipe')
    print('3) Search Recipes by Dish')
    print('4) Search Recipes by Ingredient')
    print('5) Remove Recipe') ### NEED TO ADD THIS
    print('6) Exit')
    choice = 0
    invalidCount = 0
    while choice not in ['1', '2', '3', '4', '5']:
        try:
            choice = input('Select an option (1-5): ')

        except:
            print('Invalid option, please select an option between 1-5')

        invalidCount += 1
        if invalidCount >= 5:
            print('\n' * 5)
            invalidCount = 0
            options()

    print('\n' * 5)
    match choice:
        case '1':
            list_recipes()
            print('\n' * 5)
            options()

        case '2':
            add_recipe()
            print('\n' * 5)
            options()

        case '3':
            search_dishes()
            print('\n' * 5)
            options()

        case '4':
            search_recipes()
            print('\n' * 5)
            options()

        case '5':
            print('Exiting the program. Goodbye!')
            exit()

        case _:
            print('Error, invalid option, bypassed exception.')
            print('\n' * 5)
            options()

def list_recipes():
    cursor = connect.execute('SELECT dish, ingredients FROM recipe')
    recipes = cursor.fetchall()
    if recipes:
        for dish, ingredients in recipes:
            print(f'Dish: {dish}\n')
    else:
        print('No recipes found.')

def add_recipe():
    dish = input('Enter the name of the dish: ')
    ingredients = input('Enter the ingredients (comma-separated): ')
    connect.execute('INSERT INTO recipe (dish, ingredients) VALUES (?, ?)', (dish, ingredients))
    print(f'\nRecipe for {dish} added successfully.')

def search_recipes():
    ingredient = input('Enter an ingredient to search for: ')
    cursor = connect.execute('SELECT dish, ingredients FROM recipe WHERE ingredients LIKE ?', (f'%{ingredient}%',))
    recipes = cursor.fetchall()
    if recipes:
        for dish, ingredients in recipes:
            ingredientList = ingredients.split(',')
            print(f'Dish: {dish}\nIngredients: ')
            for item in ingredientList:
                print(f' - {item.strip()}')
            print('\n')
    else:
        print(f'No recipes found with ingredient: {ingredient}')

def search_dishes():
    dish_name = input('Enter the name of the dish to search for: ')
    cursor = connect.execute('SELECT dish, ingredients FROM recipe WHERE dish LIKE ?', (f'%{dish_name}%',))
    recipes = cursor.fetchall()
    if recipes:
        for dish, ingredients in recipes:
            ingredientList = ingredients.split(',')
            print(f'Dish: {dish}\nIngredients:')
            for item in ingredientList:
                print(f' - {item.strip()}')
            print('\n')
    else:
        print(f'No recipes found for dish: {dish_name}')

options()