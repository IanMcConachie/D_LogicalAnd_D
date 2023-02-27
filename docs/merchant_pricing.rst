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

The first two sources primarily provide prices for common non-magical items in the D&D canon, while the Discerning Merchant's Price Guide mostly covers magical items. Together they provide around 1,600 data points with item names, categories, price, and denomination (i.e. gold, silver, or copper pieces).


Methodology
############

