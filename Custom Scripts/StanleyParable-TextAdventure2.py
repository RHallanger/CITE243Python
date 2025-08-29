
from time import sleep

############################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Finish Broom Closet Ending

#### Variables that are used :)
choice = 0
loopCheck = 0
broomClosetCheck = 0
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
            print('Thank you for playing The Stanley Parable: Text Adventure.')
            sleep(5)
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

def broomLoop(): #Special loop for broom closet
    global broomClosetCheck
    while choice not in [1,2]:
        print('What does Stanley do?')
        print('\n\n1) Wait\n\n2) Leave')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

    match choice:
        case 1:
            broomClosetCheck += 1
            sceneBroomCloset()
        case 2:
            clear()
            broomClosetCheck = 100
            scenePostMeeting()


################## SCENES MANAGER! ##########################

def sceneMindControl():
    choice = 0
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
    nar('But here was the proof.\n\nThe heart of the operation.')
    nar('Controls labeled with emotions:\n\nhappy\n\nsad\n\nor content')
    nar('Walking\n\nEating\n\nWorking\n\nAll of it monitored and commanded from this very place.')
    nar('And as the cold reality of his past began to sink in,\nStanley decided that this machinery would never again exert its terrible power over another human life.')
    nar('For he would dismantle the controls once and for all.')
    nar('And when at last he found the surce of the room\'s power, he knew it was his duty, his obligation, to put an end to this horrible place and to everything it stood for.')
    while choice not in [1,2]:
        print('What do you do to the Mind Control Console?')
        print('\n\n1) ON\n\n2) OFF')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

        pass

    clear()
    match choice: #Mind Control On or Off
        case 1: #ON
            ################################### CONTROL ENDING#########################################
            nar('Oh Stanley, you didn\'t just activate the controls, did you?')
            nar('After they kept you enslaved all these years.\nYou go and you try to take control of the machine for yourself.')
            nar('Is that what you wanted?\n\nControl?')
            sleep(2)
            nar('Oh... Stanley.\n\nI applaud your effort, I really do.')
            nar('But you need to understand.\nThere\'s only so much that machine can do.')
            nar('You were supposed to let it go, turn the controlls off, and leave.')
            nar('If you want to throw my story off track, you\'re going to have to do much better than that.') #much included in voice, but not subtitles
            nar('I\'m afraid you don\'t have nearly the power you think you do.')
            nar('For example\n\nAnd I believe you\'ll find this pertinent...')
            nar('Stanley suddenly realized that he had just initiated the network\'s emergency detonation system.')
            nar('In the even that this machine is activated without proper DNA identification\n\nNuclear detonators are set to explode, eliminating the entire complex.')
            nar('How long until detonation, then?')
            nar('Hmm...\nLet\'s say...\nUm...')
            print('2:00')
            nar('Two minutes.')
            print('1:50')
            nar('Ah, now this is making things a little more fun, isn\'t it, Stanley?')
            print('1:40')
            nar('It\'s your time to shine!\n\nYou are the star!')
            print('1:30')
            nar('It\'s your story now!\n\nShape it to your heart\'s desires.')
            print('1:20')
            nar('Oh, this is much better than what I had in mind!')
            print('1:10')
            nar('What a shame we have so little time left to enjoy it.')
            print('1:00')
            nar('Mere moments until the bomb goes off, but what precious moments each one of them is!')
            print('0:50')
            nar('More time to talk about your\nAbout me\nWhere we\'re going\nWhat all this means.')
            print('0:40')
            nar('I barely know where to start!')
            print('0:30')
            nar('What\'s that?\n\nYou\'d like to know where your co-workers are?')
            print('0:20')
            nar('A moment of solace before you\'re obliterated?')
            print('0:10')
            nar('Alright.\nI\'m in a good mood, and you\'re going to die anyway.')
            print('0:09')
            nar('I erased them.')
            print('0:08')
            nar('I turned off the machine.')
            print('0:07')
            nar('I set you free.')
            print('0:06')
            nar('Of course, that was merely in this instance of the story.')
            print('0:05')
            nar('Sometimes when I tell it, I simply let you sit there in your office forever.\nPushing buttons endlessly and then dying alone.')
            print('0:04')
            nar('This is not a challenge.\nIt\'s a tragedy.')
            print('0:03')
            nar('You wanted to control this world; that\'s fine.')
            print('0:02')
            nar('But I\'m going to destroy it first, so you can\'t.')
            nar('0:01')
            print('And believe me, I will be laughing at every second of your inevitable life\nfrom the moment we fade in, until the moment I say: \'Happily ever af-\'')
            sleep(5)
            quit()
        case 2: #OFF
            ########################################## FREEDOM ENDING ######################################
            nar('Blackness.')
            nar('And a rising chill of uncertainty.')
            nar('Was it over?')
            nar('Yes!\n\nHe had won!')
            nar('He had defeated the machine, unshackled himself from someone else\'s command.')
            nar('Freedom was mere moments away.')
            nar('And, yet, even as the immense door slowly opened...')
            nar('Stanley reflected on how many puzzles still lay unsolved.')
            nar('Where had his co-workers gone?')
            nar('How had he been freed from the machine\'s grasp?')
            nar('What other mysteries did this strange building hold?')
            nar('But as sunlight streamed into the chamber, he realized none of this mattered to him.')
            nar('For it was not knowledge, or even power, that he had been seeking.')
            nar('But happiness.')
            nar('Perhaps his goal had not been to understand, but to let go.')
            nar('No longer would anyone tell him where to go, what to do, or how to feel.')
            nar('Whatever life he lives, it will be his.')
            nar('And that was all he needed to know.')
            nar('It was, perhaps, the only thing worth knowing.')
            nar('Stanley stepped through the open door.')
            sleep(3)
            nar('Stanley felt the cool breeze upon his skin, the feeling of liberation, the immense possibility of the new path before him.')
            nar('This was exactly the way, right now, that things were meant to happen.')
            nar('And Stanley was happy.')
            quit()

