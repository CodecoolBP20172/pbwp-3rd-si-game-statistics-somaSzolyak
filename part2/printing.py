import pprint
import reports

pp = pprint.PrettyPrinter()


def get_most_played_print(file_name):
    pp.pprint(reports.get_most_played(file_name))
    return reports.get_most_played(file_name)


def sum_sold_print(file_name):
    pp.pprint(reports.sum_sold(file_name))
    return reports.sum_sold(file_name)


def get_selling_avg_print(file_name):
    pp.pprint(reports.get_selling_avg(file_name))
    return reports.get_selling_avg(file_name)


def count_longest_title_print(file_name):
    pp.pprint(reports.count_longest_title(file_name))
    return reports.count_longest_title(file_name)


def get_date_avg_print(file_name):
    pp.pprint(reports.get_date_avg(file_name))
    return reports.get_date_avg(file_name)


def get_game_print(file_name, title):
    pp.pprint(reports.get_game(file_name, title))
    return reports.get_game(file_name, title)


def count_grouped_by_genre_print(file_name):
    pp.pprint(reports.count_grouped_by_genre(file_name))
    return reports.count_grouped_by_genre(file_name)


def get_date_ordered_print(file_name):
    pp.pprint(reports.get_date_ordered(file_name))
    return reports.get_date_ordered(file_name)
