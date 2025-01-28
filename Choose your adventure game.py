# Choose your adventure game
import time

def intro():    # INTRODUCTION
    name = input('''Enter your adventurer's name: 
''')
    print(
name + ''' stood at the entrance of Ravenwood Manor, 
a crumbling estate draped in shadows.''')
    
    time.sleep(2)

    print('''
The air smells of damp wood and something faintly metallic.
The sound of your heartbeat is almost drowned out by the distant sound of a clock ticking somewhere deeper inside.

Before you, the iron gates creaked open as if compelled 
by an unseen force, swaying your mind and pulling you in.
          ''')


def ironGate(): # Checks the user input for their choice
    
    userInput1 = ''

    while userInput1 != '1' and userInput1 != '2':
        print('1. March onward')
        print('2. ...')

        userInput1 = input()

    return int(userInput1)




def checkChoice1(choice1):  # Prints the appropriate path for the user's input
    if choice1 == 1:
        ironGateChoice1()
    else:
        ironGateChoice2()




def ironGateChoice2():  # LEAVE ENDING (iron gate)
    print('''
You can't shake the feeling that the manor itself is alive, watching you.
Perhaps leaving immediately was the wisest choice...
          ''')
    
    time.sleep(5)

    print("Ending: Better Safe Than Sorry.")

    time.sleep(2)

    playAgain()




def ironGateChoice1():  # 2nd Choice
    print('''
You find yourself in the grand yet decaying entrance hall.
Moonlight filters through shattered stained-glass windows,
casting fractured colors across the dusty floor.
          ''')
    
    time.sleep(5)

    print("Before you, two distinct paths present themselves: ")

    time.sleep(3)
          
    

def entranceChoice():   # Checks the user input for their chosen path
    userInput2 = ''

    while userInput2 != '1' and userInput2 != '2':
        print('''
1. The Grand Staircase
2. The Hallway
          ''')
        
        userInput2 = input()

    return int(userInput2)




def checkChoice2(choice2):  # Prints the appropriate path for the user's input at Entrance Hall
    if choice2 == 1:
        lockedDoor()
    else:
        hallway()        


    
def lockedDoor():   # locked door path after staircase
    print('''You make your way up the grand staircase...''')

    time.sleep(4)
    
    print('''
Only to find yourself obstructed by a locked door.''')

    time.sleep(3)



def staircaseChoice():  # Gives the player the choice to go back to the Entrance Hall at the locked door
    
    userInput2a = ''

    while userInput2a != '1':
        print('''
1. Make your way back down the staircase to the entrance hall''')
        
        userInput2a = input()

    return int(userInput2a)



def checkChoice2a(choice2a):    
    if choice2a == 1:  # Go back to the entrance hall
        new_choice = entranceChoice()  # Get the new choice
        checkChoice2(new_choice)  # Process the new choice




def hallway():  # Prints the appropriate path for the user's input to Hallway
    print('''
You step into the left hallway,
the flickering candelabra drawing you closer.''')
    
    time.sleep(5)

    print('''
The whispers grow louder, but they’re unintelligible, 
like the voice of a distant crowd. 
''')
    
    time.sleep(5)

    print('''Halfway down the hall, you notice a door slightly ajar on your right,
revealing what looks like a dimly lit study. ''')
    
    time.sleep(6)

    print('''
At the same time, the candelabra’s light begins to fade,
and ahead you see another door with faint scratching sounds coming from behind it.
''')

    time.sleep(4)

    print('Do you:')

    time.sleep(3)



def hallwayChoice():    # Gives the player the choice to go into the Study or investigate Scratching Door
    userInput3 = ''

    while userInput3 != '1' and userInput3 != '2':
        print('''
1. Enter the study
2. Investigate the Scratching Door''')
        
        userInput3 = input()

    return int(userInput3)


def checkChoice3(choice3):  # Prints the appropriate path for the user's input in the hallway
    if choice3 == 1:
        study()
    else:
        scratchingDoor()



def study():
    print('''
You push open the door to the study,
and the scent of aged books and smoldering firewood greets you. ''')
    
    time.sleep(5)

    print('''
The room is dimly lit by a dying fire in the hearth, 
casting long shadows across the walls. 
''')
    
    time.sleep(5)

    print('''
Shelves of dusty tomes line the walls, 
interrupted by a grand, mahogany desk in the center.''')

    time.sleep(5)

    print('On the desk, you see:')

    time.sleep(3)


