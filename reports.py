

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
    answer = 0
    with open(file_name) as games_file:
        try:
            number = 0
            for line in games_file.readlines():
                number += 1
                if title == line.split("\t")[0]:
                    answer = number
                    return answer
            if answer == 0:
                raise ValueError("Title either wasn't found in the given list or there was a processing problem")
        except ValueError as error:
            return error
# Idea: what if I only ready the file once and I build a 2 dimensional list out of it and only search in that list
# instead of reading through the file over and over again? the file reading repeating part would be replaced by
# for cicles that go through the list looking for answers. The code would be a litle bit more dry.
# Like 1 less line every function.
