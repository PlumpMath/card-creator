
main_set = {
	'name': "MainSet",
	'cards': [
			# cards 0 - 4
			{'name': "Simplicity", 			'pic': "simplicity", 		'body': "Gain 1 point.", 'body_width': 25, 'speed': "4", 'count': 3},
			{'name': "Working 9 to 5", 		'pic': "working_9_to_5", 	'body': "Gain 2 points.", 'body_width': 25, 'speed': "2", 'count': 3},
			{'name': "Big Time", 			'pic': "big_time",			'body': "Gain 3 points.", 'body_width': 25, 'speed': "0", 'count': 3},
			{'name': "Hecatomb", 			'pic': "hecatomb", 			'body': "Trash any number of cards you control to gain that many points.", 'body_width': 24, 'speed': "0", 'count': 1},
			{'name': "Catch Up", 			'pic': "catch_up", 			'body': "The player with the least points (if any) gains 4 points.", 'body_width': 24, 'speed': "1", 'count': 1},
			# cards 5 - 9
			{'name': "Together We Fall", 	'pic': "together_we_fall",	'body': "Both players lose 7 points.", 'body_width': 35, 'speed': "2", 'count': 0},
			{'name': "Ambush!", 			'pic': "ambush", 			'body': "Put a card from your hand into play face up.", 'body_width': 23, 'speed': "1", 'count': 2},
			{'name': "Duplicate", 			'pic': "duplicate",			'body': "Both players double their points.", 'body_width': 20, 'speed': "2", 'count': 1},
			{'name': "Pain",				'pic': "jellyfish", 		'body': "Lose 2 points. Make a card used or unused.", 'body_width': 24, 'speed': "2", 'count': 1},
			{'name': "Rescue Mission", 		'pic': "rescue_mission", 	'body': "Lose 3 points. Pick a trashed card and put it into play (unused).", 'body_width': 25, 'speed': "1", 'count': 1},
			# cards 10 - 14
			{'name': "Time Machine", 		'pic': "time_machine", 		'body': "Lose 5 points. You can use two additional cards this turn.", 'body_width': 25, 'speed': "1", 'count': 0},
			{'name': "Scoundrels", 			'pic': "scoundrels", 		'body': "Both players may play up to two cheats from their hands.", 'body_width': 23, 'speed': "3", 'count': 1},
			{'name': "Late Bloomer", 		'pic': "late_bloomer",		'body': "Gain 1 point. Turn a card into a cheat.", 'body_width': 25, 'speed': "1", 'count': 2},
			{'name': "Metamorphic", 		'pic': "metamorphic",		'body': "Gain 1 point. Flip up a cheat.", 'body_width': 17, 'speed': "2", 'count': 1},
			{'name': "The Sublime", 		'pic': "the_sublime", 		'body': "Lose 2 points. Trash this card. Make two used cards usable again.", 'body_width': 17, 'speed': "0", 'count': 1},
			# cards 15 - 19
			{'name': "Destiny", 			'pic': "destiny", 			'body': "Put the top card of the deck into play.", 'body_width': 20, 'speed': "3", 'count': 2},
			{'name': "Philantropist", 		'pic': "philantropist", 	'body': "Select one of your cards (not this one) and give it to your opponent. Make it usable.", 'body_width': 27, 'speed': "5", 'count': 1},
			{'name': "Anarchy", 			'pic': "anarchy", 			'body': "Each player gains 1 point for each cheat they have in play. Trash all cheats.", 'body_width': 28, 'speed': "2", 'count': 1},
			{'name': "Ancient Riches", 		'pic': "pyramid", 			'body': "Lose 5 points. Gain 1 point for each card in the trash pile.", 'body_width': 23, 'speed': "0", 'count': 1},
			{'name': "Peddler", 			'pic': "peddler", 			'body': "Trash an unused card you control. Gain points equal to that card's speed.", 'body_width': 30, 'speed': "2", 'count': 1},
			# cards 20 - 24
			{'name': "Silence", 			'pic': "silence", 			'body': "Until the end of your next turn, players cannot gain points.", 'body_width': 22, 'speed': "3", 'count': 0},
			{'name': "Purge", 				'pic': "purge", 			'body': "Gain 1 point. Trash all used cards.", 'body_width': 22, 'speed': "1", 'count': 1},
			{'name': "Late to the Party", 	'pic': "neon", 				'body': "The player with the highest total speed (if any) gains 4 points.", 'body_width': 25, 'speed': "0", 'count': 1},
			{'name': "Faster than the Eye", 'pic': "hands", 			'body': "Turn any number of cards you control into cheats.", 'body_width': 25, 'speed': "3", 'count': 1},
			{'name': "Martyr", 				'pic': "praying", 			'body': "Lose 3 points.", 'body_width': 25, 'speed': "5", 'count': 1},
			# cards 25 - 29
			{'name': "Asceticism",			'pic': "elephant", 			'body': "Gain 1 point. Discard your hand.", 'body_width': 20, 'speed': "3", 'count': 1},
			{'name': "Observing the Infinite",'pic': "wisdom", 			'body': "Lose 3 points. Look at the top 5 cards of the deck and put one of those into play. Discard the rest.", 'body_width': 28, 'speed': "1", 'count': 1},
			{'name': "Fresh Air",	 		'pic': "sunrise", 			'body': "Shuffle the discard pile into the deck. Draw three cards.", 'body_width': 22, 'speed': "3", 'count': 1},
			{'name': "Careful Heist",	 	'pic': "sneakdoor", 		'body': "Take control of a card (this does not make a used card unused).", 'body_width': 25, 'speed': "-3", 'count': 0},
			{'name': "Convincing Tounge",	'pic': "snake", 			'body': "Select which card the opponent must use on her next turn.", 'body_width': 23, 'speed': "2", 'count': 1},
			# cards 30 - 34
			{'name': "Scrap Canon",			'pic': "fire", 				'body': "Trash another card you control, if possible. Trash a card.", 'body_width': 22, 'speed': "2", 'count': 0},
			{'name': "Angry Hermit",		'pic': "horse", 			'body': "Gain 1 point. If this is your only card in play, put two cards from the trash into play.", 'body_width': 26, 'speed': "2", 'count': 0},
			{'name': "Paris",				'pic': "paris", 			'body': "Make all your cards used. Put a card from your hand into play face up and use it immediately.", 'body_width': 26, 'speed': "2", 'count': 1},
			{'name': "Slow Magic",			'pic': "slow_magic",		'body': "You can use an additional card. Make that card unused at the end of this turn.", 'body_width': 28, 'speed': "3", 'count': 1},
			{'name': "Poke",				'pic': "poke",	 			'body': "Perform the effect of an unused card that your opponent controlls.", 'body_width': 22, 'speed': "0", 'count': 1},
			# cards 35 - 39
			{'name': "Beasts",				'pic': "bison", 			'body': "Destroy the card with the highest speed. You choose which one in the case of a tie.", 'body_width': 24, 'speed': "2", 'count': 0},
			{'name': "Overwhelming Desire",	'pic': "desire", 			'body': "Lose 2 points for each unused card you have in play. Play up to two face up cards.", 'body_width': 25, 'speed': "2", 'count': 1},
			{'name': "Excursion",			'pic': "bicycle", 			'body': "Gain 4 points. Your opponent may play a face up card.", 'body_width': 19, 'speed': "3", 'count': 1},
			{'name': "Art", 				'pic': "bike2", 			'body': "Lose 1 point. You may make this card unused.", 'body_width': 25, 'speed': "1", 'count': 0},
			{'name': "Permutations",		'pic': "creatures", 		'body': "Play up to three face up cards. Make them used.", 'body_width': 25, 'speed': "3", 'count': 1},
			# cards 40 - 44
			{'name': "Bad Omen",			'pic': "bird", 		'body': "Lose all your points. Make all your cheats unused.", 'body_width': 25, 'speed': "0", 'count': 0},

			#{'name': "",	 				'pic': "sunrise", 			'body': "", 'body_width': 25, 'speed': "3", 'count': 2},
	],
}


banished = {
	'name': "Banished",
	'cards': [
			{'name': "Destruction", 		'pic': "destruction", 		'body': "Trash a card.", 'body_width': 25, 'speed': "-1", 'count': 2},
	]
}
