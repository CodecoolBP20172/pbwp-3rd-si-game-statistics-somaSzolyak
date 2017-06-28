

def count_games(file_name):
    game_counter = 0
    with open(file_name) as game_names_file:
        while game_names_file.readline() != "":
            game_counter += 1
    return game_counter


def decide(file_name, year):
    data_str = str("not empty")
    data_list = list()
    with open(file_name) as games_file:
        data_str = games_file.readline()
        while len(data_str) > 1:
            data_list = data_str.split("\t")
            data_list[4] = data_list[4].rstrip()
            if int(data_list[2]) == year:
                return True

            data_str = games_file.readline()
    return False
