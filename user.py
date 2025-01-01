class User:
    def __init__(self, name, balance, wins, losses):
        self.name = name
        self.balance = int(balance)
        self.wins = int(wins)
        self.losses = int(losses)

    def __repr__(self):
        return f"User(name={self.name}, balance={self.balance}, wins={self.wins}, losses={self.losses})"


def read_player_stats(user_name: str):
    with open("PlayerDatabase.txt") as f:
        for line in f:
            data = line.split()
            if data[0] in user_name:
                return User(data[0], data[1], data[2], data[3])
    return None

def write_player_stats(player: User):
    with open("PlayerDatabase.txt", 'r') as f:
        lines = f.readlines()

    player_found = False
    for i, line in enumerate(lines):
        data = line.split()
        if data[0] == player.name:
            lines[i] = f"{player.name} {player.balance} {player.wins} {player.losses}\n"
            player_found = True
            break

    if not player_found:
        lines.append(f"{player.name} {player.balance} {player.wins} {player.losses}\n")

    with open("PlayerDatabase.txt", 'w') as f:
        f.writelines(lines)

def handle_player():
    while True:
        username = input("Enter your username: ")
        player = read_player_stats(username)
        if player is None:
            print("There was no user found with your name!")
            print("Please check you spelling and if you want to continue enter 'y'")
            choice = input(f"The name you entered was {username} is this correct?: ")
            if choice == "y":
                print("A user will be created after you stop the game!")
                return User(username, 0, 0, 0)
        else:
            return player