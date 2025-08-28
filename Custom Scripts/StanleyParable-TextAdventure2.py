from os import system, name
from random import choice
from statistics import linear_regression
from time import sleep

global loopCheck #This is to keep track of how many times they loop through the looper function
loopCheck = 0

def clear():
    print('\n' * 100 )

def nar(text):
    input(f"\n{text}\n")
    clear()

def looper():
    #Purpose of this function is to provide a condensed loopable option. It removes a lot of fun dialogue opportunity, but whatever.
    clear()
    match loopCheck:
        case 1: #It's not a number they can use, so loop again
            nar('When given two options, Stanley decided to pick neither.\n\nDo you feel good not picking option one or option two?')
            nar('I will give you another chance...')

        case 2: #It's not a number they can use, so loop again
            nar('Seriously Stanley?\n\nYou\'re really going to make me do this again?')
            nar('Fine, I\'ll give you another chance...')

        case 3: #It's not a number they can use, so loop again
            nar('Stanley, I\'m starting to think you\'re doing this on purpose now.\n\nIs that it?')
            nar('You\'re just trying to mess with me?\n\nWell I\'m not going to take it anymore.\n\nBut I\'ll give you one last chance...')

        case 4: #It's not a number they can use, so loop again
            nar('This is your last chance Stanley.\n\nChoose wisely.\n\nOr not wisely.\n\nI don\'t care anymore.')
            nar('But this is it.\n\nOne more time and that\'s it.')

        case 5: #They've looped too many times, so end the game
            nar('Stanley, paralyzed with the seemingly infinite possibility of options could move no further.')
            nar('How could Stanley possibly pick just one?')
            nar('Unable to decide, Stanley simply stood there forever.')
            nar('Well Stanley, you ruined my story.')
            nar('Are you happy?')
            nar('Goodbye Stanley...')
            quit()

        case _:
            quit()

def tbd():
    nar('And Stanley...')
    nar('Oh hang on, something isn\'t right.')
    nar('The next page is simply blank.')
    nar('Oh, here is something on my desk.\n\nA sticky note from the developers.')
    nar('Yada yada, huhn hun hnn...\n"We are sorry to say that we did not get this far into the game\nThis is just a student project I did for fun."')
    nar('A student project? Just for fun?!')
    nar('Well Stanley, I guess this is the end of the line for us both.\nMaybe there will be an update in the future?\n\n"Don\'t bet on it."')
    nar('Suffice it to say, thank you for playing The Stanley Parable: Text Adventure.')
    quit()

clear() #This one is just to frame the text at the bottom of the screen
print('This is the story of a man named Stanley.')
input('Press ENTER to continue...')
clear()
nar('Stanley worked for a company in a big building where he was Employee Number 427.')
nar('Employee Number 427\'s job was simple.\nHe sat at his desk in Room 427, and he pushed buttons on a keyboard.')
nar('Orders came to him through a monitor on his desk.')
nar('Telling him what buttons to push, how long to push them, and in what order.')
nar('This is what Employee Number 427 did every day of every month of every year.')
nar('And although others might have considered it soul-rending.\nStanley relished every moment that the orders came in, as though he had been made exactly for this job.')
nar('And Stanley was happy.')
nar('And then one day, something very peculiar happened.')
nar('Something that would forever change Stanley.')
nar('Something that he would never quite foreget.')
nar('He had been at his desk for nearly an hour.\nWhen he realised that not one single order had arrived on his monitor for him to follow.')
nar('No one had showed up to give him instructions.\nCall a meeting.\nOr even say hi.')
nar('Never in all his years at the company had this happened.\nThis complete isolation.')
nar('Something was very clearly wrong.')
nar('Shocked, frozen solid, Stanley found himself unable to move for the longest time.')
nar('But as he came to his wits and regained his senses.')
nar('He got up from his desk and stepped out of his office.')

#Alright, first decision time
#These variables seem very self 
choice = 0

