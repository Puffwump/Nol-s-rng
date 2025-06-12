import random as rd, time as tm

class Colors:
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

game = {
    "speed": 1,
    "coins": 0,
    "rarities":{
        "common": 0,
        "uncommon": 0,
        "rare": 0,
        "epic": 0,
        "legendary": 0,
        "mythic": 0,
        "exotic": 0,
    },
    "exotic_unlocked": False,
    "max_rolls": 10,
}

def roll_rarity():
    roll = rd.randint(1, 500)

    if roll <= 300: rarity = "common"
    elif roll <= 400: rarity = "uncommon"
    elif roll <= 470: rarity = "rare"
    elif roll <= 490: rarity = "epic"
    elif roll <= 497: rarity = "legendary"
    elif roll <= 499: rarity = "mythic"
    elif roll == 500 and game["exotic_unlocked"]: rarity = "exotic"
    elif roll == 500 and not game["exotic_unlocked"]: game["exotic_unlocked"] = True


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
                print(" "*8,char, " "*100 , end = "\r")
                tm.sleep(0.05)

    if rarity == "common": game["coins"] += 1; game["rarities"]["common"] += 1
    elif rarity == "uncommon": game["coins"] += 3; game["rarities"]["uncommon"] += 1
    elif rarity == "rare": game["coins"] += 10; game["rarities"]["rare"] += 1
    elif rarity == "epic": game["coins"] += 20; game["rarities"]["epic"] += 1
    elif rarity == "legendary": game["coins"] += 50; game["rarities"]["legendary"] += 1
    elif rarity == "mythic": game["coins"] += 100; game["rarities"]["mythic"] += 1
    elif rarity == "exotic": game["coins"] += 500; game["rarities"]["exotic"] += 1

def prompt_rolls():
    while True:
        try:
            rolls = int(input(f"How many rolls (max {game['max_rolls']})? "))
            if 1 <= rolls <= game["max_rolls"]:
                roll(rolls)
            else:
                print(f"Please enter a number between 1 and {game['max_rolls']}.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue