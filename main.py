from card_sets import main_set
from page import generate_pages_from_set
from settings import poker_card_settings
from stats import print_stats

ALL = range(32, 35)

new = [6, 8, 9, 14, 16, 22, 26, 32, 33, 34, 5]

generate_pages_from_set(main_set, poker_card_settings, card_indexes = new, save = False, show = True)

#print_stats(main_set)

