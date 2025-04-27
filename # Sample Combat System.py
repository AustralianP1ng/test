# Sample Combat System Text Vers

import random
import time
from tkinter import *


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
        target.take_damage(normal_damage)


    def defend(self):
        self.defending = True


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
         
        target.take_damage(heavy_damage)

        return damage_multiplier, heavy_damage


player = Character("HERO", 100, 10, False)

enemy_types = [Character('DUMMY', 100, 5, False), Character("SKELETON", 25, 15, False),Character('GOBLIN', 50, 12, False), Character("GOLEM", 100, 10, True)]
enemy = enemy_types[0]

game_window = Tk()
game_window.geometry("1280x720")
game_window.title("Sample Combat System")
game_window.config(background= "#faf4eb")

def enemy_turn():
    enemy_choice = random.randint(1,2)
    
    if enemy_choice == 1:
        enemy.normal_attack(player)
        game_log.config(text= f"{enemy.name} ATTACK you for {enemy.attack_power} DMG!")
    else:
        enemy.defend()
        game_log.config(text= f"{enemy.name} DEFENDS!")


def attack_pressed():
    player.normal_attack(enemy)
    game_log.config(text= f"You ATTACK {enemy.name} for {player.attack_power} DMG!")
    game_window.after(3000, enemy_turn)


def defend_pressed():
    player.defend()
    game_log.config(text= f"You DEFEND! Incoming DMG is halved!")
    game_window.after(3000, enemy_turn)


def heavy_pressed():
    damage_multiplier, heavy_damage = player.heavy_attack(enemy)
    game_log.config(text= f'You HEAVY ATTACK {enemy.name} for {heavy_damage} points of DAMAGE! ({damage_multiplier}x dmg mult)')
    game_window.after(4000, enemy_turn)


def flee_pressed():
    player.heavy_attack(enemy)
    game_log.config(text= "You FLEE")
    game_window.after(2000)
    quit()


game_log = Label(game_window,
                 text= "Time to BATTLE",
                 font= ('Arial', 24),
                 bg= '#faf4eb')

button_frame = Frame(game_window,
                     bg= '#faf4eb')

attack_button = Button(button_frame,
                       font= ("Arial", 30), 
                       padx= 20,
                       relief= RAISED,
                       bd= 10,
                       text= 'ATTACK',
                       command= attack_pressed)

defend_button = Button(button_frame,
                       font= ("Arial", 30), 
                       padx= 20,
                       relief= RAISED,
                       bd= 10,
                       text= 'DEFEND',
                       command= defend_pressed)

heavy_attack_button = Button(button_frame,
                             font= ("Arial", 30), 
                             padx= 20,
                             relief= RAISED,
                             bd= 10,
                             text= 'HEAVY',
                             command= heavy_pressed)

flee_button = Button(button_frame,
                     font= ("Arial", 30), 
                     padx= 20,
                     relief= RAISED,
                     bd= 10,
                     text= 'FLEE', 
                     command= flee_pressed)


game_log.pack()

button_frame.pack(side= 'bottom',
                  pady= 50)

attack_button.grid(row= 0,
                   column= 0,
                   padx= 20)

defend_button.grid(row= 0,
                   column= 1,
                   padx= 20)

heavy_attack_button.grid(row= 0,
                         column= 2,
                         padx= 20)

flee_button.grid(row= 0,
                 column= 3,
                 padx= 20)


# Game launches
game_window.mainloop()
