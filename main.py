
import random
import time
global totalRolls
sped_upgrade = 0
reroll_upgrade = 0
speed = 0.5
totalRolls = 0
rolled_coins = 0
coins = 0
reroll = 0
common_coins = 0
exotic_unlocked = False
prismatic_unlocked = False
exotic_printed = False
prismatic_printed = False
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
    if prismatic_unlocked == True:
        prismatic = 0
        for i in range (int(n)):
            print("rolling...", end="\r")
        time.sleep(speed)
        if prismatic_unlocked == True:
            if prismatic_printed == False:
                print("prismatic rarity is a 1/300 chance, and gives you 500 coins!")
                exotic_printed = True
            roll = (random.randint(1, 300))
            if roll < 200:
                rarity = "common"
                rolled_coins += 1
                common += 1
            if roll >= 200 and roll <= 291:
                rarity = "uncommon"
                uncommon += 1
                rolled_coins += 3
            if roll >= 291 and roll <= 321:
                rarity = "rare"
                rare += 1
                rolled_coins += 10
            if roll >= 321 and roll <= 351:
                rarity = "epic"
                epic += 1
                rolled_coins += 20
            if roll >= 351 and roll <= 396:
                rarity = "legendary"
                legendary += 1
                rolled_coins += 50
            if roll >= 396 and roll <=397:
                rarity = "mythic"
                mythic += 1
                rolled_coins += 100
            if roll >= 397 and roll != 400:
                rarity = "exotic"
                exotic += 1
                rolled_coins += 500
            if roll == 400:
                rarity = "prismatic"
                prismatic += 1
                rolled_coins += 1000
                print("THAT'S INSANE!!!! you rolled PRISMATIC rarity!!!!!!!", end="\r")
            print("you rolled ", rarity , "!")
            if rarity == "epic":
                print("wow! you got epic!", end="\r")
            if rarity == "legendary":
                print("WoOoOw!!!!! YOU GOT LEGENDARY!!!!!!!!!", end="\r")
            if rarity == "mythic":
                print("AMAZING!!!!!!!! YOU GOT MYTHIC!!!!!!!!!!", end="\r")
            if rarity == "exotic":
                print("FANTASTIC!!!! you rolled ExOtIc rarity!!!!!!!", end="\r")
    if exotic_unlocked == True:
        exotic = 0
    for i in range (int(n)):
        print("rolling...", end="\r")
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
            if sped_upgrade == 2:
                confirm = input("upgrading rolling speed from 0.4 seconds -> 0.35 seconds for 100 coins?")
                if confirm == "yes":
                    if coins >= 100:
                        coins -= 100
                        speed = 0.35
                        sped_upgrade += 1
                    else:
                        print("ERROR. not enough coins for upgrade. sending you to rolling...")
            if sped_upgrade == 1:
                confirm = input("upgrading rolling speed from 0.45 seconds -> 0.4 seconds for 80 coins?")
                if confirm == "yes":
                    if coins >= 80:
                        coins -= 80
                        speed = 0.4
                        sped_upgrade += 1
                    else:
                        print("ERROR. not enough coins for upgrade. sending you to rolling...")
            else:
                confirm = input("upgrading rolling speed from 0.5 seconds -> 0.45 seconds for 40 coins?")
                if confirm == "yes":
                    if coins >= 40:
                        coins -= 40
                        speed = 0.45
                        sped_upgrade += 1
                    else:
                        print("ERROR. not enough coins for upgrade. sending you to rolling...")
                else:
                    print("sending you to rolling...")
        if u == "luck":
            if reroll_upgrade == 1:
                confirm = input("upgrading reroll chance from less than 110 -> less than 120 for 200 coins")
                if confirm == "yes":
                    if coins >= 200:
                        coins -= 200
                        reroll = 120
                    else:
                        print("ERROR, not enough coins for upgrade, sending you to rolling...")
            confirm = input("upgrading reroll chance by 0 -> less than 110 for 100 coins")
            if confirm == "yes":
                if coins >= 100:
                    coins -= 100
                    reroll = 110
                    reroll_upgrade += 1
                else:
                    print("ERROR, not enough coins for upgrade, sending you to rolling...")
            else:
                print("sending you to rolling")
            if u == "rarity":
                if exotic_unlocked:
                    confirm = input("would you like to unlock another NEW RARITY?!?!")
                    if confirm == "yes":
                        confirm2 = input("unlocking prismatic for 500 coins")
                        if confirm2 == "yes":
                            if coins >= 500:
                                coins -= 500
                                prismatic_unlocked = True
                            else:
                                print("ERROR, not enough coins for upgrade, sending you to rolling...")
                confirm = input("would you like to unlock a NEW RARITY?!?! ")
                if confirm == "yes":
                    confirm2 = input("unlocking Exotic for 200 coins ")
                    if confirm2 == "yes":
                        if coins >= 200:
                            coins -= 200
                            print("you have unlocked Exotic rarity!")
                            print("Exotic rarity is a 1/300 chance, and gives you 500 coins!")
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