def sceneBossOffice():
    keypad = 0
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
                clear()
                nar('Yet incredibly, by simply by pushing random buttons on the keypad, Stanley happened to input the correct code by sheer luck.\n\nAmazing.')
                nar('He stepped into the newly opened passageway')
                pass

            case 8888:
                clear()
                nar('8')

            case _:
                keypadIncorrect += 1
                match keypadIncorrect:
                    case 1:
                        clear()
                        nar('Stanley just sat around twiddling his thumbs.\n\nTrying to input anything on the device was useless since he could never possibly know that the combination was:')
                        nar('2-8-4-5')

                    case 2:
                        clear()
                        nar('2-8-4-5')

                    case 3:
                        clear()
                        print('For god-')
                        nar('But it turns out that the panel\'s emergency override kicked in and the door just opened by itself and Stanley got the hell along with the story\n\nWell whoop-de-doo!')
                        keypad = 2845

                    case _:
                        nar('Stanley, by all accounts, refused the convenience of an emergency override and continued to input wrong numbers anyway.')

    sceneMindControlSplit()

def sceneInsanity():
    nar('But Stanley just couldn\'t do it.')
    nar('He considered the possibility of facing his boss...\n\nAdmitting that he had left his post during work hours.')
    nar('He might be fired for that.')
    nar('And in such a competitive economy, why had he taken that risk?')
    nar('All because he believed that everyone had vanished?')
    nar('His boss would think that he was crazy.')
    nar('And then something occured to Stanley.')
    nar('"Maybe" he thought to himself.\n\n"Maybe I am crazy."')
    nar('"All of my coworkers blinking mysteriously out of existence in a single moment for no reason at all."')
    nar('"None of it made any logical sense."')
    nar('And as Stanley pondered this, he began to make other strange observations.')
    nar('For example, why couldn\'t he see anything but text?')
    nar('Why is he not allowed to go back on a decision?')
    nar('"No," Stanley said to himself.\n\n"This is all too strange."\n\n"This can\'t be real."')
    nar('And at last he came to the conclusion that had been on the tip of his tongue.\nHe just hadn\'t found the words for it.')
    nar('"I\'M DREAMING!" He yelled.')
    nar('"This is all a dream!" Ah, what a relief Stanley felt to have finally found an answer.\nAn explanation.\nHis co-workers weren\'t actually gone.')
    nar('He wasn\'t going to lose his job.')
    nar('He wasn\'t crazy after all.')
    nar('And he thought to himself, "I suppose I\'ll wake up soon."\n\n"I\'ll have to go back to my boring real life job of pushing buttons."')
    nar('"I may as well enjoy this while I\'m still lucid."')
    nar('So, he imagined himself flying and began to gently float above the ground.')
    nar('Then he imagined himself flying through space on a magical starfield.\nAnd it too appeared.\n\nIt was so much fun.')
    nar('And Stanley marveled that he had still not woken up.')
    nar('How was he remaining so lucid?')
    nar('And then perhaps the strangest question of them all entered Stanley\'s head.')
    nar('One he was amazed he hadn\'t asked sooner.')
    nar('"Why is there a voice in my head dictating everything that I am doing and thinking?"')
    nar('Now the voice was describing itself being considered by Stanley who found it particularly strange.')
    nar('"I\'m dreaming about a voice describing me thinking about how it\'s describing my thoughts." He thought.')
    nar('And while he thought it all very odd, and wondered if this voice spoke to all people in their dreams...')
    nar('The truth was that of course this was not a dream.')
    nar('How could it be?')
    nar('Was Stanley simply deceiving himself?\n\nBelieving that if he\'s asleep then he doesn\'t have to take responsibility for himself?')
    nar('Stanley is as awake right now as he\'s ever been in his life.')
    nar('Now hearing the voice speak these words was quite a shock to Stanley.')
    nar('After all, he knew for certain, beyond a doubt that this was in fact a dream.')
    nar('"Did the voice not see him float and make the magical stars just a moment ago?"')
    nar('"How else would the voice explain all that?"')
    nar('"This voice was a part of himself too!"')
    nar('"SURELY! SURELY!"\n\nIf he could just...')
    nar('He would prove it.')
    nar('He would prove that he was in control.\n\nThat this was a dream.')
    nar('So he closed his eyes gently and invited himself to wake up.')
    nar('He felt the cool weight of the blanket on his skin.\n\nThe press of the matress on his back.')
    nar('The fresh air of the world outside this one.')
    nar('"Let me wake up." He thought to himself.')
    nar('"I\'m through with this dream."\n\n"I wish it to be over."\n\n"Let me go back to my job."\n\n"Let me continue pushing the buttons."')
    nar('"Please, it is all I want."')
    nar('"I want my apartment,\nand my wife,\nand my job."')
    nar('"All I want is my life exactly the way it\'s always been."')
    nar('"My life is normal."')
    nar('"I am normal."')
    nar('"Everything will be fine."')
    nar('"I am okay."')
    nar('Stanley began screaming.')
    nar('"PLEASE! SOMEONE WAKE ME UP!"')
    nar('"MY NAME IS STANLEY!"\n\n"I HAVE A BOSS!"\n\n"I HAVE AN OFFICE!"')
    nar('"I AM REAL!"\n\n"PLEASE, JUST SOMEONE TELL ME I AM REAL!"')
    nar('"I MUST BE REAL! I MUST BE-"\n\n"CAN ANYONE HEAR MY VOICE?"')
    nar('"WHO AM I? WHO AM I?"')
    nar('And then everything went black.')
    clear()
    sleep(2)
    nar('Press ENTER to continue...')
    nar('This is a story about a woman named Mariella.')
    nar('Mariella woke up on a day like any other.')
    nar('She rose, got dressed, gathered her belongings, and walked to her place of work.')
    nar('But on this particular day,\nher walk was interrupted by the body of a man who had stumbled through town talking and screaming to himself.')
    nar('And then collapsed dead on the sidewalk.')
    nar('And although she would soon turn to go call for an ambulance.')
    nar('For just a few brief moments, she considered the strange man.')
    nar('He was obviously crazy.\n\nThis much she knew.')
    nar('Everyone knows what crazy people look like.')
    nar('And in that moment, she thought to herself how lucky she was to be normal.')
    nar('"I am sane."\n\n"I am in control of my mind."')
    nar('"I know what is real and what isn\'t."')
    nar('It was comforting to think this.')
    nar('And in a certain way, seeing this man made her feel better.')
    nar('But then she remembered the meeting she had scheduled for that day.')
    nar('The very important people who\'s impressions of her would affect her career and by extension...')
    nar('The rest of her life.')
    nar('She had no time for this.')
    nar('So, it was only a moment that she stood there staring down at the body.')
    nar('And then she turned and ran.')
    quit()

