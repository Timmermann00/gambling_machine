import game

balance = 0
while True:
    choice = game.print_options()
    balance = game.handle_choice(choice, balance)
    
    if balance is None:
        break