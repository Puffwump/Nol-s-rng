import random as rd, time as tm

game = {
    "speed": 1,
    "coins": 0,
    "common": 0,
    "uncommon": 0,
    "rare": 0,
    "epic": 0,
    "legendary": 0,
    "mythic": 0,
    "exotic": 0,
    "exotic_unlocked": False
}

def roll_rarity():
    roll = rd.randint(1, 500)

    if roll <=50: rarity = "common"
    elif roll <= 100: rarity = "uncommon"
    elif roll <= 150: rarity = "rare"
    elif roll <= 200: rarity = "epic"
    elif roll <= 250: rarity = "legendary"
    elif roll < 500: rarity = "mythic"
    elif roll == 500 and game["exotic_unlocked"]: rarity = "exotic"
    elif roll == 500 and not game["exotic_unlocked"]: game["exotic_unlocked"] = True;


    return rarity

def roll(count):
    for i in range( 0, count ):
        rarity = roll_rarity()
        print(f"You rolled {rarity} rarity!", end = "\r")
        tm.sleep(0.5)

        time_now = tm.time()

        spinner = ['|', '/', '-', '\\']
        while tm.time() - time_now < game["speed"]:
            for char in spinner:
                print(char, " "*100 , end = "\r")
                tm.sleep(0.05)

    if rarity == "common": game["coins"] += 1; game["common"] += 1
    elif rarity == "uncommon": game["coins"] += 3; game["uncommon"] += 1
    elif rarity == "rare": game["coins"] += 10; game["rare"] += 1
    elif rarity == "epic": game["coins"] += 20; game["epic"] += 1
    elif rarity == "legendary": game["coins"] += 50; game["legendary"] += 1
    elif rarity == "mythic": game["coins"] += 100; game["mythic"] += 1
    elif rarity == "exotic": game["coins"] += 500; game["exotic"] += 1

roll(int(input("\nEnter the number of rolls: ")))