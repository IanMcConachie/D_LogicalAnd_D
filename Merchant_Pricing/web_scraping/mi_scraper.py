"""
Author: 			Ian McConachie
Professor: 			Humphrey Shi, Steven Walton
Class: 				CS 472
Date Created: 		02/22/2023
Last Date Modified: 02/22/2023

Description:

This python script scrapes data from csv files--particularly the discerning
merchant's price guide put out by Dave Eisinger and Fey Rune Labs. It
writes the category of an item, the item's name, and the price of the item
(in gold, silver, or copper pieces) to a text file separating each field with a
"|" character. Each entry is separated by a newline.
"""

## Import Statements
import csv


## Modular Functions

def collect_data(file_contents):
	"""
	:inputs:		file_contents [a csv object defined in csv library]
	:returns:		item_list [a list of strings]

	This function takes a csv object created from a csv file document and
	extracts a list of items, their categories, and their price. It returns
	this data as a list of strings that are formatted as:
			category|item|price
	"""
	item_list = []

	for row in file_contents:
		name = row[0]
		cost = row[2]
		catg = row[9]

		# Check to see if no price listed
		if (len(cost) == 0):
			continue

		# All prices in the DMPG are in gp
		cost = cost + " gp"
		item_entry = catg + "|" + name + "|" + cost
		item_list.append(item_entry)

	return item_list


def write_data(item_list, write_file):
	"""
	:inputs: 	item_list   [a list of strings]
			 	write_file  [a str]
	:returns:	None

	This function takes in a list of strings and a file to write to and writes
	the strings to the file, separating each with a new line. This function
	returns nothing, but has the side effect of writing to write_file.
	"""
	with open(write_file, 'w') as file:
		file.write('\n'.join(item_list))


## Main Function

def main():
	"""
	:inputs: 		None
	:returns: 		None

	This is the main function which utilizes the above functions to scrape
	data from the csv files listed and write it to the file given by write_file.
	"""
	write_file = "mi_merchant_prices.txt"

	with open("magic_items.csv", 'r') as file:
		contents = csv.reader(file)
		item_list = collect_data(contents)
		write_data(item_list, write_file)
			



## Executing Main Function

if __name__ == "__main__":
	main()