while choice not in [1,2]: #This will let them keep looping until an option is selected
    print('What should Stanley do?')
    print('Hint: Use numbers to indicate your choice.')
    print('\n\n1) Leave the office\n\n2) Close the door')

    try: #Catch them if they enter something weird
        choice = int(input('> '))

    except:
        print('Are you mocking me Stanley?\n\nWhen I told you to enter a number, you decided now would be the time for letters?\n\n\nIt was simply too much free will.\nGood bye Stanley...')
        sleep(15)
        quit()

    if choice not in [1,2]:
        loopCheck += 1
        looper() #This function will handle the looping and dialogue for invalid options)

    pass

clear()
match choice: #Results of leaving his office
    case 1: #Leave the office
        nar('All of his co-workers were gone.\nWhat could it mean?')
        nar('Stanley decided to go to the meeting room.\n\nPerhaps he had simply missed a memo.')
        pass

    case 2: #Close the door
        tbd()

choice = 0 #Now is the important moment in a coders life to choose, nest hell or variable hell... We will see
exceptCatch = False
nar('When Stanley came to a set of two open doors, he enetered the door on his left.')

while choice not in [1,2]: #Left or Right Decision
    print('What door does Stanley enter?')
    print('\n\n1) The Left Door\n\n2) The Right Door')

    try:
        choice = int(input('> '))

    except:
        if exceptCatch == False:
            exceptCatch = True
            print('Stanley, was so bad at entering numbers.\n\nIt was a surprise that he was not fired years ago.\n\nListen to me Stanley, you must enter a number for this to work.')

        else:
            print('I gave you an additional chance, and you squandered it Stanley.')
            print('Thank you for playing The Stanley Parable: Text Based Edition.')
            sleep(15)
            quit()

    if choice not in [1,2]:
        loopCheck += 1
        looper()

    pass

clear()
match choice: #Left or Right Results
    case 1: #Left door
        nar('Yet there was not a single person here either.')
        nar('Feeling a wave of disbelief.\nStanley decided to go up to his boss\'s office hoping he might find an answer there.')
        nar('Coming to a staircase, Stanley walked upstairs to his boss\'s office.')
        pass

    case 2: #Right door
        tbd()

choice2 = 0
#####################################LEFT DOOR PATH#####################################
if choice == 1: #If they chose the left door
    while choice2 not in [1,2,3]: #Next Room Decision from the meeting room
        print('Where does Stanley go now?')
        print('\n\n1) Upstairs\n\n2) Downstairs\n\n3) The Broom Closet')
        try:
            choice2 = int(input('> '))

        except:
            if exceptCatch == False:
                exceptCatch = True
                nar('Stanley, you do realize that you didn\'t type a number right?')
                nar('Here have another try.')
            else:
                nar('Ooooookay Stanley, you gave it your best shot.\n\nBut I need someone who can follow simple instructions.\n\nGoodbye Stanley...')
                quit()

        if choice2 not in [1,2,3]:
            loopCheck += 1
            looper()
    pass

clear()
match choice2: #Results of Boss's Office, Downstairs, or Broom Closet
    case 1: #Boss's Office
        pass
    case 2: #Downstairs
        tbd()
    case 3: #Broom Closet
        tbd()

nar('Stepping into his manager\'s office\nStanley was once again stunned to discover not an indication of any human life.')
nar('Shocked, unraveled, Stanley wondered in disbelief who orchestrated this.')
nar('What dark secret was being held from him?')
nar('What he could not have known was that the keypad behind the boss\'s desk guarded the terrible truth that his boss had been keeping from him.')
nar('And so the boss had assigned it an extra secret pin number: 2-8-4-5')
nar('But, of course, Stanley couldn\'t possibly have known this.')

while int(keypad) != 2845:
    print('Enter a four digit code to the keypad.')
    print('Hint: formated as "1111"')
    keypad = input('> ')

    if keypad.len() > 4 or keypad.len() < 4:
        nar('Stanley, it is supposed to be four digits.\nNo less and no more')
        nar('2-8-4-5')

    if keypad == 2845:
        nar()

    elif keypad == 8888:
        nar()

    else:
        nar('Nothing happened')