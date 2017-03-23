#!/usr/bin/env python3
# license safe image downloader

# https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q=trains&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:l,sur:fmc
# 1. Searches for whatever using custom google url (license safe, high resolution)
# 2. Finds image elemenet's direct link
# 3. downloads x pictures from the page. if no more pictures, it clicks
# 'Show more results' and continues on the next page. 

import requests
import argparse
import sys
import bs4

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("search_term", help="Keyword for the google search.")
parser.add_argument("-p", "--page", help="Specifies which page should the image collection start on. ")
args = parser.parse_args()
search_term = args.search_term

# License safe, high resolution search link
url = 'https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q=' + keyword + '&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=sur:fmc'


