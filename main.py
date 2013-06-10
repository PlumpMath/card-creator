from card_sets import main_set
from page import generate_pages_from_set

ALL = range(0, 100)

generate_pages_from_set(main_set, card_indexes = ALL, save = False, show = True)
