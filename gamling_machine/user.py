import os

class User:
    def __init__(self, name, balance, wins, losses):
        self.name = name
        self.balance = int(balance)
        self.wins = int(wins)
        self.losses = int(losses)

    def __eq__(self, other):
        return (
                isinstance(other, User) and
                self.name == other.name and
                self.balance == other.balance and
                self.wins == other.wins and
                self.losses == other.losses
        )

    def __repr__(self):
        return f"User(name={self.name}, balance={self.balance}, wins={self.wins}, losses={self.losses})"


def read_player_stats(user_name: str):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "PlayerDatabase.txt")
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        data = line.split()
        if data[0] in user_name:
            return User(data[0], data[1], data[2], data[3])
    return None

def write_player_stats(player: User):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "PlayerDatabase.txt")
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()

    player_found = False
    for i, line in enumerate(lines):
        data = line.split()
        if data[0] == player.name:
            lines[i] = f"{player.name} {player.balance} {player.wins} {player.losses}\n"
            player_found = True
            break

    if not player_found:
        lines.append(f"{player.name} {player.balance} {player.wins} {player.losses}\n")

    f = open(file_path, "w")
    f.writelines(lines)
    f.close()

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