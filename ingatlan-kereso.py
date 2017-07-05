#!/usr/bin/env python3

import pprint
import traceback
import requests

from time import sleep
from lxml import html
from lxml import etree  # html pretty print

pp = pprint.PrettyPrinter(indent=4)


def get_apartment_ids(url):
    print("GET {}".format(url))

    page = requests.get(url)
    tree = html.fromstring(page.content)

    apartments_count = tree.xpath("//div[@class='results__number']")
    count = apartments_count[0].get("data-listings-count")
    count = count.replace(" ", "")
    print("COUNT {}".format(count))

    pagecount = (int(count) / 20) + 1
    print("PAGECOUNT {}".format(pagecount))

    apartmentIds = []

    # First page parsing
    apartmentButtonInfoList = tree.xpath("//button[@class='listing__hide-undo button--link js-hide-undo']")
    for apartmentButtonInfo in apartmentButtonInfoList:
        apartmentId = apartmentButtonInfo.get('data-id')
        apartmentIds.append(apartmentId)

    parsed_page_count = 1
    
    while parsed_page_count != pagecount:

        page_index = parsed_page_count + 1
        next_page_url = url + "?page=" + str(page_index)

        nextpage_apartment_ids = get_apartments_for_nextpages(next_page_url)
        apartmentIds.extend(nextpage_apartment_ids)
        
        parsed_page_count += 1

    print("Apartments: " + str(len(apartmentIds)))

    pp.pprint(apartmentIds)

    return apartmentIds

def get_apartments_for_nextpages(url):
    print("GET {}".format(url))
    page = requests.get(url)
    tree = html.fromstring(page.content)
    apartmentButtonInfoList = tree.xpath("//button[@class='listing__hide-undo button--link js-hide-undo']")

    apartmentIds = []
    for apartmentButtonInfo in apartmentButtonInfoList:
        apartmentId = apartmentButtonInfo.get('data-id')
        apartmentIds.append(apartmentId)

    return apartmentIds

def get_apartment_details(apartment_ids):

    for apartment_id in apartment_ids:
        
        apartment_url = "https://ingatlan.com/" + str(apartment_id)
        #print("GET {}".format(apartment_url))

        apartment_page = requests.get(apartment_url)
        apartment_tree = html.fromstring(apartment_page.content)

        # collect data
        apartment_title = apartment_tree.xpath("//h1[@class='js-listing-title']")[0].text_content().encode('utf-8')

        apartment_size = apartment_tree.xpath("//span[@class='parameter-value']")[0].text_content()
        apartment_size = apartment_size.split(" ")[0]
        apartment_rooms = apartment_tree.xpath("//span[@class='parameter-value']")[1].text_content()
        apartment_rooms = apartment_rooms[:6]
        apartment_price = apartment_tree.xpath("//span[@class='parameter-value']")[2].text_content()
        apartment_price = apartment_price.split(" ")[0]


        apartment_parameters = apartment_tree.xpath("//div[@class='paramterers']/table/tr/td/text()")

        apartment_description = apartment_tree.xpath("//div[@class='long-description']")[0].text_content()


        print("LAKAS: {} {} {} {}".format(apartment_size, apartment_rooms, apartment_price, apartment_title))
        print(apartment_parameters)
        print(apartment_description)


def main():
    emails = []
    url = ('http://ingatlan.com/lista/elado+lakas+ujhegy-rozsaliget-lakopark')
    url_zuglo = 'https://ingatlan.com/lista/elado+lakas+tegla-epitesu-lakas+budapest+1-m2erkely-felett+uj-epitesu+ujszeru+felujitott+jo-allapotu+25-mFt-ig+45-60-m2+2-szoba-felett+xiv-ker'

    apartment_ids = get_apartment_ids(url)
    get_apartment_details(apartment_ids)


    print("{} apartments".format(len(apartment_ids)))

if __name__ == '__main__':
    main()