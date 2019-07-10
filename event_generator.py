## USAGE:
#  Get 1 result:
# python3 event_generator.py
#
#  Get N results, where N is in the range [1, 5000]:
# python3 event_generator.py N
#  Example:
# python3 event_generator.py 100

import sys
import requests
import json
from random import choice
import datetime

num_customers = sys.argv[1] if len(sys.argv) > 1 else 1
get_all_customer_details = False

# Get customer data from randomuser.me
def get_customers(num_customers, get_all_customer_details=True):

    url = "https://randomuser.me/api/?results=" + str(num_customers)

    details = {
        "gender"	: False,
        "name"		: True,
        "location" 	: True,
        "email" 	: False,
        "login" 	: False,
        "registered" 	: False,
        "dob" 		: False,
        "phone" 	: False,
        "cell" 		: False,
        "id" 		: True,
        "picture" 	: False,
        "nat" 		: False
    }

    if not get_all_customer_details:
        # Available nationalities:
        #  AU,BR,CA,CH,DE,DK,ES,FI,FR,GB,IE,IR,NO,NL,NZ,TR,US
        #
        # NO always returns error
        # BR, CA returns None as id
        # FI returns erroneous id
        # IR arabic name may not be readable
        url += "&nat=AU,CH,DE,DK,ES,FI,FR,GB,IE,IR,NL,NZ,TR,US"
        url += "&inc="
        for detail, inc in details.items():
            url += detail + ',' if inc else ''
        url = url.strip(',')
    try:
        print(url)
        r = requests.get(url)
        print(r)
        results = json.loads(r.text)["results"]
    except:
        print("Results cannot be retrieved from randomuser.me")
        results = ''
    return results

# EVENTS list
# The event will be chosen randomly from this list
events = ["SHOPPER_VIEWED_PRODUCT",
          "SHOPPER_ADDED_PRODUCT_TO_CART",
          "SHOPPER_REMOVED_PRODUCT_FROM_CART",
          "SHOPPER_PAID"]

# PRODUCTS list
# The product will be chosen randomly from this list
with open('products.json') as products_file:
    products = json.load(products_file)



if __name__ == "__main__":
    results = get_customers(num_customers, get_all_customer_details)
    for result in results:
        message = {}
        message["event"] = choice(events)

        shopper = {}
        shopper["id"] = result["id"]["value"]
        shopper["name"] = result["name"]["first"].capitalize() + ' ' + result["name"]["last"].capitalize()
        shopper["city"] = result["location"]["city"].capitalize()

        product = {}
        random_product = choice(products)
        product["name"] = random_product["name"]
        product["sku"] = random_product["sku"]

        message["shopper"] = shopper
        message["product"] = product
        message["timestamp"] = datetime.datetime.utcnow().isoformat()

        print( message )
