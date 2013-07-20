from PIL import Image, ImageFont, ImageDraw, ImageOps
from textwrap import TextWrapper
from converters import cm_to_pixels, normalized_font_size

font_path = '/Library/Fonts/Arial.ttf'
title_font = ImageFont.truetype(font_path, normalized_font_size(80), encoding='unic')
body_font = ImageFont.truetype(font_path, normalized_font_size(46), encoding='unic')

footer_color = (190, 200, 200)

def draw_text_centered(card, text, y, font, card_width):
	line_width, line_height = font.getsize(text)
	x = (card_width / 2) - (line_width / 2)
	draw = ImageDraw.Draw(card)
	draw.text((x, y), text, font=title_font, fill=(0, 0, 0))

def draw_title(card, raw_text, pos, card_width):
	(x, y) = pos
	text = raw_text.decode('utf-8')
	draw_text_centered(card, text, y, title_font, card_width)

def draw_pip(card, text, pos, color):
	margin = 10
	margin_x2 = margin * 2
	(body_w, body_h) = body_font.getsize(text)
	pip_size = (body_w + margin_x2, body_h + margin_x2)
	pip_bg = Image.new("RGB", pip_size, color)
	card.paste(pip_bg, pos)
	draw = ImageDraw.Draw(card)
	(x, y) = pos
	(text_x, text_y) = (x + margin, y + margin)
	draw.text((text_x, text_y), text, font=body_font, fill=(0, 0, 0))

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

def draw_illustration(card, illustration_name, y, vertical_space, width_minus_border, outline_width, outline_color):
	image_spacing = 20
	image_spacing_x2 = image_spacing * 2
	illustration = Image.open("illustrations/" + illustration_name + ".png")
	cropped = ImageOps.fit(illustration, (width_minus_border - (outline_width * 2) - image_spacing_x2, vertical_space - (outline_width * 2)), Image.ANTIALIAS, 0.01, (0.5, 0.5)) 
	cropped_with_border = ImageOps.expand(cropped, border=outline_width, fill=outline_color)
	card.paste(cropped_with_border, (0 + image_spacing, y))

def draw_footer(card, height, width_minus_border, height_minus_border):
	footer = Image.new("RGB", (width_minus_border, height), footer_color)
	card.paste(footer, (0, height_minus_border - height))

def draw_bg(card, w, h):
	bg = Image.open("illustrations/bg1.png")
	cropped = ImageOps.fit(bg, (w, h), Image.ANTIALIAS, 0.01, (0.5, 0.5)) 
	card.paste(cropped, (0, 0))

def get_rgb(color_as_text):
	if color_as_text == "red":
		return (255, 100, 100)
	elif color_as_text == "blue":
		return (100, 150, 255)
	else:
		return (220, 220, 220)

def to_dir(direction_as_text):
	if direction_as_text == "right":
		return 0.0
	elif direction_as_text == "down":
		return 270.0
	elif direction_as_text == "left":
		return 180.0
	elif direction_as_text == "up":
		return 90.0
	else:
		raise "Can't match " + direction_as_text

def if_arrow_pos(direction_as_text, arrow_size, card_width, card_height):
	(arrow_image_width, arrow_image_height) = arrow_size
	margin = 5
	if direction_as_text == "right":
		return (card_width - arrow_image_width, (card_height / 2) - (arrow_image_height / 2))
	elif direction_as_text == "down":
		return ((card_width / 2) - (arrow_image_width / 2), card_height - (arrow_image_height + margin))
	elif direction_as_text == "left":
		return (margin, card_height / 2 - arrow_image_height / 2)
	elif direction_as_text == "up":
		return (card_width / 2 - arrow_image_width / 2, margin)
	else:
		raise "Can't match " + direction_as_text

def create_card(card_data, size_minus_border, border_width, border_color, outline_width, outline_color):
	(width_minus_border, height_minus_border) = size_minus_border
	card = Image.new("RGB", size_minus_border, "white")
	card_color = get_rgb(card_data['color'])

	#print "width_minus_border: " + str(width_minus_border)
	#print "height_minus_border: " + str(height_minus_border)

	if(card_data['template'] == "if"):
		true_dir = card_data['true']
		false_dir = card_data['false']
		true_pic = Image.open("illustrations/True.png")
		false_pic = Image.open("illustrations/False.png")
		rotated_true_pic = true_pic.rotate(to_dir(true_dir))
		rotated_false_pic = false_pic.rotate(to_dir(false_dir))
		#print true_dir + " -> " + str(if_arrow_pos(true_dir, true_pic.size, width_minus_border, height_minus_border))
		card.paste(rotated_true_pic, if_arrow_pos(true_dir, rotated_true_pic.size, width_minus_border, height_minus_border))
		card.paste(rotated_false_pic, if_arrow_pos(false_dir, rotated_false_pic.size, width_minus_border, height_minus_border))

	if(card_data['template'] == "dir"):
		true_pic = Image.open("illustrations/Arrow.png")
		rotated_true_pic = true_pic.rotate(to_dir(card_data['direction']))
		(w, h) = rotated_true_pic.size
		card.paste(rotated_true_pic, (width_minus_border / 2 - w / 2, height_minus_border / 2 - h / 2))

	draw_pip(card, card_data['template'], (20, 20), card_color)
	#draw_bg(card, width_minus_border, height_minus_border)
	#draw_illustration(card, card_data['pic'], 100, 500, width_minus_border, outline_width, outline_color)
	y = 170

	if card_data['template'] == "if":
		y = 230

	draw_title(card, card_data['body'], (20, y), width_minus_border)
	#draw_body(card, card_data['body'], 730, width_minus_border, card_data['body_width'])

	card_with_border = ImageOps.expand(card, border=border_width, fill=border_color)
	return card_with_border


