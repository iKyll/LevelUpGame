from player import Player
from monster import Monster
from random import *
import threading
import time
import os
import sys
import json

class EnergyGiver():
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    
    def run(self):
        while True:
            while player.stamina < player.max_stamina:
                player.stamina += 2
                time.sleep(5)

def PrintStats():
    print(" ")

    print(f"Health: {player.health}")
    print(f"Stamina: {player.stamina}")
    print(f"Attack Damage: {player.attack}")
    print(f"Speed: {player.speed}")
    print(f"Crit Chance: {player.crit}%")
    print(f"Potions: {player.pot}")
    print(f"Coins: {player.coins}")
    print(f"Experience: {player.exp}")
    print(f"Level: {player.level}")
    print(f"Zone: {player.zone}")

    print(" ")

    print(f"Stone: {player.stone}")
    print(f"Iron: {player.iron}")
    print(f"Gems: {player.gems}")

    print(" ")

    print(f"Inventory:")
    print(f"Sword: {player.sword}")
    print(f"Helmet: {player.helmet}")
    print(f"Chestplate: {player.chestplate}")
    print(f"Leggings: {player.leggings}")
    print(f"Boots: {player.boots}")
    print(f"Ring: {player.ring}")
    print(f"Collar: {player.collar}")

def Die(obj):
    global player
    global monster

    if obj == player:
        print("You died!")
        print("Data is saving...")
        player.health = 1
        DataSaver()
        print("You have one hp if you can't heal yourself it's game over")
        del player
        quit()
    elif obj == monster:
        player.exp += monster.exp_value
        player.coins += monster.coin_value
        print(f"You killed the monster and gain {monster.exp_value} Exp/{monster.coin_value} Coins")
        Check_Level()
        del monster
    else:
        print("Error in game, please check the Die function \nAnd the call of the Die function")
        quit()

def Check_Level():
    global player
    
    while player.exp >= player.level * 50:
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
    player.crit += 1
    player.level += 1
    print("You leveled up ! Heres your stats")
    PrintStats()

def BattleSystem():
    global monster
    global player
    global isBoss

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
            if randint(0, 100) <= player.crit:
                print("CRIT")
                monster.health -= player.attack * 2
            else:
                monster.health -= player.attack
            if monster.health <= 0:
                monster_died = True
            attacker = monster
            time.sleep(0.5)
        else:
            print("Monster attack")
            if randint(0, 100) <= monster.crit:
                player.health -= monster.attack * 2
            else:
                player.health -= monster.attack
            if player.health <= 0:
                player_died = True
            attacker = player
            time.sleep(0.5)
    
    if player_died == True:
        Die(player)
    else:
        Die(monster)
        if isBoss == True:
            isBoss = False
            if player.zone == player.current_zone:
                if player.zone < 11:
                    player.zone += 1
                    change = input("Do you want to move on to the next area: ")
                    if change.lower() == "yes":
                        player.current_zone += 1

def Boss():
    global player
    global monster
    global isBoss

    if player.level < 10:
        print("You don't have the requirements")
    else:
        if player.stamina >= 20:
            sure = input("Are you sure you want to fight this monster ? ")
            if sure.lower() == "yes":
                monster = Monster(randint(player.current_zone * 250, player.current_zone * 2 * 250), randint(player.current_zone * 10, player.current_zone * 2 * 10), randint(player.current_zone * 10, player.current_zone * 2 * 50), player.current_zone * 500, randint(player.current_zone * 50, player.current_zone * 2 * 50), randint(player.current_zone * 2, player.current_zone* 2 * 50))
                isBoss = True
                BattleSystem()
                player.stamina -= 20
        else:
            print("You don't have enough stamina to do this !")

def Battle():
    global player
    global monster

    while player.stamina >= 5:
        monster = Monster(randint(player.current_zone * 50, player.current_zone * 2 * 50), randint(player.current_zone * 2, player.current_zone * 2 * 2), randint(player.current_zone * 2, player.current_zone * 2 * 2), randint(player.current_zone * 50, player.current_zone * 2 * 50), randint(player.current_zone * 5, player.current_zone * 2 * 5), randint(player.current_zone * 2, player.current_zone * 2 * 2))
        BattleSystem()
        player.stamina -= 5
        ask_stop = input("Do you want to stop the Battle (Yes/Press Enter for continue) ")
        if ask_stop.lower() == "yes":
            break
    
    if player.stamina < 5:
        print("You don't have enough stamina to do this !")
        pass

