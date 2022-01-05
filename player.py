import os
import sys
import json
import time

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.stamina = 100
        self.max_stamina = 100
        self.attack = 10
        self.speed = 10
        self.crit = 2
        self.pot = 5
        self.coins = 50
        self.inventory = {
            "pot": 5,
            "big_pot": 2,
            "stamina_pot": 5,
        }
        self.exp = 0
        self.level = 1
        self.zone = 1
        self.current_zone = 1

        self.stone = 0
        self.iron = 0
        self.gems = 0

        self.sword = None
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.boots = None
        self.ring = None
        self.collar = None
    
        self.load_player()

    def load_player(self):
        items_reader = open(os.path.join(sys.path[0], "items_id.txt"), "r")
        items_id = items_reader.read()
        items_id = json.loads(items_id)
        print("Loading player data ...")
        time.sleep(1)

        if self.sword in items_id['swords']:
            self.attack += items_id['swords'][self.sword]
            self.sword = self.sword + " " + "(+" + str(items_id['swords'][self.sword]) + " Attack Damage)"

        if self.helmet in items_id['helmets']:
            self.max_health += items_id['helmets'][self.helmet]
            self.health = self.max_health
            self.helmet = self.helmet + " " + "(+" + str(items_id['helmets'][self.helmet]) + " Hp)"
        
        if self.chestplate in items_id['chestplates']:
            self.max_health += items_id['chestplates'][self.chestplate]
            self.health = self.max_health
            self.chestplate = self.chestplate + " " + "(+" + str(items_id['chestplates'][self.chestplate]) + " Hp)"  

        if self.leggings in items_id['leggings']:
            self.max_health += items_id['leggings'][self.leggings]
            self.health = self.max_health
            self.leggings = self.leggings + " " + "(+" + str(items_id['leggings'][self.leggings]) + " Hp)"

        if self.boots in items_id['boots']:
            self.max_health += items_id['boots'][self.boots]
            self.health = self.max_health
            self.boots = self.boots + " " + "(+" + str(items_id['boots'][self.boots]) + " Hp)"

        if self.ring in items_id['rings']:
            self.speed += items_id['rings'][self.ring]
            self.ring = self.ring + " " + "(+" + str(items_id['rings'][self.ring]) + " Speed)"

        if self.collar in items_id['collars']:
            self.crit += items_id['collars'][self.collar]
            self.collar = self.collar + " " + "(+" + str(items_id['collars'][self.collar]) + " Crit Chance)"

        if self.zone == 0:
            raise ValueError

    def Shop(self):
        global player
        items_reader = open(os.path.join(sys.path[0], "items_id.txt"), "r")
        items_id = items_reader.read()
        items_id = json.loads(items_id)

        print("Welcome to the shop !")

        print(" ")

        print("Wooden_sword: " + str(items_id["swords"]['wooden_sword']) + " Attack Damage, Price = " + str(items_id["swords"]['wooden_sword'] * 50))
        print("Stone_sword: " + str(items_id["swords"]['stone_sword']) + " Attack Damage, Price = " + str(items_id["swords"]['stone_sword'] * 50))
        print("Long_sword: " + str(items_id["swords"]['long_sword']) + " Attack Damage, Price = " + str(items_id["swords"]['long_sword'] * 50))

        print(" ")

        print("Wooden_helmet: " + str(items_id["helmets"]['wooden_helmet']) + " Hp, Price = " + str(items_id["helmets"]['wooden_helmet'] * 50))
        print("Steel_helmet: " + str(items_id["helmets"]['steel_helmet']) + " Hp, Price = " + str(items_id["helmets"]['steel_helmet'] * 50))

        print(" ")

        print("Wooden_chestplate: " + str(items_id["chestplates"]['wooden_chestplate']) + " Hp, Price = " + str(items_id["chestplates"]['wooden_chestplate'] * 50))
        print("Steel_chestplate: " + str(items_id["chestplates"]['steel_chestplate']) + " Hp, Price = " + str(items_id["chestplates"]['steel_chestplate'] * 50))

        print(" ")

        print("Wooden_leggings: " + str(items_id["leggings"]['wooden_leggings']) + " Hp, Price = " + str(items_id["leggings"]['wooden_leggings'] * 50))
        print("Steel_leggings: " + str(items_id["leggings"]['steel_leggings']) + " Hp, Price = " + str(items_id["leggings"]['steel_leggings'] * 50))

        print(" ")

        print("Wooden_boots: " + str(items_id["boots"]['wooden_boots']) + " Hp, Price = " + str(items_id["boots"]['wooden_boots'] * 50))
        print("Steel_boots: " + str(items_id["boots"]['steel_boots']) + " Hp, Price = " + str(items_id["boots"]['steel_boots'] * 50))

        print(" ")

        print("Steel_ring: " + str(items_id["rings"]['steel_ring']) + " Speed, Price = " + str(items_id["rings"]['steel_ring'] * 50))
        print("Jeweled_ring: " + str(items_id["rings"]['jeweled_ring']) + " Speed, Price = " + str(items_id["rings"]['jeweled_ring'] * 50))

        print(" ")

        print("Steel_collar: " + str(items_id["collars"]['steel_collar']) + " Crit Chance, Price = " + str(items_id["collars"]['steel_collar'] * 50))
        print("Jeweled_collars: " + str(items_id["collars"]['jeweled_collar']) + " Crit Chance, Price = " + str(items_id["collars"]['jeweled_collar'] * 50))

        print(" ")

        print("Potion: Price = 50")

        print(" ")

        print(f"You have {self.coins} Coins")
        shop_active = True
        while shop_active == True:
            item = input("What do you want to buy ? (Quit for return to main menu) ")

            if item.lower() == "wooden_sword":
                if self.coins >= items_id["swords"]['wooden_sword'] * 50:
                    self.coins -= items_id["swords"]['wooden_sword'] * 50
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "wooden_sword"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "stone_sword":
                if self.coins >= items_id["swords"]['stone_sword'] * 50:
                    self.coins -= items_id["swords"]['stone_sword'] * 50
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "stone_sword"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "long_sword":
                if self.coins >= items_id["swords"]['long_sword'] * 50:
                    self.coins -= items_id["swords"]['long_sword'] * 50
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "long_sword"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass

            elif item.lower() == "wooden_helmet":
                if self.coins >= items_id["helmets"]['wooden_helmet'] * 50:
                    self.coins -= items_id["helmets"]['wooden_helmet'] * 50
                    if self.helmet != None:
                        updated = {self.helmet: 1}
                        self.inventory.update(updated)
                    self.helmet = "wooden_helmet"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "steel_helmet":
                if self.coins >= items_id["helmets"]['steel_helmet'] * 50:
                    self.coins -= items_id["helmets"]['steel_helmet'] * 50
                    if self.helmet != None:
                        updated = {self.helmet: 1}
                        self.inventory.update(updated)
                    self.helmet = "steel_helmet"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass

            elif item.lower() == "wooden_chestplate":
                if self.coins >= items_id["chestplates"]['wooden_chestplate'] * 50:
                    self.coins -= items_id["chestplates"]['wooden_chestplate'] * 50
                    if self.chestplate != None:
                        updated = {self.chestplate: 1}
                        self.inventory.update(updated)
                    self.chestplate = "wooden_chestplate"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "steel_chestplate":
                if self.coins >= items_id["chestplates"]['steel_chestplate'] * 50:
                    self.coins -= items_id["chetsplates"]['steel_chestplate'] * 50
                    if self.chestplate != None:
                        updated = {self.chestplate: 1}
                        self.inventory.update(updated)
                    self.chestplate = "steel_chestplate"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass

            elif item.lower() == "wooden_leggings":
                if self.coins >= items_id["leggings"]['wooden_leggings'] * 50:
                    self.coins -= items_id["leggings"]['wooden_leggings'] * 50
                    if self.leggings != None:
                        updated = {self.leggings: 1}
                        self.inventory.update(updated)
                    self.leggings = "wooden_leggings"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "steel_leggings":
                if self.coins >= items_id["leggings"]['steel_leggings'] * 50:
                    self.coins -= items_id["leggings"]['steel_leggings'] * 50
                    if self.leggings != None:
                        updated = {self.leggings: 1}
                        self.inventory.update(updated)
                    self.leggings = "steel_leggings"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
                
            elif item.lower() == "wooden_boots":
                if self.coins >= items_id["boots"]['wooden_boots'] * 50:
                    self.coins -= items_id["boots"]['wooden_boots'] * 50
                    if self.boots != None:
                        updated = {self.boots: 1}
                        self.inventory.update(updated)
                    self.boots = "wooden_boots"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "steel_boots":
                if self.coins >= items_id["boots"]['steel_boots'] * 50:
                    self.coins -= items_id["boots"]['steel_boots'] * 50
                    if self.boots != None:
                        updated = {self.boots: 1}
                        self.inventory.update(updated)
                    self.boots = "steel_boots"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass

            elif item.lower() == "steel_ring":
                if self.coins >= items_id["rings"]['steel_ring'] * 50:
                    self.coins -= items_id["rings"]['steel_ring'] * 50
                    if self.ring != None:
                        updated = {self.ring: 1}
                        self.inventory.update(updated)
                    self.ring = "steel_ring"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "jeweled_ring":
                if self.coins >= items_id["rings"]['jeweled_ring'] * 50:
                    self.coins -= items_id["rings"]['jeweled_ring'] * 50
                    if self.ring != None:
                        updated = {self.ring: 1}
                        self.inventory.update(updated)
                    self.ring = "jeweled_ring"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            
            elif item.lower() == "steel_collar":
                if self.coins >= items_id["collars"]['steel_collar'] * 50:
                    self.coins -= items_id["collars"]['steel_collar'] * 50
                    if self.collar != None:
                        updated = {self.collar: 1}
                        self.inventory.update(updated)
                    self.collar = "steel_collar"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "jeweled_collar":
                if self.coins >= items_id["collars"]['jeweled_collar'] * 50:
                    self.coins -= items_id["collars"]['jeweled_collar'] * 50
                    if self.collar != None:
                        updated = {self.collar: 1}
                        self.inventory.update(updated)
                    self.collar = "jeweled_collar"
                    self.load_player()
                else:
                    print("You don't have anough coins !")
                    pass
                
            elif item.lower() == "potion":
                if self.coins >= 50:
                    self.inventory['pot'] += 1
                    self.coins -= 50
                else:
                    print("You don't have anough coins !")
                    pass
            elif item.lower() == "quit":
                shop_active = False
            else: print("There is a problem on your command. Please check your command to see if there is an error")

    def Forge(self):
        print(" ")
        print("Wooden_sword: 5 Stone")
        print("Stone_sword: 5 Iron")
        print("Long_sword: 10 Iron")

        print(" ")

        print("Wooden_helmet: 5 Stone")
        print("Steel_helmet: 5 Iron")

        print(" ")

        print("Wooden_chestplate: 5 Stone")
        print("Steel_chestplate: 5 Iron")

        print(" ")

        print("Wooden_leggings: 5 Stone")
        print("Steel_leggings: 5 Iron")

        print(" ")

        print("Wooden_boots: 5 Stone")
        print("Steel_boots: 5 Iron")

        print(" ")

        print("Steel_ring: 5 Iron")
        print("Jeweled_ring: 5 Gems")

        print(" ")

        print("Steel_collar: 5 Iron")
        print("Jeweled_collar: 5 Gems")

        print(" ")

        print(f"You have {self.stone} Stone/{self.iron} Iron/{self.gems} Gems")

        forge_active = True
        while forge_active == True:
            forged = input("What do you want to forge ? (Quit to return to the main menu) ")

            if forged.lower() == "wooden_sword":
                if self.stone >= 5:
                    self.stone -= 5
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "wooden_sword"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "stone_sword":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "stone_sword"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "long_sword":
                if self.iron >= 10:
                    self.iron -= 10
                    if self.sword != None:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                    self.sword = "long_sword"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass

            elif forged.lower() == "wooden_helmet":
                if self.stone >= 5:
                    self.stone -= 5
                    if self.helmet != None:
                        updated = {self.helmet: 1}
                        self.inventory.update(updated)
                    self.helmet = "wooden_helmet"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "steel_helmet":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.helmet != None:
                        updated = {self.helmet: 1}
                        self.inventory.update(updated)
                    self.sword = "steel_helmet"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
                
            elif forged.lower() == "wooden_chestplate":
                if self.stone >= 5:
                    self.stone -= 5
                    if self.chestplate != None:
                        updated = {self.chestplate: 1}
                        self.inventory.update(updated)
                    self.chestplate = "wooden_chetsplate"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "steel_chestplate":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.chestplate != None:
                        updated = {self.chestplate: 1}
                        self.inventory.update(updated)
                    self.chestplate = "steel_chestplate"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
                
            elif forged.lower() == "wooden_leggings":
                if self.stone >= 5:
                    self.stone -= 5
                    if self.leggings != None:
                        updated = {self.leggings: 1}
                        self.inventory.update(updated)
                    self.leggings = "wooden_leggings"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "steel_leggings":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.leggings != None:
                        updated = {self.leggings: 1}
                        self.inventory.update(updated)
                    self.leggings = "steel_leggings"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
                
            elif forged.lower() == "wooden_boots":
                if self.stone >= 5:
                    self.stone -= 5
                    if self.boots != None:
                        updated = {self.boots: 1}
                        self.inventory.update(updated)
                    self.boots = "wooden_boots"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "steel_boots":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.boots != None:
                        updated = {self.boots: 1}
                        self.inventory.update(updated)
                    self.boots = "steel_boots"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "steel_ring":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.ring != None:
                        updated = {self.ring: 1}
                        self.inventory.update(updated)
                    self.ring = "steel_ring"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "jeweled_ring":
                if self.gems >= 5:
                    self.gems -= 5
                    if self.ring != None:
                        updated = {self.ring: 1}
                        self.inventory.update(updated)
                    self.ring = "jeweled_ring"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            
            elif forged.lower() == "steel_collar":
                if self.iron >= 5:
                    self.iron -= 5
                    if self.collar != None:
                        updated = {self.collar: 1}
                        self.inventory.update(updated)
                    self.collar = "steel_collar"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass
            elif forged.lower() == "jeweled_collar":
                if self.gems >= 5:
                    self.gems -= 5
                    if self.collar != None:
                        updated = {self.collar: 1}
                        self.inventory.update(updated)
                    self.collar = "jeweled_collar"
                    self.load_player()
                else:
                    print("You don't have enough materials !")
                    pass

            elif forged.lower() == "quit":
                forge_active = False
            else: print("There is a problem on your command. Please check your command to see if there is an error")

    def Zones(self):
        for i in range(self.zone):
            print(f"Zone {i + 1}: V")

        print(" ")
        print(f"You are in zone {self.current_zone}")
        print(" ")

        change = input("What area do you want to go to ?(Quit for return to main menu) ")
        if change.lower() != "quit":
            if change.isdigit():  
                change = int(change)          
                if change <= self.zone:
                    self.current_zone = change
                    print(f"Your are in zone {self.current_zone}")
                else:
                    print("You don't have unlocked this zone !")
            else:
                print("You need to type a number !!")

    def Inventory(self):
        items_reader = open(os.path.join(sys.path[0], "items_id.txt"), "r")
        items_id = items_reader.read()
        items_id = json.loads(items_id)


        print()
        for item in self.inventory:
            print(f"{item}: {self.inventory[item]}")
        print()

        while True:
            choice = input('What do you want to do? (Use/Equip/Quit) ')
            if choice.lower() not in ['use', 'equip', 'quit']:
                print("You can only type Use/Equip/Quit !!")

            if choice.lower() == "quit":
                break
            
            elif choice.lower() == "use":
                print()
                used = input("What object do you want to use? ")
                self.Heal(used)
                break
            
            elif choice.lower() == "equip":
                print()
                equiped = input("What item do you want to equip? ")
                print()
                if equiped in self.inventory:
                    InvChange = equiped
                    self.inventory.pop(equiped)
                    if equiped in items_id["swords"]:
                        updated = {self.sword: 1}
                        self.inventory.update(updated)
                        self.sword = InvChange
                        self.load_player()

                    elif equiped in items_id["helmets"]:
                        updated = {self.helmet: 1}
                        self.inventory.update(updated)
                        self.helmet = InvChange
                        self.load_player()

                    elif equiped in items_id["chestplates"]:
                        updated = {self.chestplate: 1}
                        self.inventory.update(updated)
                        self.chestplate = InvChange
                        self.load_player()
                    
                    elif equiped in items_id["leggings"]:
                        updated = {self.leggings: 1}
                        self.inventory.update(updated)
                        self.leggings = InvChange
                        self.load_player()

                    elif equiped in items_id["boots"]:
                        updated = {self.boots: 1}
                        self.inventory.update(updated)
                        self.boots = InvChange
                        self.load_player()
                    
                    elif equiped in items_id["rings"]:
                        updated = {self.ring: 1}
                        self.inventory.update(updated)
                        self.ring = InvChange
                        self.load_player()

                    elif equiped in items_id["collars"]:
                        updated = {self.collar: 1}
                        self.inventory.update(updated)
                        self.collar = InvChange
                        self.load_player()


    def Heal(self, obj):
        if obj in self.inventory:
            if obj.lower() not in ['pot', 'big_pot', 'stamina_pot']:
                print("You can only use potions")
            
            if obj.lower() == "pot":
                if self.inventory['pot'] != 0:
                    self.health += 50
                    updated = {"pot": self.inventory['pot'] - 1}
                    self.inventory.update(updated)
                else:
                    print("You don't have any pots")

            elif obj.lower() == "big_pot":
                if self.inventory['big_pot'] != 0:
                    self.health += 100
                    updated = {"big_pot": self.inventory['big_pot'] - 1}
                    self.inventory.update(updated)
                else:
                    print("You don't have any pots")

            elif obj.lower() == "stamina_pot":
                if self.inventory['stamina_pot'] != 0:
                    self.stamina += 50
                    updated = {"stamina_pot": self.inventory['stamina_pot'] - 1}
                    self.inventory.update(updated)
                else:
                    print("You don't have any pots")
        else:
            print("You don't have this object")