def sceneEscapeRoute():
    global loopCheck
    choice = 0

    nar('Although this passage way had escape written on it,\n\nThe truth was that, at the end of this hall, Stanley would meet his violent death.')
    while choice not in [1,2]:
        print('What does Stanley do?')
        print('\n\n1) Continue forward\n\n2) Turn around')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

    match choice:
        case 1:
            pass
        case 2:
            clear()
            sceneMindControlSplit()

    clear()
    nar('The door behind him was not shut.\n\nStanley still had every opportunity to turn around and get back on track.')
    choice = 0
    while choice not in [1,2]:
        print('What does Stanley do?')
        print('\n\n1) Continue forward\n\n2) Turn around')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

    match choice:
        case 1:
            pass
        case 2:
            clear()
            sceneMindControlSplit()

    clear()
    nar('At this point, Stanley was making a concious concerted effort to walk forward and willingly confront his death.')
    choice = 0
    while choice not in [1,2]:
        print('What does Stanley do?')
        print('\n\n1) Continue forward\n\n2) Turn around')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

    match choice:
        case 1:
            pass
        case 2:
            clear()
            sceneMindControlSplit()

    clear()
    nar('As the machine whirred into motion and Stanley was inched closer and closer to his demise.\n\nHe reflected that his life has been of no consequence whatsoever')
    nar('Stanley can\'t see the bigger picture.\n\nHe doesn\'t know the real story.')
    nar('Trapped forever in his narrow vision of what this world is.')
    nar('Perhaps his death was of no great loss like plucking the eyeballs from a blind man.')
    nar('So he resigned and willingly accepted this violent end to his brief and shallow life.')
    nar('Farewell Stanley')
    nar('"Farewell Stanley," cried the narrator as Stanley was led helplessly into the enormous metal jaws.')
    nar('In a single visceral instant, Stanley was obliterated as the machine crushed every bone in his body.\n\nKilling him instantly.')
    nar('And yet it would be just a few minutes before Stanley would restart the game back in his office as alive as ever.')
    nar('What exactly did the narrator think he was going to accomplish?')
    nar('When every path you can walk has been created for you long in advance,\n\nDeath becomes meaningless.')
    nar('Making life the same.')
    nar('Do you see now?\n\nDo you see that Stanley was already dead from the moment he hit start?')
    nar('Oh look at these two.\n\nHow they wish to destroy one another.\n\nHow they wish to control one another.\n\nHow they both wish to be free.')
    nar('Can you see?\nCan you see how much they need one another?')
    nar('No.\n\nPerhaps not.')
    nar('Sometimes these things cannot be seen.')
    nar('But listen to me, you can still save these two.')
    nar('You can stop the program before theyboth fail.')
    nar('Click the \'x\' and quit.')
    nar('There\'s no other way to beat this game.')
    nar('As long as you move forward, you will be walking someone else\'s path.')
    nar('Stop now and be your only true choice.\n\nWhatever you do choose it, don\'t let time choose for you.')
    nar('DON\'T LET TIME-')
    sleep(999)
    quit()

