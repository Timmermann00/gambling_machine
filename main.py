import game
import user

player = user.handle_player()

while True:
    choice = game.print_options()
    returnValue = game.handle_choice(player, choice)
    
    if returnValue is None:
        break