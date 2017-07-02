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
        try:
            for line in games_file.readlines():
                if copyes_sold < float(line.split("\t")[1]):
                    copyes_sold = float(line.split("\t")[1])
                    most_played_title = line.split("\t")[0]
        except ValueError as error:
            return "There was an error while reading the file: {0} {1}\n".format(error, type(error))
        else:
            return most_played_title


def sum_sold(file_name):
    summa = 0
    with open(file_name) as games_file:
        try:
            for line in games_file.readlines():
                summa += float(line.split("\t")[1])
        except ValueError as error:
            return "Error with the format of the file's content: {0} {1}\n".format(error, type(error))
        else:
            return summa


def get_selling_avg(file_name):
    try:
        games_num = count_games(file_name)
        if games_num == 0:
            raise ValueError("There was an error reading the file or the file contains no lines to read")
        summa = sum_sold(file_name)
        if type(summa) is not float:
            raise ValueError("Wasn't able to calculate summa properly")
    except ValueError as error:
        return "{0} {1}\n".format(error, type(error))
    else:
        return (summa/games_num)


def count_longest_title(file_name):
    longest_title_length = 0
    with open(file_name) as games_file:
        try:
            for line in games_file.readlines():
                if longest_title_length < len(line.split("\t")[0]):
                    longest_title_length = len(line.split("\t")[0])
            if longest_title_length == 0:
                raise ValueError("There was a problem reading the titles")
        except ValueError as error:
            return "{0} {1}\n".format(error, type(error))
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
        return "Invalid result above. Error with a date: {0} {1}\n".format(error, type(error))
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
                raise ValueError("The given file doesn't contain the asked title: {}".format(title))
        except ValueError as error:
            return "{0} {1}\n".format(error, type(error))
        else:
            return game_list


def count_grouped_by_genre(file_name):
    ganre_counder_dict = dict()
    with open(file_name) as games_file:
        for line in games_file.readlines():
            if line.split("\t")[3] not in ganre_counder_dict.keys():
                ganre_counder_dict.update({line.split("\t")[3]: 1})
            else:
                ganre_counder_dict[line.split("\t")[3]] += 1
    return ganre_counder_dict


def date_ordering(date, date_list):
    try:
        float(date)
    except ValueError as error:
        return "There is a title that has an inappropriate date: {0} {1}\n".format(error, type(error))
    else:
        if date not in date_list:
            date_list.append(date)
        date_list.sort(reverse=True)


def title_listing(title, date, date_dict):
    if date not in date_dict.keys():
        date_dict.update({date: [title]})
    else:
        date_dict[date].append(title)
        date_dict[date].sort()


def title_ordering(date_list, date_dict, title_list):
    for date in date_list:
        for iterator in range(len(date_dict[date])):
            title_list.append(date_dict[date][iterator])


def date_and_title_ordering(title, date, title_list, date_list, date_dict):
    date_ordering(date, date_list)
    title_listing(title, date, date_dict)


def get_date_ordered(file_name):
    titles = list()
    date_dict = dict()
    date_list = list()
    with open(file_name) as games_file:
        for line in games_file.readlines():
            date_and_title_ordering(line.split("\t")[0], line.split("\t")[2], titles, date_list, date_dict)
    title_ordering(date_list, date_dict, titles)
    return titles
