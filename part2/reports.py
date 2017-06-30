def count_games(file_name):
    game_counter = 0
    with open(file_name) as game_names_file:
        while game_names_file.readline() != "":
            game_counter += 1
    return game_counter


def get_most_played(file_name):
    copyes_sold = 0
    most_played_title = str()
    with open(file_name) as games_file:
        for line in games_file.readlines():
            if copyes_sold < float(line.split("\t")[1]):
                copyes_sold = float(line.split("\t")[1])
                most_played_title = line.split("\t")[0]
        return most_played_title


def sum_sold(file_name):
    summa = 0
    with open(file_name) as games_file:
        for line in games_file.readlines():
            summa += float(line.split("\t")[1])
        return summa


def get_selling_avg(file_name):
    try:
        games_num = count_games(file_name)
        if games_num == 0:
            raise ValueError("There was an error reading the file or the file contains no lines to read")
        summa = sum_sold(file_name)
    except ValueError as error:
        print(error)
    else:
        return (summa/games_num)


def count_longest_title(file_name):
    longest_title_length = 0
    with open(file_name) as games_file:
        try:
            for line in games_file.readlines():
                # longest_title_length = (len(line.split("\t")[0]) if longest_title_length < len(line.split("\t")[0]))
                if longest_title_length < len(line.split("\t")[0]):
                    longest_title_length = len(line.split("\t")[0])
            if longest_title_length == 0:
                raise ValueError(
                    "There was a problem reading the titles or the title you are looking for is not in the given file")
        except ValueError as error:
            print(error)
        else:
            return longest_title_length


def sum_year(file_name):
    years_sum = 0
    with open(file_name) as games_file:
        for line in games_file.readlines():
            years_sum += float(line.split("\t")[2])
        return years_sum


# maybe i should throw file error or something else instead of ValueError
def get_date_avg(file_name):
    try:
        games_num = count_games(file_name)
        if games_num == 0:
            raise ValueError("There was an error reading the file or the file contains no lines to read")
        sum_of_years = sum_year(file_name)
    except ValueError as error:
        print(error)
    else:
        return round(sum_of_years/games_num)


def get_game(file_name, title):
    game_list = list()
    with open(file_name) as games_file:
        try:
            for line in games_file.readlines():
                if line.split("\t")[0] == title:
                    game_list = line.split("\t")
                    game_list[1] = float(game_list[1])
                    game_list[2] = int(game_list[2])
                    game_list[4] = game_list[4].rstrip()
            if len(game_list) == 0:
                raise ValueError("The given file didn't contain the asked title")
        except ValueError as error:
            print(error)
        else:
            return game_list
