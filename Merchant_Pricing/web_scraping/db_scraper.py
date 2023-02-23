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



def main():
	"""
	:inputs: 		None
	:returns: 		None

	This is the main function which utilizes the above functions to scrape
	data from the html files listed in the files list and write them to 
	the file given by write_file.
	"""
	URLs = ['https://www.dndbeyond.com/equipment']
	req = Request(
    	url='https://www.dndbeyond.com/equipment', 
    	headers={'User-Agent': 'Mozilla/5.0'}
	)

	for url in URLs:
		req = Request( url=url, headers={'User-Agent': 'Mozilla/5.0'})
		website = urlopen(req)
		print(website.read())


if __name__ == "__main__":
	main()