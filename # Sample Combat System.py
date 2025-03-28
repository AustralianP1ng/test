# Sample Combat System Text Vers

import random
import time



class Character():

    def __init__(self, 
                 name: str, 
                 hp: int, 
                 attack_power: int,
                 defending: bool):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defending = False

    def normal_attack(self,
                      target: str):        
        normal_damage = self.attack_power
        target.take_damage(normal_damage)

        print(f'{self.name} attacks {target.name} for {self.attack_power} points of DAMAGE!')
        print()
        time.sleep(1)


    def defend(self):
        self.defending = True

        print(f"{self.name} DEFENDS.")
        print()
        time.sleep(1)


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


    def heavy_attack(self,
                     target: str):
        pass
         



def gameStart():

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

    # Initialise player and enemy objects
    player = Character(player_name, 100, 10, False)

    enemy_types = [Character('DUMMY', 100, 0, False), Character("SKELETON", 25, 5, False),Character('GOBLIN', 50, 7, False), Character("GOLEM", 100, 4, True)]
    enemy = random.choice(enemy_types)


    # Actual start of the game
    while player.is_alive() and enemy.is_alive():

        print("""[1| ATTACK]  [2| DEFEND]  [3| FLEE]""")
        playerChoice = input("> ")

        while playerChoice != '1' and playerChoice != '2' and playerChoice != '3':
            print()
            playerChoice = input('''Invalid choice. Please enter "1", "2" or "3"
> ''')

        else:
            player.reset_defense()
            enemy.reset_defense()
            
            if playerChoice == '1':
                player.normal_attack(enemy)
            
            elif playerChoice == '2':
                player.defend()
            
            else:
                player.flee()
        
        if enemy.is_alive():
            enemy_turn = random.randint(1, 2)

            if enemy_turn == 1:
                enemy.normal_attack(player)
            else:
                enemy.defend()
    
    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
        print("You WIN.")
    else:
        print(f"{enemy.name} defeated {player.name}!")
        print("You LOSE.")

gameStart()
