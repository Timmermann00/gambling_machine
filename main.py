import game
import playerDatabase

balance = 0
while True:
    user = input("Enter your username: ")
    if playerDatabase.read_player_stats(user) is None:
        print("There was no user found with your name!")
        print("Please check you spelling and if you want to continue enter 'y'")
        choice = input(f"The name you entered was {user} is this correct?: ")
        if choice == "y":
            print("A user will be created after you stop the game!")
            break
        else:
            continue
    break

while True:
    choice = game.print_options()
    balance = game.handle_choice(choice, balance)
    
    if balance is None:
        break