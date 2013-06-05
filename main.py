from PIL import Image, ImageFont, ImageDraw, ImageOps
from textwrap import TextWrapper

dpi = 300.0

def inches_to_pixels(inches):
	return int(dpi * inches)

def cm_to_inches(cm):
	return cm * 0.393700787

def cm_to_pixels(cm):
	return inches_to_pixels(cm_to_inches(cm))

def normalized_font_size(points):
	return int((points * dpi) / 300.0)

a4_size = (cm_to_pixels(21.0), cm_to_pixels(29.7))
(a4_width, a4_height) = a4_size
print "A4 pixel dimensions: " + str(a4_size)

poker_size = (cm_to_pixels(6.3), cm_to_pixels(8.8))
(poker_width, poker_height) = poker_size
print "Poker card pixel dimensions: " + str(poker_size)

margin = cm_to_pixels(1.0)
spacing = cm_to_pixels(0.02)

border_width = cm_to_pixels(0.25) # around each card
border_color = (150, 150, 150)

size_minus_border = (poker_width - (border_width * 2), poker_height - (border_width * 2))
(width_minus_border, height_minus_border) = size_minus_border
print "Card size without the borders: " + str(size_minus_border)

font_path = '/Library/Fonts/Georgia.ttf'
title_font = ImageFont.truetype(font_path, normalized_font_size(64), encoding='unic')
body_font = ImageFont.truetype(font_path, normalized_font_size(46), encoding='unic')

hexagon = Image.open("illustrations/hexagon.png")

footer_color = (190, 200, 200)

def draw_title(card, raw_text, pos):
	text = raw_text.decode('utf-8')
	draw = ImageDraw.Draw(card)
	draw.text(pos, text, font=title_font, fill=(0, 0, 0))

def draw_corner_nr(card, raw_text, pos):
	text = raw_text.decode('utf-8')
	draw = ImageDraw.Draw(card)
	draw.text(pos, text, font=title_font, fill=(0, 0, 0))

def draw_body(card, raw_text, center_y, card_width, chars_per_line):
	text = raw_text.decode('utf-8')
	wrapper = TextWrapper()
	wrapper.width = chars_per_line
	wrapper.replace_whitespace = True
	wrapper.drop_whitespace = False
	lines = wrapper.wrap(text)
	line_width, line_height = body_font.getsize(lines[0])
	y = center_y - (line_height * (float(len(lines)) / 2.0))
	for line in lines:
		line_width, line_height = body_font.getsize(line)
		draw = ImageDraw.Draw(card)
		draw.text(((card_width - line_width) / 2, y), line, font = body_font, fill = (0, 0, 0))
		y += line_height

def draw_illustration(card, illustration_name, y, vertical_space):
	illustration = Image.open("illustrations/" + illustration_name + ".png")
	cropped = ImageOps.fit(illustration, (width_minus_border, vertical_space), Image.ANTIALIAS, 0.01, (0.5, 0.5)) 
	card.paste(cropped, (0, y))

def draw_hexagon(card):
	card.paste(hexagon, (width_minus_border - 110, height_minus_border - 110))

def draw_footer(card, height):
	footer = Image.new("RGB", (width_minus_border, height), footer_color)
	card.paste(footer, (0, height_minus_border - height))

def create_card(card_data):
	card = Image.new("RGB", size_minus_border, "white")
	draw_illustration(card, card_data['illustration'], 100, 500)
	draw_title(card, card_data['name'], (20, 15))
	draw_body(card, card_data['body'], 730, width_minus_border, card_data['body_width'])
	#draw_hexagon(card)
	draw_footer(card, 100)
	draw_corner_nr(card, card_data['corner_nr'], (width_minus_border - 65, height_minus_border - 90))
	card_with_border = ImageOps.expand(card, border=border_width, fill=border_color)
	return card_with_border

def create_paper(cards_data_set):
	cards = [create_card(data) for data in cards_data_set]
	paper = Image.new("RGB", a4_size, "white")
	card_index = 0
	for y in xrange(margin, a4_height - poker_height, poker_height + spacing):
		for x in xrange(margin, a4_width - poker_width, poker_width + spacing):
			card = cards[card_index % len(cards)]
			card_index += 1
			paper.paste(card, (x, y))
	return paper

def generate_papers_from_sets(sets):
	i = 1
	for s in sets:
		print "Generating set " + str(i)
		paper = create_paper(s)
		paper.save("output/set" + str(i) + ".png")
		i += 1

card_set_0 = [
	{'name': "", 'illustration': "", 'body': "Gain 3 points.", 'body_width': 25, 'corner_nr': "0"},
	{'name': "", 'illustration': "", 'body': "Gain 3 points.", 'body_width': 25, 'corner_nr': "0"},
	{'name': "", 'illustration': "", 'body': "Gain 3 points.", 'body_width': 25, 'corner_nr': "0"},
]

card_set_1 = [
	{'illustration': "big_time", 'body_width': 25, 'corner_nr': "0", 'name': "Big Time", 'body': "Gain 3 points."}, 
	{'illustration': "destruction", 'body_width': 25, 'corner_nr': "0", 'name': "Destruction", 'body': "Trash a card."},
	{'illustration': "ambush", 'body_width': 23, 'corner_nr': "2", 'name': "Ambush!", 'body': "Put a card from your hand into play face up."},
]

card_set_2 = [
	{'name': "Hecatomb", 'illustration': "hecatomb", 'body': "Trash any number of cards you control to gain that many points.", 'body_width': 24, 'corner_nr': "2"},
	{'name': "Simplicity", 'illustration': "simplicity", 'body': "Gain 1 point.", 'body_width': 25, 'corner_nr': "4"},
	{'name': "Catch Up", 'illustration': "catch_up", 'body': "The player with the least points (if any) gains 5 points.", 'body_width': 24, 'corner_nr': "2"},
]

card_set_3 = [
	{'name': "Time Machine", 'illustration': "time_machine", 'body': "Lose 5 points. You can use two additional cards this turn.", 'body_width': 25, 'corner_nr': "1"},
	{'name': "Together We Fall", 'illustration': "together_we_fall", 'body': "Both players lose 7 points.", 'body_width': 35, 'corner_nr': "1"},
	{'name': "Scoundrels", 'illustration': "scoundrels", 'body': "Both players may play up to two cheats from their hands.", 'body_width': 23, 'corner_nr': "3"},
]

card_set_4 = [
	{'name': "Rescue Mission", 'illustration': "rescue_mission", 'body': "Lose 2 points. Pick a trashed card and put it into play (unused).", 'body_width': 25, 'corner_nr': "1"},
	{'name': "Working 9 to 5", 'illustration': "working_9_to_5", 'body': "Gain 2 points.", 'body_width': 25, 'corner_nr': "2"},
	{'name': "Late Bloomer", 'illustration': "late_bloomer", 'body': "Gain 1 point. Turn a card into a cheat.", 'body_width': 25, 'corner_nr': "1"},
]

card_set_5 = [
	{'name': "Metamorphic", 'illustration': "metamorphic", 'body': "Gain 1 point. Flip up a cheat.", 'body_width': 17, 'corner_nr': "2"},
	{'name': "Duplicate", 'illustration': "duplicate", 'body': "Both players double their points.", 'body_width': 20, 'corner_nr': "2"},
	{'name': "The Sublime", 'illustration': "the_sublime", 'body': "Trash this card. Make two used cards usable again.", 'body_width': 20, 'corner_nr': "1"},
]

sets = [card_set_1, card_set_2, card_set_3, card_set_4, card_set_5]
generate_papers_from_sets(sets)

#create_paper(card_set_5).show()
