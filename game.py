import random
import user

def rand_word_gen():
    resultList = []
    words = ["Apple", "Orange", "Grapefruit"]
    for y in range(3):
        innerList = []
        for x in range(3):
            innerList.append(random.choice(words))
        resultList.append(innerList)
    return resultList


def print_centered(wordList):
    # Find the longest word in the grid for consistent alignment
    max_width = max(len(word) for row in wordList for word in row)

    # Print the grid with alignment
    for row in wordList:
        print("  ".join(word.ljust(max_width) for word in row))


def define_win_multiplier(resultList):
    fruit_multipliers = {
        "Apple": 2,
        "Orange": 3,
        "Grapefruit": 5
    }

    for row in resultList:
        setTry = set(row)
        if len(setTry) == 1:
            fruit = next(iter(setTry))
            multiplier = fruit_multipliers.get(fruit)
            print("You get three " + fruit + " in a row and a " + str(multiplier) + "x multiplier on your bet!")
            return multiplier

    print("You won nothing!")
    return 0


def get_valid_input(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_game(player: user, bet: int):
    resultList = rand_word_gen()
    print_centered(resultList)
    multiplier = define_win_multiplier(resultList)
    if multiplier != 0:
        player.wins += 1
        player.balance += bet * multiplier
    else:
        player.losses += 1
        player.balance -= bet


def print_options() -> int:
    options = {
        1: "Add Balance",
        2: "Play a game",
        3: "Show Balance",
        4: "Show Stats",
        5: "Quit"
    }

    print("\nOptions:")
    for key, value in options.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("Choose your option: "))
            if choice in options:
                return choice
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def handle_choice(player, choice):
    if choice == 1:
        player.balance = player.balance + get_valid_input("Enter the amount you want to add to your account: ")
        print(f"Your new balance of your account is: {player.balance}")
        return 1
    elif choice == 2:
        bet = get_valid_input("How much do you want to bet?: ")
        if bet > player.balance:
            print("You dont have enough money to make such a bet!")
            return 1
        else:
            play_game(player, bet)
            return 1
    elif choice == 3:
        print(f"Your currently have {player.balance} in your account!")
        return 1
    elif choice == 4:
        win_percentage = (player.wins / (player.wins + player.losses)) * 100
        print(f"You have won {player.wins} and lost {player.losses} thats an overall win percentage of {win_percentage}%")
        return 1
    elif choice == 5:
        print("Thanks for playing!")
        user.write_player_stats(player)
        return None