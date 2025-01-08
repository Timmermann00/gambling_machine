from gamling_machine import handle_player, print_options, handle_choice

if __name__ == "__main__":
    player = handle_player()

    while True:
        choice = print_options()
        returnValue = handle_choice(player, choice)

        if returnValue is None:
            break