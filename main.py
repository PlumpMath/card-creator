from card_sets import main_set
from paper import generate_papers_from_set, create_paper

generate_papers_from_set(main_set, card_indexes = [0, 1, 2, 3, 4], save = True, show = True)
#create_paper(main_set, [10, 11, 12, 13]).show()
