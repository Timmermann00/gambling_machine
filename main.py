import game
import playerDatabase

balance = 0
player = playerDatabase.handle_player()

while True:
    choice = game.print_options()
    balance = game.handle_choice(choice, balance)
    
    if balance is None:
        break