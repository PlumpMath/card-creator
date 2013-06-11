from card_sets import main_set
from page import generate_pages_from_set
from stats import print_stats

ALL = range(0, 999)

generate_pages_from_set(main_set, card_indexes = [8,13,18,19,24,25,26,27,28,29,30,31], save = True, show = False)

print_stats(main_set)

