

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


def get_latest(file_name):
    data_str = str("not empty")
    data_list = list()
    cur_latest = 0
    latest_title = str()
    with open(file_name) as games_file:
        data_str = games_file.readline()
        while len(data_str) > 1:
            data_list = data_str.split("\t")
            data_list[4] = data_list[4].rstrip()
            if int(data_list[2]) > cur_latest:
                cur_latest = int(data_list[2])
                latest_title = data_list[0]
            data_str = games_file.readline()
    return latest_title
