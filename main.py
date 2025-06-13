
import random
import time
global totalRolls
speed = 0.5
totalRolls = 0
rolled_coins = 0
coins = 0
reroll = 0
common_coins = 0
exotic_unlocked = False
exotic_printed = False
print("welcome to rng")
while True:
    if totalRolls >= 100:
        print("congratulations! for reaching 100 rolls, you have been awarded with the 25 rolls option!")
    a = input("type the amount of times you would like to roll? (1, 5 or 10 times) ")

    if a == "1":
        n = 1
    elif a == "5":
        n = 5
    elif a == "10":
        n = 10
    if totalRolls >= 100 and a == "25":
        n = 25
    if int(a) > 10 and totalRolls < 100:
        print("invalid syntax, setting to 1 roll...")
        n = 1
    totalRolls += n
    common = 0
    uncommon = 0
    rare = 0
    epic = 0
    legendary = 0
    mythic = 0
    if exotic_unlocked == True:
        exotic = 0
    for i in range (int(n)):
        print("rolling...", " "*100, end="\r")
        time.sleep(speed)
        if exotic_unlocked == True:
            if exotic_printed == False:
                print("ExOtIc rarity is a 1/300 chance, and gives you 500 coins!")
                exotic_printed = True
            roll = (random.randint(1, 300))
            if roll < 150:
                rarity = "common"
                rolled_coins += 1
                common += 1
            if roll >= 150 and roll <= 241:
                rarity = "uncommon"
                uncommon += 1
                rolled_coins += 3
            if roll >= 241 and roll <= 271:
                rarity = "rare"
                rare += 1
                rolled_coins += 10
            if roll >= 271 and roll <= 291:
                rarity = "epic"
                epic += 1
                rolled_coins += 20
            if roll >= 291 and roll <= 296:
                rarity = "legendary"
                legendary += 1
                rolled_coins += 50
            if roll >= 296 and roll != 300:
                rarity = "mythic"
                mythic += 1
                rolled_coins += 100
            if roll == 300:
                rarity = "exotic"
                rolled_coins += 500
                print("FANTASTIC!!!! you rolled ExOtIc rarity!!!!!!!", end="\r")
            print("you rolled ", rarity , "!")
            if rarity == "epic":
                print("wow! you got epic!", end="\r")
            if rarity == "legendary":
                print("WoOoOw!!!!! YOU GOT LEGENDARY!!!!!!!!!", end="\r")
            if rarity == "mythic":
                print("AMAZING!!!!!!!! YOU GOT MYTHIC!!!!!!!!!!", end="\r")
        else:
            roll = (random.randint(1, 150))
            if roll < reroll:
                roll = (random.randint(1, 150))
                print("rerolled!")
            if roll < 100:
                rarity = "common"
                rolled_coins += 1
                common += 1
            if roll >= 100 and roll <= 130:
                rarity = "uncommon"
                uncommon += 1
                rolled_coins += 3
            if roll >= 131 and roll <= 141:
                rarity = "rare"
                rare += 1
                rolled_coins += 10
            if roll >= 142 and roll <= 147:
                rarity = "epic"
                epic += 1
                rolled_coins += 20
            if roll >= 148 and roll != 150:
                rarity = "legendary"
                legendary += 1
                rolled_coins += 50
            if roll == 150:
                rarity = "mythic"
                mythic += 1
                rolled_coins += 100
            print("you rolled ", rarity , "!",)
            if rarity == "epic":
                print("wow! you got epic!", end="\r")
            if rarity == "legendary":
                print("WoOoOw!!!!! YOU GOT LEGENDARY!!!!!!!!!", end="\r")
            if rarity == "mythic":
                print("AMAZING!!!!!!!! YOU GOT MYTHIC!!!!!!!!!!", end="\r")

            time.sleep(speed)
    print("you rolled common ", common, " times")
    time.sleep(0.5)
    print("you rolled uncommon ", uncommon, " times")
    time.sleep(0.5)
    print("you rolled rare ", rare, " times")
    time.sleep(0.5)
    print("you rolled epic ", epic, " times")
    time.sleep(0.5)
    print("you rolled legendary ", legendary, " times")
    time.sleep(0.5)
    print("you rolled mythic", mythic, "times")
    time.sleep(0.5)
    if exotic_unlocked == True:
        print("you rolled exotic", exotic, "times")
    rolled_coins = rolled_coins + common_coins
    print("you earned", rolled_coins, "coins")
    coins += rolled_coins
    rolled_coins = 0
    print("you have rolled a total of", totalRolls, "times")
    time.sleep(0.5)
    print("you have accumulated a total of", coins, "coins")
    s = input("would you like to spend your coins in the shop? ")
    if s == "yes":
        u = input("would you like to upgrade your rolling speed, luck, or unlock new rarities? (type speed, luck or rarities)")
        if u == "speed":
            confirm = input("upgrading rolling speed from 0.5 seconds -> 0.45 seconds for 40 coins?")
            if confirm == "yes":
                if coins >= 40:
                    coins -= 40
                    speed = 0.45
                else:
                    print("ERROR. not enough coins for upgrade. sending you to rolling...")
            else:
                print("sending you to rolling...")
        if u == "luck":
            confirm = input("upgrading reroll chance by 0 -> less than 110 for 100 coins")
            if confirm == "yes":
                if coins >= 100:
                    coins -= 100
                    reroll = 110
                else:
                    print("ERROR, not enough coins for upgrade, sending you to rolling...")
            else:
                print("sending you to rolling")
            if u == "rarity":
                confirm = input("would you like to unlock a NEW RARITY?!?! ")
                if confirm == "yes":
                    confirm2 = input("unlocking ExOtIc for 200 coins ")
                    if confirm2 == "yes":
                        if coins >= 200:
                            coins -= 200
                            print("you have unlocked ExOtIc rarity!")
                            print("ExOtIc rarity is a 1/300 chance, and gives you 500 coins!")
                            exotic_unlocked = True
                        else:
                            print("ERROR, not enough coins for upgrade, sending you to rolling...")
                    else:
                        print("sending you to rolling...")
                print("this feature has not come out yet, but it's in the works!")
                print("sending you to rolling...")
    else:
        print("sending you to rolling...")
    r = input("would you like to roll again? (yes or no) ")
    if r == "yes":
        time.sleep(0)
    if r == "no":
        break