def sceneMindControlSplit():
    global loopCheck
    choice = 0
    while choice not in [1,2]:
        print('Where does Stanley go now?')
        print('\n\n1) Escape Route\n\n2) Mind Control Facility')

        choice = excepter(choice)

        if choice not in [1,2]:
            loopCheck += 1
            looper()

        pass

    clear()
    match choice:
        case 1: #Escape Route
            sceneEscapeRoute()

        case 2: #Mind Control Facility
            sceneMindControl()

def scenePostMeeting():
    global loopCheck
    choice = 0
    while choice not in [1,2,3]: #Next Room Decision from the meeting room
        print('Where does Stanley go now?')
        print('\n\n1) Upstairs\n\n2) Downstairs\n\n3) The Broom Closet')

        choice = excepter(choice)

        if choice not in [1,2,3]:
            loopCheck += 1
            looper()

    clear()
    match choice:
        case 1: #Boss's Office
            sceneBossOffice()

        case 2: #Downstairs and Insanity Ending
            sceneInsanity()

        case 3: #Broom Closet
            sceneBroomCloset()

def sceneBroomCloset():
    global broomClosetCheck
    match broomClosetCheck:
        case 0:
            nar('Stanley stepped into the broom closet, but there was nothing here, so he turned around and got back on track.')
            broomLoop()
        case 1:
            nar('There was nothing here.')
            nar('No choice to make,\nno path to follow,\njust an empty broom closet.')
            nar('No reason to still be here.')
            broomLoop()
        case 2:
            nar('It was baffling that Stanley was still just sitting in the broom closet.')
            

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
        sceneBossOffice()

    case 2: #Downstairs and Insanity Ending
        sceneInsanity()

    case 3: #Broom Closet
        tbd()