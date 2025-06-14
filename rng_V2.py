import random as rd, time as tm, os, json, sys

class Styles:
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CLEAR_LINE = "\033[2K"
    PURPLE = "\033[95m"

print(f"{Styles.MAGENTA}\nWelcome to the RNG Game!{Styles.RESET}")
print(f"{Styles.CYAN}Roll the dice and earn coins based on the rarity of your rolls!{Styles.RESET}\n")
print(f"{Styles.YELLOW}Type 'help' for available commands.{Styles.RESET}\n")

game = {
    "speed": 1,
    "coins": 0,
    "rarities": [
        {"name": "common", "count": 0, "reward": 1, "chance": 300},
        {"name": "uncommon", "count": 0, "reward": 3, "chance": 400},
        {"name": "rare", "count": 0, "reward": 10, "chance": 470},
        {"name": "epic", "count": 0, "reward": 20, "chance": 490},
        {"name": "legendary", "count": 0, "reward": 50, "chance": 497},
        {"name": "mythic", "count": 0, "reward": 100, "chance": 499},
        {"name": "exotic", "count": 0, "reward": 500, "chance": 500},
    ],
    "coin_multiplier": 1,
    "rolled_coins": 0,
    "exotic_unlocked": False,
    "max_rolls": 10,
    "max_roll_rarity": None
}

game["max_roll_rarity"] = game["rarities"][-1]["chance"]

def prompt_roll():
    try:
        rolls = int(input(f"How many rolls (max {game['max_rolls']})? "))
        if not (1 <= rolls <= game["max_rolls"]):
            print(f"{Styles.RED}\nPlease enter a number between 1 and {game['max_rolls']}.{Styles.RESET}")
            return prompt_roll()
    except ValueError:
        print(Styles.RED, "\nInvalid input. Please enter a valid number.\n", Styles.RESET)
        return prompt_roll()

    for _ in range(rolls):

        time_now = tm.time()
        spinner = ['|', '/', '-', '\\']
        if game["speed"] != 0: 
            while tm.time() - time_now < game["speed"]:
                for char in spinner:
                    print(" "*8, char, " "*100, end="\r")
                    tm.sleep(0.05)

        roll = rd.randint(1, game["max_roll_rarity"])
        for r in game["rarities"]:
            if roll <= r["chance"]:
                if r["name"] == "exotic" and not game["exotic_unlocked"]:
                    game["exotic_unlocked"] = True
                    print(f"{Styles.PURPLE}Exotic rarity unlocked!{Styles.RESET}") 
                    break
                rarity = r
                break

        print(f"You rolled {rarity['name']} rarity!", " "*100, end="\r")

        tm.sleep(0.5 * game["speed"])

        game["rolled_coins"] += rarity["reward"] * game["coin_multiplier"]
        rarity["count"] += 1
    
    if game["coin_multiplier"] > 1:
        p = f" x {game['coin_multiplier']}x coin multiplier!{Styles.RESET}"
    else:
        p = None
    print(f"{Styles.GREEN}You earned {game['rolled_coins']} coins{p if p else ''}", " "*100, end = '\n')
    game["coins"] += game["rolled_coins"]
    game["rolled_coins"] = 0
    print(f"{Styles.YELLOW}Total Coins: {game['coins']}{Styles.RESET}")

