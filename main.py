from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap

dpi = 300.0

def inches_to_pixels(inches):
	return int(dpi * inches)

def cm_to_inches(cm):
	return cm * 0.393700787

def cm_to_pixels(cm):
	return inches_to_pixels(cm_to_inches(cm))

def normalized_font_size(points):
	return int((points / dpi) * 300.0)

a4_size = (cm_to_pixels(21.0), cm_to_pixels(29.7))
(a4_width, a4_height) = a4_size
print "A4 pixel dimensions: " + str(a4_size)

poker_size = (cm_to_pixels(6.3), cm_to_pixels(8.8))
(poker_width, poker_height) = poker_size
print "Poker card pixel dimensions: " + str(poker_size)

margin = cm_to_pixels(1.0)
spacing = cm_to_pixels(0.1)

border_width = cm_to_pixels(0.1) # around each card

size_minus_border = (poker_width - (border_width * 2), poker_height - (border_width * 2))
(width_minus_border, height_minus_border) = size_minus_border
print "Card size without the borders: " + str(size_minus_border)

font_path = '/Library/Fonts/Times New Roman.ttf'
title_font = ImageFont.truetype(font_path, normalized_font_size(64), encoding='unic')
body_font = ImageFont.truetype(font_path, normalized_font_size(46), encoding='unic')

def draw_title(card, raw_text, pos):
	text = raw_text.decode('utf-8')
	draw = ImageDraw.Draw(card)
	draw.text(pos, text, font=title_font, fill=(0, 0, 0))

def draw_body(card, raw_text, y, card_width, chars_per_line):
	text = raw_text.decode('utf-8')
	lines = textwrap.wrap(text, width = chars_per_line)
	for line in lines:
	    line_width, line_height = body_font.getsize(line)
	    draw = ImageDraw.Draw(card)
	    draw.text(((card_width - line_width) / 2, y), line, font = body_font, fill = (0, 0, 0))
	    y += line_height

def draw_illustration(card, card_data, y, vertical_space):
	illustration = Image.open("illustrations/" + card_data['illustration'] + ".png")
	cropped = ImageOps.fit(illustration, (width_minus_border, vertical_space), Image.NEAREST, 0.01, (0.5, 0.5)) 
	card.paste(cropped, (0, y))

def create_card(card_data):
	card = Image.new("RGB", size_minus_border, "white")
	draw_illustration(card, card_data, 100, 550)
	draw_title(card, card_data['name'], (20, 15))
	draw_body(card, card_data['body'], 750, width_minus_border, 25)
	card_with_border = ImageOps.expand(card, border=border_width, fill="black")
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

card_set_1 = [
	{'illustration': "bison", 'name': "The Death", 'body': "Give each player a warm cup of coffee and a hug."}, 
	{'illustration': "citrus", 'name': "Lemonade", 'body': "If you're the oldest player at the table, eat a flower."},
	{'illustration': "citrus", 'name': "Fish", 'body': "If you're the oldest player at the table, eat a flower."},
]

create_paper(card_set_1).show()


