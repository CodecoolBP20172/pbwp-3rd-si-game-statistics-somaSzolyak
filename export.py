import printing


def count_games_export(file_name, export_file):

    export_file.write("{}\n".format(printing.count_games_print(file_name)))


def decide_export(file_name, year, export_file):

    export_file.write("{}\n".format(printing.decide_print(file_name, year)))


def get_latest_export(file_name, export_file):

    export_file.write("{}\n".format(printing.get_latest_print(file_name)))


def count_by_genre_export(file_name, genre, export_file):

    export_file.write("{}\n".format(printing.count_by_genre_print(file_name, genre)))


def get_line_number_by_title_export(file_name, title, export_file):

    export_file.write("{}\n".format(printing.get_line_number_by_title_print(file_name, title)))


def main():
    name_of_the_file = "game_stat.txt"
    year = 2000
    genre = "RPG"
    title = "Half-Life"
    with open("results.txt", "w") as export_file:

        count_games_export(name_of_the_file, export_file)
        decide_export(name_of_the_file, year, export_file)
        get_latest_export(name_of_the_file, export_file)
        count_by_genre_export(name_of_the_file, genre, export_file)
        get_line_number_by_title_export(name_of_the_file, title, export_file)


main()
