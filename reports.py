

def count_games(file_name):
    game_counter = 0
    with open(file_name) as game_names_file:
        while game_names_file.readline() != "":
            game_counter += 1
    return game_counter


def decide(file_name, year):
    with open(file_name) as games_file:
        for line in games_file.readlines():
            year_in_line = int(line.split("\t")[2])
            if len(line) > 1 and year == year_in_line:
                return True
    return False


def get_latest(file_name):
    cur_latest = 0
    latest_title = str()
    with open(file_name) as games_file:
        for line in games_file.readlines():
            cur_year = int(line.split("\t")[2])
            cur_title = line.split("\t")[0]
            if cur_latest < cur_year:
                cur_latest = cur_year
                latest_title = cur_title
    return latest_title


def count_by_genre(file_name, genre):
    games_of_genre = 0
    with open(file_name) as games_file:
        for line in games_file.readlines():
            if genre == line.split("\t")[3]:
                games_of_genre += 1
    return games_of_genre


def get_line_number_by_title(file_name, title):
    data_str = str("not empty")
    data_list = list()
    row_num = 0
    with open(file_name) as games_file:
        try:
            data_str = games_file.readline()
            row_num += 1
            while len(data_str) > 1:
                data_list = data_str.split("\t")
                data_list[4] = data_list[4].rstrip()
                if title == data_list[0]:
                    return row_num
                data_str = games_file.readline()
                row_num += 1
            if row_num >= 0 or row_num > 24:
                raise ValueError("There is no such title in the file as {}".format(title))
        except ValueError as error:
            print("Value Error: {}".format(error))
        return None
