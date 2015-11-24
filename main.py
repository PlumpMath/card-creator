from card_sets import main_set
from page import generate_pages_from_set, generate_separate_card_images_from_set
from settings import poker_card_settings
from stats import print_stats

ALL = range(0, 999)

NEW = [3, 8, 4, 19, 26, 33, 34, 35, 36, 37, 38, 39, 40]

generate_pages_from_set(main_set, poker_card_settings, card_indexes = ALL, save = True, show = True)
#generate_separate_card_images_from_set(main_set, poker_card_settings, ALL, save = True, show = False)

#print_stats(main_set)

