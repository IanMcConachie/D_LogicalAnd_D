"""
Author: 			Ian McConachie
Professor: 			Humphrey Shi, Steven Walton
Class: 				CS 472
Date Created: 		02/22/2023
Last Date Modified: 02/22/2023

Description:

This python script scrapes data from the D&D Beyond 5e resource site. It
writes the category of an item, the item's name, and the price of the item
(in gold, silver, or copper pieces) to a text file separating each field with a
"|" character. Each entry is separated by a newline.
"""

## Import Statements
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, NavigableString, Tag

## Modular Functions

def make_soup(html_text):
	"""
	:inputs: 	html_text [a string version of an html file]
	:returns:	soup [a BeautifulSoup object]

	This is a simple helper function that takes in a string containing the
	text from an html file and then outputs a "BeautifulSoup" object using the
	instantiation methods provided by Beautiful Soup 4.
	"""
	soup = BeautifulSoup(html_text, 'html.parser')
	return soup


def collect_data(soup):
	"""
	:inputs:		soup [a BeautifulSoup object defined in bs4]
	:returns:		item_list [a list of strings]

	This function takes a BeautifulSoup object created by parsing an html
	document and extracts a list of items, their categories, and their price.
	It returns this data as a list of strings that are formatted as:
			category|item|price
	"""
	item_list = []
	item_rows = soup.find_all(class_="list-row-equipment")

	for row in item_rows:
		name_tag = row.find(class_="link")
		cost_tag = row.find(class_="list-row-cost-primary-text")
		catg_tag = row.find(class_="list-row-name-secondary-text")

		name = (name_tag.text).strip()
		cost = (cost_tag.text).strip()
		catg = (catg_tag.text).strip()

		if (cost == "--"):
			continue

		item_entry = catg+"|"+name+"|"+cost
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


## Main function

def main():
	"""
	:inputs: 		None
	:returns: 		None

	This is the main function which utilizes the above functions to scrape
	data from the URLs listed in the URL list and write them to 
	the file given by write_file.
	"""
	URLs = ['https://www.dndbeyond.com/equipment', 'https://www.dndbeyond.com/equipment?page=2',
			'https://www.dndbeyond.com/equipment?page=3', 'https://www.dndbeyond.com/equipment?page=4',
			'https://www.dndbeyond.com/equipment?page=5', 'https://www.dndbeyond.com/equipment?page=6',
			'https://www.dndbeyond.com/equipment?page=7', 'https://www.dndbeyond.com/equipment?page=8',
			'https://www.dndbeyond.com/equipment?page=9', 'https://www.dndbeyond.com/equipment?page=10',
			'https://www.dndbeyond.com/equipment?page=11', 'https://www.dndbeyond.com/equipment?page=12',
			'https://www.dndbeyond.com/equipment?page=13', 'https://www.dndbeyond.com/equipment?page=14']
	write_file = "db_merchant_prices.txt"
	item_list = []
	for url in URLs:
		req = Request( url=url, headers={'User-Agent': 'Mozilla/5.0'})
		website = urlopen(req)
		#print(website.getcode())
		text = website.read()
		soup = make_soup(text)
		item_list = item_list + collect_data(soup)

	write_data(item_list, write_file)

	return None


if __name__ == "__main__":
	main()