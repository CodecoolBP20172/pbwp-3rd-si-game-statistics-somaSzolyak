import printing


def get_most_played_export(file_name, export_file):

    export_file.write("{}\n".format(printing.get_most_played_print(file_name)))


def sum_sold_export(file_name, export_file):
    export_file.write("{}\n".format(printing.sum_sold_print(file_name)))


def get_selling_avg_export(file_name, export_file):
    export_file.write("{}\n".format(printing.get_selling_avg_print(file_name)))


def count_longest_title_export(file_name, export_file):
    export_file.write("{}\n".format(printing.count_longest_title_print(file_name)))


def get_date_avg_export(file_name, export_file):
    export_file.write("{}\n".format(printing.get_date_avg_print(file_name)))


def get_game_export(file_name, title, export_file):
    export_file.write("{}\n".format(printing.get_game_print(file_name, title)))


def count_grouped_by_genre_export(file_name, export_file):
    export_file.write("{}\n".format(printing.count_grouped_by_genre_print(file_name)))


def get_date_ordered_export(file_name, export_file):
    export_file.write("{}\n".format(printing.get_date_ordered_print(file_name)))


def main():
    path = "game_stat.txt"
    title = "Half-Life"
    with open("results.txt", "w") as export_file:
        get_most_played_export(path, export_file)
        sum_sold_export(path, export_file)
        get_selling_avg_export(path, export_file)
        count_longest_title_export(path, export_file)
        get_date_avg_export(path, export_file)
        get_game_export(path, title, export_file)
        count_grouped_by_genre_export(path, export_file)
        get_date_ordered_export(path, export_file)


main()