def shop():
    print(f"{Styles.BLUE}Welcome to the shop!{Styles.RESET}")
    print(f"{Styles.CYAN}You can spend your coins here to unlock new features or buy items.{Styles.RESET}\n")
    print(f"{Styles.YELLOW}Current Coins: {game['coins']}{Styles.RESET}\n")

    while True:
        i = input(f"{Styles.YELLOW} shop, what would you like to buy? >>> {Styles.RESET}").strip().lower()
        if i in ["exit"]:
            print(f"\n{Styles.GREEN}Exiting shop...{Styles.RESET}\n")
            return
        elif i in ["list", 'help', '']:
            print(f"\n{Styles.CYAN}Available products:\n"
              f"  1. Faster Rolls (speed) - 50 coins: Decrease roll animation time\n"
              f"  2. Coin Multiplier (mult) - 100 coins: Double coins per roll\n"
              f"  3. Increase Max Rolls (max) - 200 coins: Increase max rolls per session by 5\n"
              f"  4. Unlock Exotic Rarity (exotic) - 300 coins: Unlock the exotic rarity for rolls\n"
              f"  5. Increase Luck (luck) - 400 coins: Increase the chances of rolling higher rarities\n"
              f"  Type the product name to buy it!{Styles.RESET}\n")
        elif i in ["speed", "faster", "rollspeed"]:
            if game["coins"] >= 50:
                if game["speed"] > 0.1:
                    game["coins"] -= 50
                    game["speed"] = max(0.1, game["speed"] - 0.1)
                    print(f"\n{Styles.GREEN}Roll speed increased! New speed: {game['speed']}s{Styles.RESET}\n")
                else:
                    print(f"\n{Styles.YELLOW}Roll speed is already at minimum!{Styles.RESET}\n")
            else:
                print(f"\n{Styles.RED}Not enough coins!{Styles.RESET}\n")
        elif i in ["mult", "multiplier", 'coin', 'coins']:
            if game["coins"] >= 100:
                if game["coin_multiplier"] == 1:
                    game["coins"] -= 100
                    game["coin_multiplier"] = 2
                    print(f"\n{Styles.GREEN}Coin multiplier activated! You now earn double coins per roll.{Styles.RESET}\n")
                else:
                    print(f"\n{Styles.YELLOW}Coin multiplier already purchased!{Styles.RESET}\n")
            else:
                print(f"\n{Styles.RED}Not enough coins!{Styles.RESET}\n")
        elif i in ["max", "maxrolls"]:
            if game["coins"] >= 200:
                
                game["coins"] -= 200
                game["max_rolls"] += 5
                print(f"\n{Styles.GREEN}Max rolls per session increased! New max: {game['max_rolls']}{Styles.RESET}\n")
            else:
                print(f"\n{Styles.RED}Not enough coins!{Styles.RESET}\n")
        elif i in ["exotic", "rarity"]:
            if game["coins"] >= 300:
                game["coins"] -= 300
                game["exotic_unlocked"] = True
                print(f"\n{Styles.PURPLE}Exotic rarity unlocked!{Styles.RESET}\n")
            else:
                print(f"\n{Styles.RED}Not enough coins!{Styles.RESET}\n")
        elif i in ["luck"]:
            if game["coins"] >= 400:
                game["coins"] -= 400
                for r in game["rarities"]:
                    r["chance"] += 5
                print(f"\n{Styles.GREEN}Luck increased! All rarity chances increased by 5%.{Styles.RESET}\n")
                game["max_roll_rarity"] = game["rarities"][-1]["chance"]
            else:
                print(f"\n{Styles.RED}Not enough coins!{Styles.RESET}\n")
        else:
            print(f"{Styles.RED}Unknown product. Type 'list' to see available products.{Styles.RESET}")

def main():
    while True:
        try:
            i = input(f"{Styles.MAGENTA}>>> {Styles.RESET}").strip().lower()

            if i in ["exit", "quit"]:
                if input(f'{Styles.YELLOW}Save progress before exiting? (yes/no) >>> {Styles.RESET}').strip().lower() == 'yes':
                    sys.stdout.write('\033[3K\r')
                    sys.stdout.flush()
                    with open(f"{input('What file name would you like to save as? >>> ')}.json", 'w') as f:
                        json.dump(game, f)
                return
            elif i in ["roll", "r"]:
                prompt_roll()
            elif i in ["help", "h"]:
                print(f"{Styles.CYAN}Available commands:\n"
                      f"  roll (or r) - Roll the dice\n"
                      f"  exit (or quit) - Exit the game\n"
                      f"  status (or s) - Show current status\n"
                      f"  shop (or sh) - Open the shop\n"
                      f"  help (or h) - Show this help message{Styles.RESET}")
            elif i in ["status", "s"]:
                print(f"{Styles.BLUE}Current Status:\n"
                      f"  Coins: {game['coins']}\n"
                      f"  Rolled Coins: {game['rolled_coins']}\n"
                      f"  Exotic Unlocked: {'Yes' if game['exotic_unlocked'] else 'No'}\n"
                      f"  Speed: {game['speed']}s\n"
                      f"  Rarities:")
                print(f"    Common: {game['rarities']['common']['count']} (Reward: {game['rarities']['common']['reward']})")
                print(f"    Uncommon: {game['rarities']['uncommon']['count']} (Reward: {game['rarities']['uncommon']['reward']})")
                print(f"    Rare: {game['rarities']['rare']['count']} (Reward: {game['rarities']['rare']['reward']})")
                print(f"    Epic: {game['rarities']['epic']['count']} (Reward: {game['rarities']['epic']['reward']})")
                print(f"    Legendary: {game['rarities']['legendary']['count']} (Reward: {game['rarities']['legendary']['reward']})")
                print(f"    Mythic: {game['rarities']['mythic']['count']} (Reward: {game['rarities']['mythic']['reward']})")
                if game['exotic_unlocked']:
                    print(f"    Exotic: {game['rarities']['exotic']['count']} (Reward: {game['rarities']['exotic']['reward']})")
                print(Styles.RESET)
            elif i in ["shop", "sh"]:
                shop()
            elif i == 'cheat' and os.path.exists('cheat.txt'):
                print("cheat mode activated")
                game["coin_multiplier"] = int(input("Enter coin multiplier: ") or game["coin_multiplier"])
                game["coins"] = int(input("Enter coin amount: ") or game["coins"])
                game["exotic_unlocked"] = bool(input("Enter exotic unlocked (True/False): ") or game["exotic_unlocked"])
                game["max_rolls"] = int(input("Enter max rolls: ") or game["max_rolls"])
                game["speed"] = float(input("Enter speed: ") or game["speed"])
            else:
                print(f"{Styles.RED}Invalid command. Type 'help' to list all commands.{Styles.RESET}")
        except KeyboardInterrupt:
            print(Styles.RED, "\nKeyboardInterrupt, I would suggest using 'quit'", Styles.RESET)

if __name__ == "__main__":
    main()