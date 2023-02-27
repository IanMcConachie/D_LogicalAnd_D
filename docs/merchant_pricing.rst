Merchant Pricing Documentation
=================================

In this document we explain the mechanics and design of the merchant pricing feature of D&&D.


Web Scraping
--------------

Here we give a detailed explanation of how data was collected and what sources were used to train and test the machine learning model behind the merchant pricing feature.

Sources
#########

The data that was used in creating our model for this feature came from three online sources:

- `The Thieves Guild <https://www.thievesguild.cc/shops/>`_
- `D&D Beyond <https://www.dndbeyond.com/equipment>`_
- `The Discerning Merchant's Price Guide <https://aftermidnightgaming.com/wp-content/uploads/2021/02/727668-Discerning_Merchants_Price_Guide_v4.1.pdf>`_

The first two sources primarily provide prices for common non-magical items in the D&D canon, while the Discerning Merchant's Price Guide mostly covers magical items. Together they provide around 1,600 data points with item names, categories, price, and denomination (i.e. gold, silver, or copper pieces). However, after duplicates were removed we were left with approximately 1,400 data points.


Methodology
############

Thieves Guild and D&D Beyond both publish their pricing lists as websites which I scraped using python's built in html parser and the `Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ library for extracting information from a parsed html file. For the Discerning Merchant's Price Guide (DMPG) I used a fan-made csv file available `here <https://guildberkeley.wordpress.com/tag/discerning-merchants-price-guide/>`_ that compiled entries from the document (which originally came in the form of a pdf). The DMPG entries from the csv file were traversed using python's built-in csv library.

A different script was made for scraping the data from each of the 3 sources into their own formatted txt file of data points. This resulted in 3 pairs of python scripts and text files:

- tg_scraper.py -> tg_merchant_prices.txt (The Thieves Guild)
- db_scraper.py -> db_merchant_prices.txt (D&D Beyond)
- mi_scraper.py -> mi_merchant_prices.txt (DMPG)

The data from each of these files was then combined using the data_combiner.py script. This script also simplified the categories the items fell into so that they had less overlap, separated the integer price value from the denomination, and got rid of any duplicate entries.




