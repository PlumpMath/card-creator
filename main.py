from card_sets import main_set
from page import generate_pages_from_set, generate_separate_card_images_from_set
from settings import poker_card_settings
from stats import print_stats

ALL = range(0, 999)

#new = [6, 8, 9, 14, 16, 22, 26, 32, 33, 34, 5]

#generate_pages_from_set(main_set, poker_card_settings, card_indexes = ALL, save = False, show = True)
generate_separate_card_images_from_set(main_set, poker_card_settings, ALL, save = True, show = False)

#print_stats(main_set)

