# Sample Combat System Text Vers

import random
import time


achievements = set()        # Achievement for each mob defeated


class Character():

    def __init__(self, 
                 name: str, 
                 hp: int, 
                 attack_power: int,
                 defending: bool):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defending = defending

        self.charging = False


    def normal_attack(self,
                      target: str):        
        normal_damage = self.attack_power
        print(f'{self.name} attacks {target.name} for {normal_damage} points of DAMAGE!')

        target.take_damage(normal_damage)

        print()
        time.sleep(2)


    def defend(self):
        self.defending = True

        print(f"{self.name} DEFENDS.")
        print()
        time.sleep(2)


    def reset_defense(self):        # resets 'DEFENDING' back to false after one turn
        self.defending = False


    def take_damage(self,
                    damage: int):
        if self.defending:
            damage = damage // 2
            print(f"{self.name} is DEFENDING and only takes {damage} DAMAGE!")
            
        else:
            print(f"{self.name} takes {damage} DAMAGE!")
        self.hp -= damage

    
    def is_alive(self):
        return self.hp > 0
    

    def flee(self):
        print(f'{self.name} FLED.')
        print()
        exit()


    def heavy_attack_charge(self):
        self.charging = True

        print(f"""{self.name} is CHARGING their HEAVY ATTACK
{self.name} will not be able to use HEAVY ATTACK on their next turn!
""")        
        time.sleep(2)


    def heavy_attack(self,
                     target: str):
        
        damage_multiplier_list = [1.50, 1.75, 2.0]
        damage_multiplier = random.choice(damage_multiplier_list)

        heavy_damage = int(self.attack_power * damage_multiplier)

        print(f'{self.name} HEAVY ATTACKS {target.name} for {heavy_damage} points of DAMAGE! ({damage_multiplier}x dmg mult)')
         
        target.take_damage(heavy_damage)
        print()

        time.sleep(2)


class weapons():
    def __init__(self, 
                 weapon_name: str,
                 weapon_attack: int,
                 ):
        pass
        

def showAchievements():

    total_achievements = 4

    print(f"""
You have defeated {len(achievements)} out of {total_achievements} enemies.
""")
    time.sleep(2)


def enemyAI():
    pass



def playAgain():

    play_again_choice = input("""Play again:
[1| View defeated enemies]
[2| Yes]
[3| No ]
> """)
    
    while play_again_choice not in ['1', '2', '3']:
        print("""Invalid choice. Please enter 1, 2 or 3.
""")
        play_again_choice = input("> ")
    
    if play_again_choice == '1':
        for enemies_defeated in achievements:
            print()
            print(enemies_defeated)
            print()
            time.sleep(2)
        
        playAgain()
        

    elif play_again_choice == '2':
        print()
        gameStart()
    
    else:
        quit()


def gameStart():

    heavy_attack_counter = 0

    # Initialise player and enemy objects
    player = Character(player_name, 100, 10, False)

    # Different enemies
    enemy_types = [Character('DUMMY', 100, 5, False), Character("SKELETON", 25, 15, False),Character('GOBLIN', 50, 12, False), Character("GOLEM", 100, 10, True)]

    enemy_choice = input("""Choose an opponent:
[1| DUMMY]  [2| SKELETON]  [3| GOBLIN]  [4| GOLEM]
> """)
    
    while enemy_choice not in ['1', '2', '3', '4']:
        print()
        enemy_choice = input('''Invalid choice. Please enter "1", "2", "3" or "4"
> ''')
    

    if enemy_choice == '1':
        enemy = enemy_types[0]

    elif enemy_choice == '2':
        enemy = enemy_types[1]

    elif enemy_choice == '3':
        enemy = enemy_types[2]
    
    elif enemy_choice == '4':
        enemy = enemy_types[3]


    # Actual start of the game
    while player.is_alive() and enemy.is_alive():

        print(f"""Player HP: {player.hp}
Enemy HP: {enemy.hp}
""")    
        
        if player.charging == True:
            player.heavy_attack(enemy)
            player.charging = False

        else:

            if heavy_attack_counter == 0:   # Allows heavy attack if heavy attack wasn't used last turn
                print("""[1| ATTACK]  [2| DEFEND]  [3| HEAVY]  [4| FLEE]""")
                playerChoice = input("> ")

                while playerChoice not in ['1', '2', '3', '4']:
                    print()
                    playerChoice = input('''Invalid choice. Please enter "1", "2", "3" or "4"
> ''')

                else:
            
                    if playerChoice == '1':
                        player.normal_attack(enemy)
            
                    elif playerChoice == '2':
                        player.defend()
            
                    elif playerChoice == '3':

                        heavy_attack_counter += 1
                        player.heavy_attack_charge()
            
                    else:
                        player.flee()

            else:
                heavy_attack_counter -= 1   # Doesn't give heavy attack option if used last turn (prevents spam)

                print("""[1| ATTACK]  [2| DEFEND]  [3| FLEE]""")
                playerChoice = input("> ")

                while playerChoice not in ['1', '2', '3']:
                    print()
                    playerChoice = input('''Invalid choice. Please enter "1", "2" or "3"
> ''')
                else:
            
                    if playerChoice == '1':
                        player.normal_attack(enemy)
            
                    elif playerChoice == '2':
                        player.defend()
            
                    else:
                        player.flee()
                            

            player.reset_defense()

            if enemy == enemy_types[0] or enemy == enemy_types[1] or enemy == enemy_types[2]:
                enemy.reset_defense()
        
            if enemy.is_alive():
                if enemy == enemy_types[3]:
                    enemy.normal_attack(player)
                else:
                    ai_choice = random.randint(1, 2)

                    if ai_choice == 1:
                        enemy.normal_attack(player)
                    else:
                        enemy.defend()
                
    
    if player.is_alive():
        print(f"""{player.name} defeated {enemy.name}!
""")
        print("You WIN.")
        achievements.add(f'{enemy.name} defeated')

        showAchievements()
        playAgain()

    else:
        print(f"""{enemy.name} defeated {player.name}!
""")
        print("You LOSE.")

        showAchievements()
        playAgain()


 # Getting player to input a desired name
player_name = input('''Choose your adventurer's name
> ''')
print()

# Prevents empty spaces or blank inputs as name
while ' ' in player_name or '' == player_name:
    print()
    print('Name should not include spaces or blanks')
    time.sleep(2)
    player_name = input('''Choose your adventurer's name
> ''')


gameStart()
