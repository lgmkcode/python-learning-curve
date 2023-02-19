def create_team_list():
    empty_list = []
    return empty_list


def add_player(list_player):
    while True:
        name = input("Player Name: ")
        last_name = input("Player Last Name: ")
        team = input("Player's Team : ")
        list_player.append([name, last_name, team])

        print("any player is exist press [y], not press [n]")
        if input() == "n":
            break


def print_team_members(list_player):
    for i in range(0, (len(list_player))):
        print("Player Name: {}\nPlayer Last Name: {}\nPlayer's Team: {}".format(list_player[i][0], list_player[i][1], list_player[i][2]))


def print_log(message):
    print(message)


if __name__ == "__main__":
    print_log("===============player registration system===============")
    team_list = create_team_list()
    print_log("Created team list")
    add_player(team_list)
    print_log("added team members to list")
    print_team_members(team_list)
    print_log("printed team list")
