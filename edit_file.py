# Edits a file and save as CSV format

import csv

words = []

with open("words-tr.txt", "r", encoding="utf-8") as file:
	for line in file:
		line = line.rstrip()

		# Lowercase, only letters, one-word
		if not line.islower() or not line.isalpha() or ' ' in line:
			continue
		if len(line) <= 4 or len(line) >= 9:
			continue
		# Handle special letters
		line = line.replace("â", "a")
		line = line.replace("î", "i")
		
		total = 0
		dct = {}
		for c in line:
			line = line.rstrip()
			# Compute ascii value of every char
			total += ord(c)
			# Count every char in a word, save them in a dictionary
			if c in dct.keys():
				dct[c] += 1
			else:
				dct[c] = 1

		# Sort dictionary of chars alphabetically
		sorted_dct = {key: value for key, value in sorted(dct.items())}
		# Add all the output to single lists
		temp = [total, line, sorted_dct]
		# Add single lists to a main list while handling duplicates
		if temp not in words:
			words.append(temp)
		# Sort them based on ascii value
		words.sort()

# Open CSV file
with open("words-tr-edited.csv", "a", newline="", encoding="utf-8") as edited_file:
	# Write to file
	writer = csv.writer(edited_file)
	writer.writerow(["ascii", "word", "letter_frequency"])
	writer.writerows(words)