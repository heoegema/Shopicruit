##https://help.shopify.com/api/reference/product

import sys
import urllib.request
import json

numProducts = 0
productBought =0
noTaxProductCostTotal = 0
withTaxProductCostTotal = 0              
standardCanadianTaxRate = 1.13
numVariantAmount =0
count = 1
if(len(sys.argv) < 2):
    numOfResultsPages = 5;
else:
    numOfResultsPages = int(sys.argv[1])

while count <= numOfResultsPages:
    URL = "http://shopicruit.myshopify.com/products.json?page="
    URL += str(count)
    
    #Load the data
    try:
        results = urllib.request.urlopen(URL)

        productData = json.loads(results.readall().decode('utf-8'))
    
    except BaseException as e:
        print("Error occured while getting data: {}".format(str(e)))
        exit(1)

    products = productData["products"]


    for product in products:
    
        if(product["product_type"] == "Clock") or (product["product_type"] == "Watch"):
            numProducts += 1
            #check each variant
            for item in product["variants"]:
                numVariantAmount +=1
                if(item["taxable"] == "true"):
                    withTaxProductCostTotal += float(item["price"])
                else: 
                    noTaxProductCostTotal += float(item["price"])
                
    count+=1


cost = standardCanadianTaxRate*withTaxProductCostTotal + noTaxProductCostTotal
print("Number of Variants", numVariantAmount)
print("Number of Products", numProducts)
print("Total Cost of all clocks and watches is ${:.2f}" .format(cost))

