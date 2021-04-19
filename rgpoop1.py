
class characters:
    def __init__(self, health, power):
        self.power = power
        self.health = health


    def alive(self):
            if self.health > 0:
                return True
            else:
                return False



class Hero(characters):
    def __init__(self, health, power):
        super(Hero, self).__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if self.health <= 0:
            print("You are dead.")
        if enemy.health <= 0:
            print("You killed the goblin")
    
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))



class Goblin(characters):
    def __init__(self, health, power):
        super(Goblin, self).__init__(health, power)
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if self.health <= 0:
            print("The goblin is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))
        #print("The goblin is dead.")

class Zombie(characters):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("The Zombie does {} damage to you, and his health and power remains the same. Flee!".format(self.power))
        if self.health <= 0:
            print("The goblin is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The zombie has {} health and {} power.".format(self.health, self.power))
        #print("The goblin is dead.")


def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    zombie = Zombie(2, 2)

    while goblin.alive() and hero.alive():
        goblin.print_status()
        hero.print_status() 
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing (goblin fights you)")
        print("3. Zombie fights you")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            #Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            goblin.attack(hero)
        elif raw_input == "3":
            zombie.attack(hero)
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        #if goblin.health > 0:
            # Goblin attacks hero
            #hero.health -= goblin.power
           
            #print("The goblin does {} damage to you.".format(goblin.power))
            
            # if hero.health <= 0:
                #print("You are dead.")
             

main()







################################################################# Final Version Below:
import random

class characters:
    def __init__(self, health, power):
        self.power = power
        self.health = health
        

    def alive(self):
            if self.name == "Zombie":
                return True
            if self.health > 0:
                return True
            else:
                return False



class HeMan(characters):
    def __init__(self, health, power, armor, evade):
        super(HeMan, self).__init__(health, power)
        self.name = "HeMan"
        self.bounty = 5
        self.supertonic = "SuperTonic"
        self.armor = armor
        self.evade = evade

    def collectbounty(self, enemy):
        if enemy.name == "Goblin":
            self.bounty += 2
        elif enemy.name == "Wizard":
            self.bounty += 6
        elif enemy.name == "Dragon":
            self.bounty += 10
        print(f"You collected {enemy.bounty} coins")
        print(f"Your total bounty tally is {self.bounty} coins.")

    def buysupertonic(self):
        if self.bounty <= 0:
            self.health = 10
            self.bounty -= 5
            print(f"SuperTonic cost you 5 coins. Your bounty tally is now {self.bounty} coins.")
            print(f"Your health is now reset to {self.healt}\n")

    def buyarmor(self):
        self.bounty -= 3
        self.armor += 2
        print(f"The armor cost you 3 coins. Your bounty tally is now {self.bounty} coins.")

    def buyevade(self):
        self.bounty -= 4
        self.evade += 2
        print(f"The Evade cost you 4 coins. Your bounty tally is now {self.bounty} coins.")

    def attack(self, enemy):
        if random.randint(1, 5) == 2:
            enemy.health -= 2 * self.power
        else:
            enemy.health -= self.power
        print("You did {} damage to the {}.".format(self.power, enemy.name))
        if self.health <= 0:
            print("You are dead.")

        if enemy.name == "Zombie" and enemy.health <= 0:
            print("Zombie is not dying! Flee!")
        elif enemy.health <= 0 and enemy.name != "Zombie":
            print(f"You killed the {enemy.name}!")
            self.collectbounty(enemy)#calling the bounty fxn

    def print_status(self):
        print("You have {} health, {} power, {} Armor, and {} Evade.".format(self.health, self.power, self.armor, self.evade))
        print(f"You currently have {self.bounty} coins\n")

class Medic(characters):
    def __init__(self, health, power, armor, evade):
        super(Medic, self).__init__(health, power)
        self.name = "Medic"
        self.bounty = 5
        self.armor = armor
        self.evade = evade

    def collectbounty(self, enemy):
        if enemy.name == "Goblin":
            self.bounty += 2
        elif enemy.name == "Wizard":
            self.bounty += 6
        elif enemy.name == "Dragon":
            self.bounty += 10
        print(f"You collected {enemy.bounty} coins.")
        print(f"Your total bounty tally is now {self.bounty} coins.")

    def buysupertonic(self):
            self.health = 10
            self.bounty -= 5
            print(f"SuperTonic cost you 5 coins. Your bounty tally is now {self.bounty} coins.")
            print(f"Your health is now reset to {self.health}\n")

    def buyarmor(self):
        self.bounty -= 3
        self.armor += 2
        print(f"The armor cost you 3 coins. Your bounty tally is now {self.bounty} coins.")

    def buyevade(self):
        self.bounty -= 4
        self.evade += 2
        print(f"The Evade cost you 4 coins. Your bounty tally is now {self.bounty} coins.")

    def attack(self, enemy):
        enemy.health -= self.power
        print("You did {} damage to the {}.".format(self.power, enemy.name))
        if self.health <= 0:
            print("You are dead.")

        if enemy.name == "Zombie" and enemy.health <= 0:
            print("Zombie is not dying! Flee!")
        elif enemy.health <= 0 and enemy.name != "Zombie":
            print(f"You killed the {enemy.name}!\n")
            self.collectbounty(enemy) #calling the bounty fxn

    def print_status(self):
        print("You have {} health, {} power, {} Armor, and {} Evade".format(self.health, self.power, self.armor, self.evade))
        print(f"You currently have {self.bounty} coins\n")
        

class Shadow(characters):
    def __init__(self, health, power, armor, evade):
        super(Shadow, self).__init__(health, power)
        self.name = "Shadow"
        self.bounty = 5
        self.armor = armor
        self.evade = evade

    def collectbounty(self, enemy):
        if enemy.name == "Goblin":
            self.bounty += 2
        elif enemy.name == "Wizard":
            self.bounty += 6
        elif enemy.name == "Dragon":
            self.bounty += 10
        print(f"You collected {enemy.bounty} coins.")
        print(f"Your total bounty tally is {self.bounty} coins.\n")

    def buysupertonic(self):
            self.health += 10
            self.bounty -= 5
            print(f"SuperTonic cost you 5 coins. Your bounty tally is now {self.bounty} coins.")
            print(f"Your health is now reset to {self.health}")

    def buyarmor(self):
        self.bounty -= 3
        self.armor += 2
        print(f"The armor cost you 3 coins. Your bounty tally is now {self.bounty} coins.")

    def buyevade(self):
        self.bounty -= 4
        self.evade += 2
        print(f"The Evade cost you 4 coins. Your bounty tally is now {self.bounty} coins.")

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enemy.name))
        if self.health <= 0:
            print("You are dead.")

        if enemy.name == "Zombie" and enemy.health <= 0:
            print("Zombie is not dying! Flee!")
        elif enemy.health <= 0 and enemy.name != "Zombie":
            print(f"You killed the {enemy.name}!")
            self.collectbounty(enemy)#calling the bounty fxn

    def print_status(self):
        print("You have {} health, {} power, {} Armor, and {} Evade.".format(self.health, self.power, self.armor, self.evade))
        print(f"You currently have {self.bounty} coins.\n")


