
import random
import time
global totalRolls
speed = 1
totalRolls = 0
rolled_coins = 0
coins = 0
reroll = 0
common_coins = 0
print("\nWelcome to the rolling simulator!")
while True:
    if totalRolls >= 100:
        print("congratulations! for reaching 100 rolls, you have been awarded with the 25 rolls option!")
    a = input("\ntype the amount of times you would like to roll? (1, 5 or 10 times):")
    print("\n")

    if a == "1": n = 1
    elif a == "5": n = 5
    elif a == "10": n = 10
    if totalRolls >= 100 and a == "25": n = 25
    if int(a) > 10 and totalRolls < 100:
        print("invalid syntax, setting to 1 roll... \n")
        n = 1
        
    totalRolls += n
    common = 0
    uncommon = 0
    rare =  0
    epic = 0
    legendary = 0
    mythic = 0

    for i in range (int(n)):
        print("rolling...", end ="\r")
        time.sleep(speed)
        roll = (random.randint(1, 150))
        if roll < reroll: roll = (random.randint(1, 150)); print("rerolled!")
        if roll < 100: rarity = "common"; rolled_coins += 1; common += 1
        if roll >= 100 and roll <= 130: rarity = "uncommon"; uncommon += 1; rolled_coins += 3
        if roll >= 131 and roll <= 141: rarity = "rare"; rare += 1; rolled_coins += 10
        if roll >= 142 and roll <= 147: rarity = "epic"; epic += 1; rolled_coins += 20
        if roll >= 148 and roll != 150: rarity = "legendary"; legendary += 1; rolled_coins += 50
        if roll == 150: rarity = "mythic"; mythic += 1; rolled_coins += 100
        print("you rolled ", rarity , "!")
        if rarity == "epic": print("wow! you got epic!")
        if rarity == "legendary": print("WoOoOw!!!!! YOU GOT LEGENDARY!!!!!!!!!")
        if rarity == "mythic": print("AMAZING!!!!!!!! YOU GOT MYTHIC, WHICH IS THE RAREST ONE, 1/150!!!!!")
        
    types = [common, uncommon, rare, epic, legendary, mythic]
    type_names = ["common", "uncommon", "rare", "epic", "legendary", "mythic"]

    print("\n")
    for i in range(len(types)):
        print("you rolled", type_names[i], types[i], "times")
        time.sleep(0.5)

    rolled_coins = rolled_coins + common_coins
    print("\nyou earned", rolled_coins, "coins")

    coins += rolled_coins
    rolled_coins = 0

    print("you have rolled a total of", totalRolls, "times")
    time.sleep(0.5)

    print("you have accumulated a total of", coins, "coins")

    s = input("\nwould you like to spend your coins in the shop? ")
    if s == "yes":
        u = input("\nWould you like to upgrade your rolling speed, luck, or unlock new rarities? (type speed, luck or rarities): ")
        if u == "speed":
            confirm = input("\nUpgrading rolling speed from 0.5 seconds -> 0.45 seconds for 40 coins? (yes/no): ")
            if confirm == "yes":
                if coins >= 40:
                    coins -= 40
                    speed = 0.45
                    print("\nSpeed upgraded! Rolling will now be faster.\n")
                else:
                    print("\nERROR. Not enough coins for upgrade. Sending you to rolling...\n")
            else:
                print("\nSending you to rolling...\n")
        elif u == "luck":
            confirm = input("\nUpgrading reroll chance by 0 -> less than 110 for 100 coins? (yes/no): ")
            if confirm == "yes":
                if coins >= 100:
                    coins -= 100
                    reroll = 110
                    print("\nLuck upgraded! You now have a better reroll chance.\n")
                else:
                    print("\nERROR, not enough coins for upgrade. Sending you to rolling...\n")
            else:
                print("\nSending you to rolling...\n")
        elif u == "rarity":
            print("\nThis feature has not come out yet, but it's in the works!")
            print("Sending you to rolling...\n")
        else:
            print("\nSending you to rolling...\n")
        r = input("\nWould you like to roll again? (yes or no): ")
    if r == "yes":
        time.sleep(0)
    if r == "no":
        break