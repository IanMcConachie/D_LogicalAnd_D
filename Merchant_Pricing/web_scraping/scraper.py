"""
Author: 			Ian McConachie
Professor: 			Humphrey Shi, Steven
Class: 				CS 472
Date Created: 		02/04/2023
Last Date Modified: 02/04/2023

Description:

This python script scrapes data from the Theive's Guild 5e resource site. It
writes the category of an item, the item's name, and the price of the item
(in gold, silver, or copper pieces) to a text file separating each field with a
"|" character. Each entry is separated by a newline.

"""

## Import Statements
from bs4 import BeautifulSoup, NavigableString, Tag
import urllib.request

## Helper Functions

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


def has_anchor(child):
	"""
	"""
	ret = False
	if (child.contents[1].contents == 3):
		ret = True
	return ret


def is_category(child):
	"""
	:inputs:	child [a Tag object defined in bs4]
	:returns:	(ret, cat) [a tuple with a Boolean and a str]

	This function has a dual purpose of finding whether a child is a category
	for items and if so extracting the name of that category.
	"""
	ret = False
	cat = None
	if ('flexCat' in child['class']):
		cat = str(child.contents[1].contents[0])
		cat = cat.strip()
		ret = True

	return (ret,cat)


def is_section(child):
	"""
	:inputs:	child [a Tag object defined in bs4]
	:returns:	(ret, sec) [a tuple with a Boolean and a str]

	This function has a dual purpose of finding whether a child is a section
	for items and if so extracting the name of that section.
	"""
	ret = False
	sec = None
	if ('flexSec' in child['class']):
		sec = str(child.contents[1].contents[0])
		sec = sec.strip()
		ret = True

	return (ret,sec)


def is_item(child):
	"""
	:inputs:	child [a Tag object defined in bs4]
	:returns:	(ret, itm, cst) [a tuple with a Boolean, a str, and a str]

	This function has a dual purpose of finding whether a child is an item
	and if so, extracting the name and cost of the item.
	"""
	ret = False
	itm = None
	cst = None
	if ('contentrow' in child['class']):
		#print(len(child.contents[1].contents))
		has_a = has_anchor(child)
		if (has_a):
			itm = str(child.contents[1].contents[1].string)
			cst = str(child.contents[3].contents[2].string)
			itm = itm.strip()
			cst = cst.strip()
			ret = True
		else:
			x = 1+ 1

	return (ret,itm,cst)


## Modular Functions

def collect_data(soup):
	"""
	"""
	# Variables we'll use later
	current_cat = ""
	current_sec = ""
	item_list = []

	# Find the shop table
	table = soup.find(id="shopTbl")

	# Iterate through all children of the shop table
	for child in table.contents:
		# If the child is a string, skip
		if isinstance(child, NavigableString):
			continue

		# If the child is a Tag, analyze
		if isinstance(child, Tag):
			# If it is a new category
			is_cat = is_category(child)
			if (is_cat[0]):
				current_cat = is_cat[1]
				current_sec = ""
				#print(is_cat[1])
				continue

			# If it is a new section
			is_sec = is_section(child)
			if (is_sec[0]):
				current_sec = is_sec[1]
				#print("   ",current_sec)
				continue

			# If it is an item
			is_itm = is_item(child)
			if(is_itm[0]):
				itm = is_itm[1]
				cst = is_itm[2]
				print("    ",itm," : ", cst)
				item_entry = current_cat+"|"+itm+"|"+cst
				item_list.append(item_entry)

	return item_list


def write_data(item_list, write_file):
	"""
	:inputs: 	item_list   [a list of strings]
			 	write_file  [a str]
	:returns:	
	"""
	with open(write_file, 'w') as file:
		file.write('\n'.join(item_list))


def main():
	"""
	"""
	files = ["adventurer.html", "ilicit.html", "arcane.html",
	 "tailor.html", "alchemist.html", "blacksmith.html", "bookstore.html", 
	 "bowyer.html", "inn.html", "jewler.html", "leather.html", "temple.html"]
	write_file = "merchant_prices.txt"
	for file in files:
		print(file)
		path = "html_files/" + file
		with open(path, 'r') as f:
			text = f.read()
			soup = make_soup(text)
			item_list = collect_data(soup)
			write_data(item_list, write_file)

	return None

if __name__ == "__main__":
	main()