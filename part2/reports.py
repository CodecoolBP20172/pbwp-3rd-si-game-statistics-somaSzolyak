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
    games_num = count_games(file_name)
    summa = sum_sold(file_name)
    return (summa/games_num)
