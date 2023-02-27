"""
Author: 			Ian McConachie
Professor: 			Humphrey Shi, Steven Walton
Class: 				CS 472
Date Created: 		02/26/2023
Last Date Modified: 02/26/2023

Description:

This script takes datasets created by scraping different websites and combines 
them and formats them as a single data file with the proper formatting.
"""

## Import Statements

import re

## Helper Functions

def unique_filter(dictionary, name):
	"""

	"""
	ret = False
	if (dictionary.get(name) == None):
		dictionary[name] = 1
		ret = True
	
	return ret


def price_filter(price, denom):
	"""
	"""
	ret = False
	match_1 = re.match(r"gp|sp|cp", denom)
	match_2 = re.match(r"\d+",price)
	if (match_1 and match_2):
		ret = True

	return ret


## Modular Functions

def category_simplify(category):
	"""

	"""
	ret = category
	gemstone_cats = ['Gemstones']
	food_and_drink_cats = ['Drinks', 'Menu - Breakfast Options', 
		'Menu - Lunch Options', 'Menu - Dinner Options']
	potion_cats = ['Potions', 'Potion', 'Potions & Oils']
	wonder_cats = ['Wondrous Items: Feet', 'Wondrous Items', 'Wondrous Items: Neck',
		'Wondrous Items: Waist', 'Wondrous Items: Eyes', 'Wondrous Items: Arms & Wrists',
		'Woundrous Items', 'Wondrous Items: Head', 'Wondrous Items: Shoulders', 
		'Wondrous Items: Hands', 'Wondrous Items: Body']
	s_exceptions = ['Miscellaneous', 'Arcane Focus', 'Druidic Focus']

	if (category in gemstone_cats):
		ret = 'Gemstone'
	elif (category in food_and_drink_cats):
		ret = 'Food, Drink & Lodging'
	elif (category in potion_cats):
		ret = 'Potion or Oil'
	elif (category in wonder_cats):
		ret = 'Wondrous Item'

	elif ((category[-1] == 's') and (category not in s_exceptions)):
		ret = category[:-1]

	return ret


def write_data(header, item_list, write_file):
	"""
	:inputs: 	header		[a str]
				item_list   [a list of strings]
			 	write_file  [a str]
	:returns:	None

	This function takes in a list of strings and a file to write to and writes
	the strings to the file, separating each with a new line. Additionally it
	takes a header string which will be written at the top of the txt file This
	function returns nothing, but has the side effect of writing to write_file.
	"""
	item_list.insert(0,header)
	with open(write_file, 'w') as file:
		file.write('\n'.join(item_list))


## Main Function

def main():
	"""
	"""
	i = 0
	existing_items = {}
	categories = []
	data_files = ['db_merchant_prices.txt', 'tg_merchant_prices.txt',
				  'mi_merchant_prices.txt']
	write_file = 'all_merchant_prices.txt'
	entry_list = []

	for file in data_files:
		with open(file, 'r') as f:
			lines = f.readlines()
			for line in lines:
				item_list = line.split('|')
				name = item_list[1]
				category = item_list[0]

				# Separating price integer and type of currency
				price = item_list[2].split(" ")
				denom = price[1].strip()
				price = price[0].replace(",","")

				# Check to see if we already have recorded this item
				if not (unique_filter(existing_items, name)):
					continue

				# Filtering bad data points
				if not (price_filter(price, denom)):
					#print(name, price, denom)
					continue

				# Handling discrete category
				category = category_simplify(category)
				if (category not in categories):
					categories.append(category)

				# Making entry_list
				entry = name + '|' + category + '|' + price + '|' + denom
				entry_list.append(entry)

	# Making the header
	cat_header = '|'.join(categories) + '\n'

	# Writing to the write file
	write_data(cat_header, entry_list, write_file)




## Executing main function

if __name__ == "__main__":
	main()