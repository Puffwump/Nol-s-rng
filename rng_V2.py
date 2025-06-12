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
    "speed": 0.5,
    "coins": 0,
    "rarities": {
        "common": {"count": 0, "reward": 1},
        "uncommon": {"count": 0, "reward": 3},
        "rare": {"count": 0, "reward": 10},
        "epic": {"count": 0, "reward": 20},
        "legendary": {"count": 0, "reward": 50},
        "mythic": {"count": 0, "reward": 100},
        "exotic": {"count": 0, "reward": 500},
    },
    "rolled_coins": 0,
    "exotic_unlocked": False,
    "max_rolls": 10
}

def prompt_roll():
    try:
        rolls = int(input(f"How many rolls (max {game['max_rolls']})? "))
        if not (1 <= rolls <= game["max_rolls"]):
            print(f"{Colors.RED}\nPlease enter a number between 1 and {game['max_rolls']}.{Colors.RESET}")
            return prompt_roll()
    except ValueError:
        print(Colors.RED, "\nInvalid input. Please enter a valid number.\n", Colors.RESET)
        return prompt_roll()

    for _ in range(rolls):

        time_now = tm.time()
        spinner = ['|', '/', '-', '\\'] 
        while tm.time() - time_now < game["speed"]:
            for char in spinner:
                print(" "*8, char, " "*100, end="\r")
                tm.sleep(0.05)

        roll = rd.randint(1, 500)
        rarity = (
            "common" if roll <= 300 else
            "uncommon" if roll <= 400 else
            "rare" if roll <= 470 else
            "epic" if roll <= 490 else
            "legendary" if roll <= 497 else
            "mythic" if roll <= 499 else
            "exotic"
        )

        if roll == 500 and not game["exotic_unlocked"]:
            game["exotic_unlocked"] = True

        print(f"You rolled {rarity} rarity!", end="\r")
        tm.sleep(0.5)

        game["rolled_coins"] += game["rarities"][rarity]["reward"]
        game["rarities"][rarity]["count"] += 1

    print(f"{Colors.GREEN}You earned {game['rolled_coins']} coins!{Colors.RESET}", " "*100, end = '\n')
    game["coins"] += game["rolled_coins"]
    game["rolled_coins"] = 0
    print(f"{Colors.YELLOW}Total Coins: {game['coins']}{Colors.RESET}")

def main():
    while True:
        try:
            i = input(f"{Colors.MAGENTA}>>> {Colors.RESET}").strip().lower()

            if i in ["exit", "quit"]:
                print(Colors.GREEN, "Thank you for playing! Goodbye!", Colors.RESET)
                return
            elif i in ["roll", "r"]:
                prompt_roll()
            elif i in ["help", "h"]:
                print(f"{Colors.CYAN}Available commands:\n"
                      f"  roll (or r) - Roll the dice\n"
                      f"  exit (or quit) - Exit the game\n"
                      f"  help (or h) - Show this help message{Colors.RESET}")
            elif i in ["status", "s"]:
                print(f"{Colors.BLUE}Current Status:\n"
                      f"  Coins: {game['coins']}\n"
                      f"  Rolled Coins: {game['rolled_coins']}\n"
                      f"  Exotic Unlocked: {'Yes' if game['exotic_unlocked'] else 'No'}\n"
                      f"  Rarities:")
                print(f"    Common: {game['rarities']['common']['count']} (Reward: {game['rarities']['common']['reward']})")
                print(f"    Uncommon: {game['rarities']['uncommon']['count']} (Reward: {game['rarities']['uncommon']['reward']})")
                print(f"    Rare: {game['rarities']['rare']['count']} (Reward: {game['rarities']['rare']['reward']})")
                print(f"    Epic: {game['rarities']['epic']['count']} (Reward: {game['rarities']['epic']['reward']})")
                print(f"    Legendary: {game['rarities']['legendary']['count']} (Reward: {game['rarities']['legendary']['reward']})")
                print(f"    Mythic: {game['rarities']['mythic']['count']} (Reward: {game['rarities']['mythic']['reward']})")
                if game['exotic_unlocked']:
                    print(f"    Exotic: {game['rarities']['exotic']['count']} (Reward: {game['rarities']['exotic']['reward']})")
                print(Colors.RESET)
            else:
                print(f"{Colors.RED}Invalid command. Type 'help' to list all commands.{Colors.RESET}")
        except KeyboardInterrupt:
            print(Colors.RED, "\nKeyboardInterrupt, I would suggest using 'quit'", Colors.RESET)
 
if __name__ == "__main__":
    main()