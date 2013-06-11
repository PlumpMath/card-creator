def print_stats(card_set):
	total_count = 0
	for card in card_set['cards']:
		print str(card['count']) + " " + str(card['name']) + " (speed: " + str(card['speed']) + ")"
		total_count += card['count']
	print "Total count: " + str(total_count)
	print "Nr of card types: " + str(len(card_set['cards']))