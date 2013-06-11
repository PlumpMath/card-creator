def print_stats(card_set):
	total_count = 0
	i = 0
	for card in card_set['cards']:
		print str(i) + " " + str(card['name']) + " (speed: " + str(card['speed']) + ") count: " + str(card['count'])
		total_count += card['count']
		i += 1
	print "Total count: " + str(total_count)
	print "Nr of card types: " + str(len(card_set['cards']))