def DataSaver():
    writer_data = open(os.path.join(sys.path[0], "player_data.txt"), "w")
    data = {
        "health": player.health,
        "max_health": player.max_health,
        "stamina": player.stamina,
        "max_stamina": player.max_stamina,
        "attack": player.attack,
        "speed": player.speed,
        "crit": player.crit,
        "pot": player.pot,
        "coins": player.coins,
        "exp": player.exp,
        "level": player.level,
        "zone": player.zone,
        "current_zone": player.current_zone,

        "iron": player.iron,
        "stone": player.stone,
        "gems": player.gems,

        "sword": player.sword,
        "helmet": player.helmet,
        "chestplate": player.chestplate,
        "leggings": player.leggings,
        "boots": player.boots,
        "ring": player.ring,
        "collar": player.collar
        
    }
    writer_data.write(json.dumps(data))

def DataLoader():
    reader_data = open(os.path.join(sys.path[0], "player_data.txt"), "r")
    data = reader_data.read()
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        print("There isn't any data or the data is corrupted")
        return -1

    player.max_health = data['max_health']
    player.health = data['health']
    player.max_stamina = data['max_stamina']
    player.stamina = data['stamina']
    player.attack = data['attack']
    player.speed = data['speed']
    player.crit = data['crit']
    player.pot = data['pot']
    player.coins = data['coins']
    player.exp = data['exp']
    player.level = data['level']
    player.zone = data['zone']
    player.current_zone = data['current_zone']

    player.stone = data['stone']
    player.iron = data['iron']
    player.gems = data['gems']

    player.sword = data['sword']
    player.helmet = data['helmet']
    player.chestplate = data['chestplate']
    player.leggings = data['leggings']
    player.boots = data['boots']
    player.ring = data['ring']
    player.collar = data['collar']

    PrintStats()

def Load_data():
    global items_id

    items_reader = open(os.path.join(sys.path[0], "items_id.txt"), "r")
    items_id = items_reader.read()
    items_id = json.loads(items_id)
    
def Mine():
    global player
    random_mine = randint(0, 10)
    random_time = randint(3, 10)
    random_exp = randint(5, 20)
    random_coin = randint(0,5)
    if player.stamina >= 5:
        print("Mining ...")
        time.sleep(random_time)
        player.stamina -= 5

        if random_mine < 7:
            player.stone += 1
            player.exp += random_exp
            player.coins += random_coin
            print("You find a stone")
        elif random_mine >= 7 and random_mine <= 9:
            player.iron += 1
            player.exp += random_exp
            player.coins += random_coin
            print("You find an iron !")
        else:
            player.gems += 1
            player.exp += random_exp
            player.coins += random_coin
            print("You find a gem !!!")
    else:
        print("You don't have enough stamina to do this !")

if __name__ == '__main__':
    Load_data()
    player = Player()
    energy = EnergyGiver()
    while True:
        print(" ")
        action = input("What do you want to do ? (Battle/PrintStats/Boss/Zone/Shop/Mine/Forge/Inventory/Quit/Save/Load) ")
        if action.lower() == "battle":
            isBoss = None
            Battle()
        elif action.lower() == "printstats":
            PrintStats()
        elif action.lower() == "boss":
            isBoss = None
            Boss()
        elif action.lower() == "zone":
            player.Zones()
        elif action.lower() == "shop":
            player.Shop()
        elif action.lower() == "mine":
            Mine()
        elif action.lower() == "forge":
            player.Forge()
        elif action.lower() == "inventory":
            player.Inventory()
        elif action.lower() == "save":
            DataSaver()
        elif action.lower() == "load":
            DataLoader()
        elif action.lower() == "quit":
            sure = input("Are you sure, if you don't have save you gonna lose all of your data! ")
            if sure.lower() == "yes":
                print("GoodBye !")
                quit()
        else:
            print("You type the command wrong")


