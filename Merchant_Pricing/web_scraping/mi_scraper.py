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


## Main Function

def main():
	"""
	:inputs: 		None
	:returns: 		None

	This is the main function which utilizes the above functions to scrape
	data from the csv files listed and write it to the file given by write_file.
	"""
	write_file = "mi_merchant_prices.txt"
	item_list = []
	
	with open("magic_items.csv", 'r') as file:
		contents = csv.reader(file)
		for row in contents:
			print(row)



## Executing Main Function

if __name__ == "__main__":
	main()