class Goblin(characters):
    def __init__(self, health, power):
        super(Goblin, self).__init__(health, power)
        self.name = "Goblin"
        self.bounty = 2
    
    def attack(self, enemy):
        #20% probability that medic recuperates 2 health
        if random.randint(1, 5) == 2 and enemy.name == "Medic":
            enemy.health += 2
        elif enemy.armor > 0:
            enemy.health -= self.power/enemy.armor
        elif random.randint(1, 10) == 1 and enemy.name == "Shadow":
            enemy.health -= self.power
        elif enemy.name == "Shadow":
            enemy.health = 1
        elif enemy.evade == 2 and random.randint(1, 10) == 1: # 10% chance that attack will result in no harm to hero
                enemy.health -= 0
        elif enemy.evade == 4 and random.randint(1, 5) == 1:
                enemy.health -= 0
        elif enemy.evade == 6 and random.randint(1, 3) == 1:
                enemy.health -= 0
        elif enemy.evade >= 8 and random.randint(1, 2) == 1:
                enemy.health -= 0
        else:
            enemy.health -= self.power

        print("The {} does {} damage to you.".format(self.name, self.power))
        if self.health <= 0:
            print(f"The {self.name} is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
        #print("The goblin is dead.")

class Zombie(characters):
    def __init__(self, health, power):
        super(Zombie, self).__init__(health, power)
        self.name = "Zombie"
        #self.bounty = 10

    def attack(self, enemy):
        #20% probability that medic recuperates 2 health
        if random.randint(1, 5) == 2 and enemy.name == "Medic":
            enemy.health += 2
        elif enemy.armor > 0:
            enemy.health -= self.power/enemy.armor
        elif random.randint(1, 10) == 1 and enemy.name == "Shadow":
            enemy.health -= self.power
        elif enemy.name == "Shadow":
            enemy.health = 1
        elif enemy.evade == 2 and random.randint(1, 10) == 1: # 10% chance that attack will result in no harm to hero
                enemy.health -= 0
        elif enemy.evade == 4 and random.randint(1, 5) == 1:
                enemy.health -= 0
        elif enemy.evade == 6 and random.randint(1, 3) == 1:
                enemy.health -= 0
        elif enemy.evade >= 8 and random.randint(1, 2) == 1:
                enemy.health -= 0
        else:
            enemy.health -= self.power

        print("The {} does {} damage to you, and his health and power remains the same. Flee!".format(self.name, self.power))
        if self.health <= 0:
            print(f"The {self.name} is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))


class Wizard(characters):
    def __init__(self, health, power):
        super(Wizard, self).__init__(health, power)
        self.name = "Wizard"
        self.bounty = 6

    def attack(self, enemy):
        #20% probability that medic recuperates 2 health
        if random.randint(1, 5) == 2 and enemy.name == "Medic":
            enemy.health += 2
        elif enemy.armor > 0:
            enemy.health -= self.power/enemy.armor
        elif random.randint(1, 10) == 1 and enemy.name == "Shadow":
            enemy.health -= self.power
        elif enemy.name == "Shadow":
            enemy.health = 1
        elif enemy.evade == 2 and random.randint(1, 10) == 1: # 10% chance that attack will result in no harm to hero
                enemy.health -= 0
        elif enemy.evade == 4 and random.randint(1, 5) == 1:
                enemy.health -= 0
        elif enemy.evade == 6 and random.randint(1, 3) == 1:
                enemy.health -= 0
        elif enemy.evade >= 8 and random.randint(1, 2) == 1:
                enemy.health -= 0
        else:
            enemy.health -= self.power

        print("The {} does {} damage to you.".format(self.name, self.power))

        if random.randint(1, 5) == 1: #Wizard casts a spell and steals all belongings
            enemy.bounty = 0
            enemy.armor = 0
            enemy.evade = 0
            print("\nWizard cast a spell on you! All your coins and items are gone.\n")

        if self.health <= 0:
            print(f"The {self.name} is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Dragon(characters):
    def __init__(self, health, power):
        super(Dragon, self).__init__(health, power)
        self.name = "Dragon"
        self.bounty = 10

    def attack(self, enemy):
        #20% probability that medic recuperates 2 health
        if random.randint(1, 5) == 2 and enemy.name == "Medic":
            enemy.health += 2
        elif enemy.armor > 0:
            enemy.health -= self.power/enemy.armor
        elif random.randint(1, 10) == 1 and enemy.name == "Shadow":
            enemy.health -= self.power
        elif enemy.name == "Shadow":
            enemy.health = 1
        elif enemy.evade == 2 and random.randint(1, 10) == 1: # 10% chance that attack will result in no harm to hero
                enemy.health -= 0
        elif enemy.evade == 4 and random.randint(1, 5) == 1:
                enemy.health -= 0
        elif enemy.evade == 6 and random.randint(1, 3) == 1:
                enemy.health -= 0
        elif enemy.evade >= 8 and random.randint(1, 2) == 1:
                enemy.health -= 0
        else:
            enemy.health -= self.power

        if random.randint(1, 5) == 1 and enemy.armor > 0:
            enemy.armor = 0
            print("\nDragon breathed fire on you and destroyed your armor!\n")

        print("The {} does {} damage to you.".format(self.name, self.power))
        if self.health <= 0:
            print(f"The {self.name} is dead.")
        if enemy.health <= 0:
            print("You are dead!")
                
    def print_status(self):
        print("The {} has {} health and {} power.\n".format(self.name, self.health, self.power))


def main():

    # hero = Medic(20,3)
    # hero = Shadow(1, 5)
    # #hero = Hero(10, 5) #(health, power)
    # enemy = Goblin(10, 4)
    # enemy = Zombie(20, 2) #health was 6 here
    # zombie = Zombie(2, 2)
    print("Which hero do you want to be?")
    print("a. HeMan")
    print("b. Medic")
    print("c. Shadow")
    raw_input = input().lower()
    if raw_input == "heman":
        hero = HeMan(10, 5, 0, 0) #(health, power, armor, evade)
    elif raw_input == "shadow":
        hero = Shadow(8, 5, 0, 0)
    elif raw_input == "medic":
        hero = Medic(6, 3, 0, 0)
    hero.print_status()

    print("\nType the name of the enemy you want to face?")
    print("a. Goblin")
    print("b. Zombie")
    print("c. Wizard")
    print("d. Dragon")
    raw_input = input().lower()
    if  raw_input == "goblin":
        enemy = Goblin(10, 3)
    elif raw_input == "zombie":
        enemy = Zombie(10, 2)
    elif raw_input == "wizard":
        enemy = Wizard(15, 5)
    elif raw_input == "dragon":
        enemy = Dragon(20, 6)   
    enemy.print_status()


    while enemy.alive() and hero.alive():
        # zombie.print_status()
        print("\nWhat do you want to do (enter 1-4)?")
        print(f"1. Fight {enemy.name}")
        print(f"2. Do nothing ({enemy.name} fights you)") # print("2. Zombie fights you")
        print(f"3. Buy item")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "Goblin":
            enemy = Goblin(10, 4)
        elif raw_input == "1":
            #Hero attacks goblin
            hero.attack(enemy)
        elif raw_input == "2":
            enemy.attack(hero)
        elif raw_input == "3":
            print("\nType the name of the item would you like to buy?")
            print("a. SuperTonic")
            print("b. Armor")
            print("c. Evade")
            
            raw_input = input().lower()
            if raw_input == "supertonic":
                if hero.bounty < 5:
                    print("\nYou don't have enough coins to buy SuperTonic!\n")
                else:
                    hero.buysupertonic()
            if raw_input == "armor":
                if hero.bounty < 3:
                    print("\nYou don't have enough coins to buy Armor!\n")
                else:
                    hero.buyarmor()
            if raw_input == "evade":
                if hero.bounty < 4:
                    print("\nYou don't have enough coins to buy Evade!\n")
                else:
                    hero.buyevade()       

        elif raw_input == "4":
            print("Goodbye")
            break
      
        else:
            print("Invalid input {}".format(raw_input))
        enemy.print_status()
        hero.print_status()


main()