def leatherJournal():
    print('''
You flip open the journal, revealing frantic handwriting sprawled across its pages.
''')
    
    time.sleep(5)

    print('''
The entries speak of an ancient curse tied to the manor, 
one that feeds on the souls of those who linger too long.
''')
    
    time.sleep(5)

    print('''As you turn to the final entry, the ink begins to bleed off the page, 
forming the words:
''')

    time.sleep(7)

    print('''"It watches. It knows. Flee while you still can."
''')

    time.sleep(5)

    print('''The fire dies out, plunging the room into darkness. 
You hear the sound of something heavy breathing right behind you.

''')
    
    time.sleep(7)

    print('''Ending: The Darkness Takes You.''')

    time.sleep(2)

    playAgain()


def theKey():
    print('''You snatch the ornate key from the desk, 
its cold metal sending a chill through your fingers. 
''')
    
    time.sleep(5)

    print('''
The fire flares brightly for a brief moment, 
revealing a hidden door behind one of the bookshelves. 
The key fits perfectly into the lock.
''')

    time.sleep(7)

    print('''You swing the door open to reveal a hidden passage leading outside. 
Without a second thought, you bolt through the passage and into the safety of the night. ''')
    
    time.sleep(7)

    print('''
As you glance back, the Manor looms in the distance, 
its windows glowing faintly as if in silent acknowledgment of your escape.
''')
    
    time.sleep(6)

    print("Ending: You Escape with the Key to the Manor's Secrets.")

    time.sleep(2)

    playAgain()


def studyChoice():

    userInput4 = ''

    while userInput4 != '1' and userInput4 != '2':
        print('''
1. A leather-bound journal, its pages yellowed and stained.
2. A strange, ornate key, glinting faintly in the firelight.''')
        
        userInput4 = input()

    return int(userInput4)


def checkChoice4(choice4):
    if choice4 == 1:
        leatherJournal()
    else:
        theKey()
        

def scratchingDoor():
    print('''You grip the handle of the door where the scratching sounds echo. 
As you open it, the noise stops abruptly. Inside is a small, 
decrepit room illuminated by a single, swinging light bulb. 
At the center of the room is a locked chest with strange runes carved into its surface.
          ''')
    
    time.sleep(3)

    print('''Suddenly, the chest begins to shake violently, 
and a raspy, guttural voice whispers, 
“Open me…” 
''')
    
    time.sleep(2)

    print('''The room grows colder, frost forming on the walls as the voice grows louder.''')

    time.sleep(1)

    print("Do you:")

    time.sleep(1)


def openChest():
    print('''Ignoring the warning signs, you unlock the chest. 
''')

    time.sleep(1)

    print('''As the lid creaks open, darkness pours out, consuming the room. 
You hear a deafening roar as shadowy tendrils latch onto you, pulling you into an endless abyss. 
The whispers turn into mocking laughter as your vision fades to black.'''
)

    time.sleep(2)

    print('''Ending: The Manor Claims Another Soul.''')

    time.sleep(1)

    playAgain()


def flee():
    print('''You slam the door shut and run back down the hallway, your breath coming in ragged gasps.
''')

    time.sleep(6)

    print('''The whispers fade, but the oppressive feeling of the manor remains. 
You reach the entrance hall and find the gates inexplicably open again.
''')

    time.sleep(8)

    print('''Without hesitation, you flee into the night, vowing never to return.'''
)

    time.sleep(6)

    print('''Ending: You Escape Ravenwood Manor... For now.''')

    time.sleep(2)

    playAgain()


def scratchingDoorChoice():
    userInput5 = ''

    while userInput5 != '1' and userInput5 != '2':
        print('''1. Open the Chest
2. Flee the Room
''')
        
        userInput5 = input()

    return int(userInput5)


def checkChoice5(choice5):
    if choice5 == 1:
        openChest()
    else:
        flee()


def playAgain():
    print('''
Do you want to play again?''')

    time.sleep(1)

    print('''
1. Yes
2. No
''')

    playAgain = input()

    while playAgain not in ['1', '2']:
        print('''Invalid choice. Please enter 1 or 2.
''')
        playAgain = input()
        
    if playAgain == '1':
        playGame()
    else:
        quit()


# Game Execution Starts
def playGame():
    intro()
    userInput1 = ironGate()
    checkChoice1(userInput1)

    userInput2 = entranceChoice()
    checkChoice2(userInput2)

    if userInput2 == 1:  # Grand Staircase
        userInput2a = staircaseChoice()
        checkChoice2a(userInput2a)  # Resume flow after staircase

    elif userInput2 == 2:  # Hallway
        hallway()

    userInput3 = hallwayChoice()
    checkChoice3(userInput3)

    userInput4 = studyChoice()
    checkChoice4(userInput4)

    userInput5 = scratchingDoorChoice()
    checkChoice5(userInput5)

playGame()
