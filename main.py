from card_sets import main_set
from page import generate_pages_from_set
from settings import poker_card_settings
from stats import print_stats

ALL = range(0, 999)

generate_pages_from_set(main_set, poker_card_settings, card_indexes = ALL, save = False, show = True)

#print_stats(main_set)

