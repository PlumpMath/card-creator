from PIL import Image, ImageFont, ImageDraw, ImageOps
from textwrap import TextWrapper
from converters import cm_to_pixels, normalized_font_size

font_path = '/Library/Fonts/Georgia.ttf'
title_font = ImageFont.truetype(font_path, normalized_font_size(64), encoding='unic')
body_font = ImageFont.truetype(font_path, normalized_font_size(46), encoding='unic')

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

def draw_illustration(card, illustration_name, y, vertical_space, width_minus_border):
	illustration = Image.open("illustrations/" + illustration_name + ".png")
	cropped = ImageOps.fit(illustration, (width_minus_border, vertical_space), Image.ANTIALIAS, 0.01, (0.5, 0.5)) 
	card.paste(cropped, (0, y))

def draw_footer(card, height, width_minus_border, height_minus_border):
	footer = Image.new("RGB", (width_minus_border, height), footer_color)
	card.paste(footer, (0, height_minus_border - height))

def create_card(card_data, size_minus_border, border_width, border_color):
	(width_minus_border, height_minus_border) = size_minus_border
	card = Image.new("RGB", size_minus_border, "white")
	draw_illustration(card, card_data['pic'], 100, 500, width_minus_border)
	draw_title(card, card_data['name'], (20, 15))
	draw_body(card, card_data['body'], 730, width_minus_border, card_data['body_width'])
	draw_footer(card, 100, width_minus_border, height_minus_border)
	draw_corner_nr(card, card_data['speed'], (width_minus_border - 65, height_minus_border - 90))
	card_with_border = ImageOps.expand(card, border=border_width, fill=border_color)
	return card_with_border


