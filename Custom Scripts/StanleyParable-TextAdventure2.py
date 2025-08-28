
from time import sleep

#### Variables that are used :)
choice = 0
choice2 = 0
keypad = 0
keypadIncorrect = 0
loopCheck = 0
exceptCatch = False

################################### Functions for me to ease the scripting process###############################
def clear():
    #I couldn't get the import os clear/cls to work so I am just going to use this instead.
    print('\n' * 100 )

def nar(text):
    # This is to keep the dialogue in a clear viewing area. Well, mostly to let the narrator have his space.
    input(f"\n{text}\n")
    clear()

def looper():
    #Purpose of this function is to provide a condensed loopable option. It removes a lot of fun dialogue opportunity, but whatever.
    global loopCheck
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

def excepter(var):
    #similar to looper, but this handles if the player inputs anything that isn't a full number
    #WOOOOOOOOOOOO GOT IT TO WORK booyah
    global exceptCatch
    try:
        var = int(input('> '))
        return var

    except:
        if exceptCatch == False:
            exceptCatch = True
            print('Stanley, was so bad at entering numbers.\n\nIt was a surprise that he was not fired years ago.\n\nListen to me Stanley, you must enter a number for this to work.')

        else:
            print('I gave you an additional chance, and you squandered it Stanley.')
            print('Thank you for playing The Stanley Parable: Text Based Edition.')
            sleep(15)
            quit()

def tbd():
    #I put several hours into making the broom closet ending and realized that a lot of paths just don't have an ending yet... soooo placeholder.
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
nar('Something that he would never quite forget.')
nar('He had been at his desk for nearly an hour.\nWhen he realised that not one single order had arrived on his monitor for him to follow.')
nar('No one had showed up to give him instructions.\n\nCall a meeting.\n\nOr even say hi.')
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

    choice = excepter(choice)
    
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
nar('When Stanley came to a set of two open doors, he enetered the door on his left.')

while choice not in [1,2]: #Left or Right Decision
    print('What door does Stanley enter?')
    print('\n\n1) The Left Door\n\n2) The Right Door')

    choice = excepter(choice)

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

        choice2 = excepter(choice2)

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

############# Boss's office development because Python suggests that it is more readable to nest it :( #################
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

    if len(keypad) > 4 or len(keypad) < 4:
        nar('Stanley, it is supposed to be four digits.\nNo less and no more')
        nar('2-8-4-5')
    
    try:
        keypad = int(keypad)

    except:
        nar('Really Stanley?\nThose are not numbers.\n\nI am afraid that we will have to put our adventure on hold.')
        nar('Please come back when you have completed the basics to primary school.')
        nar('Thank you for playing The Stanley Parable: Text Advenutre, Non-Baby edition.')
        quit()

    match keypad:
        case 2845:
            nar('Yet incredibly, by simply by pushing random buttons on the keypad, Stanley happened to input the correct code by sheer luck.\n\nAmazing.')
            nar('He stepped into the newly opened passageway')
            pass

        case 8888:
            nar('8')

        case _:
            keypadIncorrect += 1
            match keypadIncorrect:
                case 1:
                    nar('Stanley just sat around twiddling his thumbs.\n\nTrying to input anything on the device was useless since he could never possibly know that the combination was:')
                    nar('2-8-4-5')

                case 2:
                    nar('2-8-4-5')

                case 3:
                    print('For god-')
                    sleep(2)
                    nar('But it turns out that the panel\'s emergency override kicked in and the door just opened by itself and Stanley got the hell along with the story\n\nWell whoop-de-doo!')
                    keypad = 2845

                case _:
                    nar('Stanley, by all accounts, refused the convenience of an emergency override and continued to input wrong numbers anyway.')

######### Mind Control Facility ########################
nar('Descending deeper into the building, Stanley realized he felt a bit peculiar.')
nar('It was a stirring of emotion in his chest as though he felt more free to think for himself.')
nar('To question the nature of his job.')
nar('Why did he feel this now,\nwhen for years it had never occured to him?')
nar('This question would not go unanswered for long.')

choice3 = 0

while choice3 not in [1,2]:
    print('Where does Stanley go now?')
    print('\n\n1) Escape Route\n\n2) Mind Control Facility')

    choice3 = excepter(choice3)

    if choice3 not in [1,2]:
        loopCheck += 1
        looper()
    pass

match choice3:
    case 1: #Escape Route
        tbd()

    case 2: #Mind Control Facility
        nar('Stanley walked straight ahead through the large door that read:\n\n\'Mind Control Facility\'')
        nar('Push ENTER to turn on the lights...')
        nar('The lights rose on an enourmous room packed with television screens.')
        nar('"What horrible secret did this place hold?" Stanley thought to himself.')
        nar('Did he have the strength to find out?')
        nar('Push ENTER to turn on the camera button...')
        nar('Now the monitors jumped to life, their true nature revealed.')
        nar('Each bore the number of an employee in the building.\n\nStanley\'s co-workers.')
        nar('The lives of so many individuals reduced to images on a screen,\n\nand Stanley one of them,\n\neternally monitored in this place where freedom meant nothing.')
        nar('This Mind Control Facility...\n\nIt was too horrible to believe.\n\nIt couldn\'t be true.')
        nar('Had Stanley really been under someone\'s control all this time?')
        nar('Was this the only reason he was happy with his boring job?')
        nar('That his emotions had been manipulated to accept it blindly?')
        nar('No!\n\nHe refused to believe it.\nHe couldn\'t accept it.')
        nar('His own life in someone else\'s control?\n\nNever!')
        nar('It was unthinkable, wasn\'t it?\n\nWas it even possible?')
        nar('Had he truly spent his entire life utterly blind to the world?')
        sleep(10)
        nar('But here was the proof.\n\nThe heart of the operation.')
        nar('Controls labeled with emotions:\n\nhappy\n\nsad\n\nor content')
        nar('Walking\n\nEating\n\nWorking\n\nAll of it monitored and commanded from this very place.')
        nar('And as the cold reality of his past began to sink in,\nStanley decided that this machinery would never again exert its terrible power over another human life.')
        nar('For he would dismantle the controls once and for all.')
        nar('And when at last he found the surce of the room\'s power, he knew it was his duty, his obligation, to put an end to this horrible place and to everything it stood for.')
