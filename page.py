from PIL import Image
from card import create_card
from converters import cm_to_pixels

a4_size = (cm_to_pixels(21.0), cm_to_pixels(29.7))
(a4_width, a4_height) = a4_size

def create_page(card_set, card_indexes):
	margin = cm_to_pixels(card_set['margin'])
	spacing = cm_to_pixels(card_set['spacing'])
	
	(card_width_cm, card_height_cm) = card_set['card_size']
	(card_width_px, card_height_px) = (cm_to_pixels(card_width_cm), cm_to_pixels(card_height_cm))

	border_width_px = cm_to_pixels(card_set['border_width']) # around each card
	border_color = card_set['border_color']

	outline_width = card_set['outline_width']
	outline_color = card_set['outline_color']

	size_minus_border = (card_width_px - (border_width_px * 2), card_height_px - (border_width_px * 2))

	card_datas = card_set['cards']
	selected_card_datas = []

	i = 0
	for d in card_datas:
		if i in card_indexes:
			selected_card_datas.append(d)
		i += 1

	cards = []
	for data in selected_card_datas:
		card = create_card(data, size_minus_border, border_width_px, border_color, outline_width, outline_color)
		for x in range(data['count']):
			cards.append(card)
	
	page = Image.new("RGB", a4_size, "white")
	card_index = 0
	for y in xrange(margin, a4_height - card_height_px, card_height_px + spacing):
		for x in xrange(margin, a4_width - card_width_px, card_width_px + spacing):
			if card_index >= len(cards):
				break
			card = cards[card_index]
			card_index += 1
			page.paste(card, (x, y))
	return page

def complete_page(card_set, card_indexes, save, show, page_counter):
	print "Creating page nr " + str(page_counter) + " with cards: " + str(card_indexes)
	page = create_page(card_set, card_indexes)
	if show:
		page.show()
	if save:
		path = "output/" + card_set['name'] + "_page_" + str(page_counter) + ".png"
		print "Saving '" + path + "'"
		page.save(path)

def generate_pages_from_set(card_set_without_settings, settings, card_indexes = range(0, 999), save = False, show = True):
	print "Generating '" + str(card_set_without_settings['name']) + "'"
	card_set = dict(card_set_without_settings.items() + settings.items())
	cards = card_set['cards']
	cards_per_page = card_set['cards_per_page']
	cards_on_current_page = 0
	indexes_on_current_page = []
	page_counter = 0
	total_card_count = 0
	for i in card_indexes:
		if i >= len(cards):
			break
		else:
			card_to_add = cards[i]
			count = card_to_add['count']
			total_card_count += count
			if (cards_on_current_page + count) <= cards_per_page:
				indexes_on_current_page.append(i)
				cards_on_current_page += count
			else:
				complete_page(card_set, indexes_on_current_page, save, show, page_counter)
				indexes_on_current_page = [i] # new array
				cards_on_current_page = count
				page_counter += 1
	complete_page(card_set, indexes_on_current_page, save, show, page_counter)
	print "Total card count: " + str(total_card_count)

def generate_separate_card_images_from_set(card_set_without_settings, settings, card_indexes = range(0, 999), save = False, show = True):
	print "Generating separate cards for set '" + str(card_set_without_settings['name']) + "'"
	card_set = dict(card_set_without_settings.items() + settings.items())
	cards = card_set['cards']
	total_card_count = 0
	card_datas = card_set['cards']

	margin = cm_to_pixels(card_set['margin'])
	spacing = cm_to_pixels(card_set['spacing'])
	
	(card_width_cm, card_height_cm) = card_set['card_size']
	(card_width_px, card_height_px) = (cm_to_pixels(card_width_cm), cm_to_pixels(card_height_cm))

	border_width_px = cm_to_pixels(card_set['border_width']) # around each card
	border_color = card_set['border_color']

	outline_width = card_set['outline_width']
	outline_color = card_set['outline_color']

	size_minus_border = (card_width_px - (border_width_px * 2), card_height_px - (border_width_px * 2))

	card_datas = card_set['cards']

	cards = []
	for i in card_indexes:
		data = card_datas[i]
		card = create_card(data, size_minus_border, border_width_px, border_color, outline_width, outline_color)
		if show:
			card.show()
		if save:
			path = "output/" + card_set['name'] + "_card_" + str(i) + "_" + data['name'].replace(" ", "_") + ".png"
			print "Saving '" + path + "'"
			card.save(path)
		
	print "Total card count: " + str(total_card_count)

