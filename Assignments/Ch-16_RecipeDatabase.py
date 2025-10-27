"""
===========================================================
Program Name: Recipe Database Manager
Author: Robert Hallanger
Date: 2025-10-27
Description:
    This program is a simple suite of tools.
    It is designed to make adjustments to an SQLite database.
    
Usage:
    Run the script using Python 3.13. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import sqlite3
connect = sqlite3.connect('recipes.db', isolation_level=None)
connect.execute('CREATE TABLE IF NOT EXISTS recipe (dish TEXT NOT NULL, ingredients TEXT) STRICT')
### Made a file named recipes.db with a new table named recipe.

### This menu will cycle constantly with all of the functions necessary to add, search/view, and remove recipes.
def options():
    # First we will show the user their options and loop them until they give a valid input.
    print('Recipe Database Menu:')
    print('1) List All Recipes')
    print('2) Add New Recipe')
    print('3) Search Recipes by Dish')
    print('4) Search Recipes by Ingredient')
    print('5) Remove Recipe') ### NEED TO ADD THIS
    print('6) Exit')

    choice = 0
    invalidCount = 0 # This counter is to break up the text to maintain readability of the screen.

    while choice not in ['1', '2', '3', '4', '5', '6']:
        choice = input('Select an option (1-6): ')
        invalidCount += 1

        if invalidCount >= 5:
            print('\n' * 5)
            invalidCount = 0
            options()

    print('\n' * 5)
    # Spaces out the screen for readability of the next function.
    # This part will take the user's choice and call the appropriate function and afterwards, return to the options menu.
    match choice:
        case '1':
            # Lists only the names of the dishes for quicker viewing.
            list_recipes()
            print('\n' * 5)
            options()

        case '2':
            # Allows the user to add a dish and the associated ingredients.
            add_recipe()
            print('\n' * 5)
            options()

        case '3':
            # Searches for recipes by dish name.
            search_dishes()
            print('\n' * 5)
            options()

        case '4':
            # Searches for recipes by ingredient.
            search_recipes()
            print('\n' * 5)
            options()

        case '5':
            # Removes a recipe from the database.
            remove_recipe()
            print('\n' * 5)
            options()

        case '6':
            # Closes the program.
            print('Exiting the program. Goodbye!')
            exit()

        case _:
            # Catches any invalid input that may have bypassed the initial checks.
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

def remove_recipe():
    dish = input('Enter the name of the dish to remove: ')
    cursor = connect.execute('SELECT * FROM recipe WHERE dish = ?', (dish,))
    recipe = cursor.fetchone()
    if recipe:
        connect.execute('DELETE FROM recipe WHERE dish = ?', (dish,))
        print(f'Recipe for {dish} removed successfully.')
    else:
        print(f'No recipe found for dish: {dish}')

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

# Start the program by calling the options function.
options()