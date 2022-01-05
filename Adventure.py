from player import Player
from monster import Monster
import time

#########################################################
###     Functions
#########################################################
def PrintStats():
    print(f"Health: {player.health}")
    print(f"Stamina: {player.stamina}")
    print(f"Attack Damage: {player.attack}")
    print(f"Experience: {player.exp}")
    print(f"Level: {player.level}")

def Die(obj):
    global player
    global monster

    if obj == player:
        print("You died!")
        print("Data saving is not implemented yet. Please restart the game.")
        del player
        quit()
    elif obj == monster:
        player.exp += monster.exp_value
        print(f"You killed the monster and gain {monster.exp_value} Exp")
        del monster
    else:
        print("Error in game, please check the Die function \nAnd the call of the Die function")
        quit()

def Check_Level():
    global player
    if player.exp >= player.level * 50:
        player.exp -= player.level * 50
        Level()
        

def Level():
    global player

    player.max_health += 25
    player.health = player.max_health
    player.max_stamina += 10
    player.stamina = player.max_stamina
    player.attack += 2
    player.speed += 5
    player.level += 1
    print("You leveled up ! Heres your stats")
    PrintStats()

def Battle():
    global monster
    global player

    attacker = player
    player_died = False
    monster_died = False

    if player.speed >= monster.speed:
        attacker = player
    else:
        attacker = monster

    while player_died == False and monster_died == False:
        if attacker == player:
            print("Player attack")
            monster.health -= player.attack
            if monster.health <= 0:
                monster_died = True
            attacker = monster
            time.sleep(0.5)
        else:
            print("Monster attack")
            player.health -= monster.attack
            if player.health <= 0:
                player_died = True
            attacker = player
            time.sleep(0.5)
    
    if player_died == True:
        Die(player)
    else:
        Die(monster)

def MainGame():
    global monster
    print("Welcome to my Adventure Game")
    choice = input("There is a slime on your road. Are you gonna attack him ? ")
    no_times = 0

    if choice.lower() == "no":
        no_times +=1
        choice = input("You are in front of a river. Do you gonna swim or walk cross the river? (walk/swim) ")
        if choice.lower() == "walk":
            no_times +=1
            choice = input("You walked and find a wolf. Do you want to fight him ? ")
            if choice.lower() == "no":
                no_times +=1
            elif choice.lower() == "yes":
                monster = Monster(200, 10, 20, 500)
                Battle()
                Check_Level()
            else:
                print("You can only say Yes or No !")
                quit()
        elif choice.lower() == "swim":
            choice = input("You swim across the river and find a gobelin. Are you gonna attack him ? ")
            if choice.lower() == "no":
                no_times +=1
                choice = input("A group of mysticals creatures is on you way. You fight ? ")
                if choice.lower() == "no":
                    no_times +=1
                elif choice.lower() == "yes":
                    monster = Monster(200, 10, 15, 200)
                    Battle()
                    Check_Level()
                else:
                    print("You can only say Yes or No !")
                    quit()
            elif choice.lower() == "yes":
                monster = Monster(100, 5, 9, 50)
                Battle()
                Check_Level()   
            else:
                print("You can only say Yes or No !")
                quit()
        else:
            print("You can only say walk or swim !")
            quit()
    elif choice.lower() == "yes":
        monster = Monster(25, 5, 10, 50)
        Battle()
        Check_Level()
        choice = input("You killed the slime and return on your road. There is a stranger, do you gonna talk to him? ")
        if choice.lower() == "no":
            no_times +=1
        elif choice.lower() == "yes":
            print("The stranger gave you 100 Exp !")
            player.exp += 100
            Check_Level()
            choice = input("You see a rock golem. Are you gonna fight him ? ")
            if choice.lower() == "no":
                no_times +=1
            elif choice.lower() == "yes":
                monster = Monster(200, 20, 5, 500)
                Battle()
                Check_Level()
            else:
                print("You can only say Yes or No !")
                quit()
        else:
            print("You can only say Yes or No !")
            quit()
    else:
        print("You can only say Yes or No !")
        quit()
    
    if no_times == 3:
        print("An legendary elemental attack you !")
        Die(player)

if __name__ == '__main__':
    player = Player()
    MainGame()