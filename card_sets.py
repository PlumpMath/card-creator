
main_set = {
	'name': "MainSet",
	'cards': [
			# Pop
			{'name': "Pop", 'body': "Pop!", 'count': 4, 'template': "pop", 'color': "white"},
			{'name': "Pop 2", 'body': "Pop twice!", 'count': 1, 'template': "pop", 'color': "white"},
			
			# Push
			{'name': "Push red", 'body': "Push red", 'count': 3, 'template': "push", 'color': "red"},
			{'name': "Push blue", 'body': "Push blue", 'count': 3, 'template': "push", 'color': "blue"},
			{'name': "Push back red", 'body': "Push_back red", 'count': 1, 'template': "push", 'color': "red"},
			{'name': "Push back blue", 'body': "Push_back blue", 'count': 1, 'template': "push", 'color': "blue"},

			# If
			{'name': "If blue", 'body': "Red?", 'count': 1, 'template': "if", 'color': "red", 'true': "right", 'false': "left"},
			{'name': "If red", 'body': "Blue?", 'count': 1, 'template': "if", 'color': "blue", 'true': "right", 'false': "up"},

			{'name': "If blue", 'body': "Red?", 'count': 1, 'template': "if", 'color': "red", 'true': "up", 'false': "down"},
			{'name': "If red", 'body': "Blue?", 'count': 1, 'template': "if", 'color': "blue", 'true': "up", 'false': "right"},

			{'name': "If blue", 'body': "Red?", 'count': 1, 'template': "if", 'color': "red", 'true': "left", 'false': "up"},
			{'name': "If red", 'body': "Blue?", 'count': 1, 'template': "if", 'color': "blue", 'true': "left", 'false': "down"},

			{'name': "If blue", 'body': "Red?", 'count': 1, 'template': "if", 'color': "red", 'true': "down", 'false': "left"},
			{'name': "If red", 'body': "Blue?", 'count': 1, 'template': "if", 'color': "blue", 'true': "down", 'false': "right"},

			# Labels
			{'name': "10", 'body': "10:", 'count': 1, 'template': "label", 'color': "white"},
			{'name': "20", 'body': "20:", 'count': 1, 'template': "label", 'color': "white"},
			{'name': "30", 'body': "30:", 'count': 1, 'template': "label", 'color': "white"},
			{'name': "40", 'body': "40:", 'count': 1, 'template': "label", 'color': "white"},
			{'name': "50", 'body': "50:", 'count': 1, 'template': "label", 'color': "white"},
			
			# Goto
			{'name': "Goto 10", 'body': "GOTO 10", 'count': 1, 'template': "goto", 'color': "white"},
			{'name': "Goto 20", 'body': "GOTO 20", 'count': 1, 'template': "goto", 'color': "white"},
			{'name': "Goto 30", 'body': "GOTO 30", 'count': 1, 'template': "goto", 'color': "white"},
			{'name': "Goto 40", 'body': "GOTO 40", 'count': 1, 'template': "goto", 'color': "white"},
			{'name': "Goto 50", 'body': "GOTO 50", 'count': 1, 'template': "goto", 'color': "white"},
			
			# Shift
			{'name': "Shift 1", 'body': "Shift 1", 'count': 1, 'template': "shift", 'color': "white"},
			{'name': "Shift 2", 'body': "Shift 2", 'count': 1, 'template': "shift", 'color': "white"},
			{'name': "Shift 3", 'body': "Shift 3", 'count': 1, 'template': "shift", 'color': "white"},
			
			# Set dir
			{'name': "Set dir", 'body': "Set direction", 'count': 1, 'template': "dir", 'direction': "up", 'color': "white"},
			{'name': "Set dir", 'body': "Set direction", 'count': 1, 'template': "dir", 'direction': "down", 'color': "white"},
			{'name': "Set dir", 'body': "Set direction", 'count': 1, 'template': "dir", 'direction': "left", 'color': "white"},
			{'name': "Set dir", 'body': "Set direction", 'count': 1, 'template': "dir", 'direction': "right", 'color': "white"},
	],
}

