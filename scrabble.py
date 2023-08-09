# BUGS
# "masalak" verildiğinde get_combinations "alaka"yı vermiyor
# "elmas" verildiğinde duplicates bir enteresan oluyor, e harfi

# TODO: eng version
import csv

tr_letters = "abcçdefgğhıijklmnoöprsştuüvyz"
word_length = 5

def main():
	# string = get_string()
	string = "kümyabğ"
	combination_list = get_combinations(string, word_length + 1)
	word_list = get_frequency(combination_list)
	if word_list:
		print_list("Only", word_list)
	add_letters(combination_list, word_list)

# Prompt user for a string between 4 and 7 characters and consist of only letters
def get_string():
	while True:
		string = input("Letters: ")
		if 4 <= string <= 7 and string.isalpha():
			break
		return string

# Get combinations of given string, length should be equal or more than given number
def get_combinations(string, number):
	# Get all the combinations
	combinations = []
	lst = [string[i: j] for i in range(len(string)) 
		for j in range(i + 1, len(string) + 1)]
	# Add items to list only if their length equal or more than given number
	for item in lst:
		if len(item) >= (number -1):
			combinations.append(item)

	return combinations

# Check if item's in list are words, compute their frequency and return them in list
def get_frequency(lst):
	word_list = []

	# For every string in list, edit them
	for string in lst:
		edited_item = edit_string(string)

		string_ascii = edited_item[0]
		string = edited_item[1]
		letter_frequency = str(edited_item[2])

		# Open CSV file
		with open("words-tr-edited.csv", "r", encoding="utf-8") as file:

			# Create DictReader
			reader = csv.DictReader(file)

			# Iterate over CSV file
			for row in reader:
				# If letter frequency matches with any letter frequency in csv file, add it them list
				if row["letter_frequency"] == letter_frequency:
					word_list.append(row["word"])

	return word_list

# Calculates ascii and frequency of letters
def edit_string(string):
	total = 0
	dct = {}
	for c in string:
		# Compute ascii value of every char
		total += ord(c)
		# Count every char in a string, save them in a dictionary
		if c in dct.keys():
			dct[c] += 1
		else:
			dct[c] = 1
	# Sort dictionary of chars alphabetically
	sorted_dct = {key: value for key, value in sorted(dct.items())}
	# Add all the output to single lists
	edited_item = [total, string, sorted_dct]

	return edited_item

# Print the list according to a format
def print_list(explanation, lst):
	# Print explanation
	print(explanation, end=": ")
	# Print every word in list, except the last word
	for word in lst[:-1]:
		print(word, end=", ")
	# Print last word if there is any item in list
	if lst:
		print(lst[len(lst) -1])

# Calculate and print all possible words, if every letter of alphabet added to world list one by one
def add_letters(lst, duplicates):
	# For every letter of Turkish alphabet
	for c in tr_letters:
		appended_list = []
		# Add letter to every item at world list
		for item in lst:
			item = item + c
			appended_list.append(item)
			# Check if new items exist in Turkish dictionary and get their letter frequency
			word_list = get_frequency(appended_list)

		# Remove duplicates
		for element in word_list:
			if element in duplicates:
				word_list.remove(element)

		# If it can contruct a word when letter added to item
		if word_list:
			# Print them according the format
			print_list(c.upper(), word_list)

main()