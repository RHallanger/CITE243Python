"""
===========================================================
Program Name: 2048 Spammer
Author: Robert Hallanger
Date: 2025-10-13
Description:
    This program performs a continuous spam of arrow keys into the web game of 2048.
    It is designed to entertain.
    
Usage:
    Run the script using Python 3.13. Ensure all dependencies
    are installed before execution.

===========================================================
"""

### We will be using Selenium to open firefox and send keystrokes.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### This function is how we will send keystrokes to the webpage
def gamePlayer():
    global spammer
    spammer.send_keys(Keys.ARROW_UP)
    spammer.send_keys(Keys.ARROW_RIGHT)
    spammer.send_keys(Keys.ARROW_DOWN)
    spammer.send_keys(Keys.ARROW_LEFT)

### This will open the webpage in firefox to have more control over.
browser = webdriver.Firefox()
browser.get('https://play2048.co/')

### Spammer will be used for inputs and Stop will be used to check for a play again button that is only present when we have lost.
# buttons = browser.find_elements(By.TAG_NAME, 'button')
spammer = browser.find_element(By.TAG_NAME, 'html')
stop = browser.find_elements(By.XPATH, "//button[text()='Play Again']")

### Spam up, right, down, left until we lose.
while not stop:
    gamePlayer()
    stop = browser.find_elements(By.XPATH, "//button[text()='Play Again']")

### We broke from the loop, so we lost.
print('Game Over...')