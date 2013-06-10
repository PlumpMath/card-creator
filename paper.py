from PIL import Image
from card import create_card
from converters import cm_to_pixels

a4_size = (cm_to_pixels(21.0), cm_to_pixels(29.7))
(a4_width, a4_height) = a4_size

def create_paper(card_set, page_index):
	margin = cm_to_pixels(card_set['margin'])
	spacing = cm_to_pixels(card_set['spacing'])
	
	(card_width_cm, card_height_cm) = card_set['card_size']
	(card_width_px, card_height_px) = (cm_to_pixels(card_width_cm), cm_to_pixels(card_height_cm))

	border_width_px = cm_to_pixels(card_set['border_width']) # around each card
	border_color = card_set['border_color']

	size_minus_border = (card_width_px - (border_width_px * 2), card_height_px - (border_width_px * 2))

	pages = card_set['pages']
	page = pages[page_index]

	cards = [create_card(data, size_minus_border, border_width_px, border_color) for data in page]
	paper = Image.new("RGB", a4_size, "white")
	card_index = 0
	for y in xrange(margin, a4_height - card_height_px, card_height_px + spacing):
		for x in xrange(margin, a4_width - card_width_px, card_width_px + spacing):
			card = cards[card_index % len(cards)]
			card_index += 1
			paper.paste(card, (x, y))
	return paper

def generate_papers_from_set(card_set, page_indexes = range(0, 99), save = False, show = True):
	print "Generating '" + str(card_set['name']) + "'"
	pages = card_set['pages']
	for i in page_indexes:
		if i >= len(pages):
			break
		else:
			print "Generating page " + str(i)
			paper = create_paper(card_set, i)
			if show:
				paper.show()
			if save:
				path = "output/" + card_set['name'] + "_page_" + str(i) + ".png"
				print "Saving '" + path + "'"
				paper.save(path)
		i += 1
