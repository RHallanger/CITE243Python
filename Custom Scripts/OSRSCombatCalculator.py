from re import L


print('This is a story about a man named Stanley.\nEveryday, Stanley would go to his office and perform his simple task.\nHis task was to input on his keyboard the button indicated on his screen.\nHe absolutely loved it.\n\nHowever, one day, his computer was blank.\nIt was then that Stanley stood up and left his office to investigate.')
print('Options:\n\n1- Close the door.\n\n2- Walk into the hallway.')
print('\nStanley, due to the medium we are telling this story, you will have to input the number corresponding to your choice.\n')
loopCheck = 0
choice1 = 0


#LEAVE THE OFFICE LOOP
while choice1 < 1 or choice1 > 2:
    try:
        choice1 = int(input('Selection > '))

    except:
        print('St-Stanley? Did you really just input something other than a full number?\n\nWell, I must say that is rather bold of you.\nTo think that I went through all of this effort to tell a story and you just throw it away the first instance you get.\nThis won\'t do...\n\nI\'m closing the game.')
        quit()

    if (choice1 < 1 or choice1 > 2) and loopCheck < 5:
        print('Stanley, that is not a valid option.\nPlease try again.')
        loopCheck += 1

    elif (choice1 < 1 or choice1 > 2) and loopCheck >= 5:
        print('Stanley, I\'m sorry, but I simply have better things to do than repeating the same line to you.\nI\'m closing the game.')
        quit()

    else:
        pass

#Results of making a vlaid selection
match choice1:
    case 1:
        print('Too scared of the prospect of being found deserting his post. Stanley hid away from the world in hopes the letters would appear on his monitor.\nThey did not come.\nWhat were you expecting Stanley?')
        quit()

    case 2:
        print('As Stanley stepped out of his office, he noticed that all of his coworkers were gone.\nPerhaps he had missed a memo.\nStanley proceeded to the meeting room.\n\nSuddenly, Stanley came across a room with two open doors.\nStanley took the door on his left.')
        print('Options:\n1- Left Door\n2- Right Door')
        pass

choice1 = 0
LoopCheck = 0

#LEFT OR RIGHT DOOR LOOP
while choice1 < 1 or choice1 > 2:
    try:
        choice1 = int(input('Selection > '))
    except:
        print('St-Stanley? Did you really just input something other than a full number?\n\nWell, I must say that is rather bold of you.\nTo think that I went through all of this effort to tell a story and you just throw it away the first instance you get.\nThis won\'t do...\n\nI\'m closing the game.')
        quit()
    if (choice1 < 1 or choice1 > 2) and LoopCheck < 5:
        print('Stanley, that is not a valid option.\nPlease try again.')
        LoopCheck += 1
    elif (choice1 < 1 or choice1 > 2) and LoopCheck >= 5:
        print('Stanley, you were doing so well. Yet, I am sorry, but I simply have better things to do than repeating the same line to you.\nI must close the game.\n\nPlease return when you or someone else is capable of selecting an option.')
        quit()
    else:
        pass

#RESULTS OF LEFT OR RIGHT DOOR
match choice1:
    case 1:
        print('Stanley walked through the door on his left.\n\nThe meeting room was empty.\nWas it a holiday?\nWas it the weekend?\nTo resolve these questions, Stanley must speak to his boss.\n\nStanley leaves the meeting room...')
        print('Options:\n1- Go upstairs to the Boss\'s office.\n2- Go downstairs.\n3- Go into the broom closet.')
        pass
    case 2:
        print('Stanley walked through the door on his right.\n\nHe knew this was not the correct way.\nPerhaps he wanted to go and admire the beauty of the break room.\n\nYes yes, quite the fabulous room.\n\nOkay Stanley lets get back on track.')
        print('Options:\n1- Go through the shortcut to the meeting room.\n2- Continue to explore.')
        pass
