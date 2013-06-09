from PIL import Image
from card import create_card, a4_size, a4_height, a4_width, poker_height, poker_width
from converters import cm_to_pixels

def create_paper(cards_data_set, margin, spacing):
	cards = [create_card(data) for data in cards_data_set]
	paper = Image.new("RGB", a4_size, "white")
	card_index = 0
	for y in xrange(margin, a4_height - poker_height, poker_height + spacing):
		for x in xrange(margin, a4_width - poker_width, poker_width + spacing):
			card = cards[card_index % len(cards)]
			card_index += 1
			paper.paste(card, (x, y))
	return paper

def generate_papers_from_set(card_set, page_indexes = range(0, 999), save = False, show = True):
	margin = cm_to_pixels(card_set['margin'])
	spacing = cm_to_pixels(card_set['spacing'])
	print "Generating '" + str(card_set['name']) + "'"
	i = 0
	for s in card_set['pages']:
		if i not in page_indexes:
			print "Skipping page " + str(i)
		else:
			print "Generating page " + str(i)
			paper = create_paper(s, margin, spacing)
			if show:
				paper.show()
			if save:
				path = "output/set" + str(i) + ".png"
				print "Saving at path '" + path + "'"
				paper.save(path)
		i += 1
