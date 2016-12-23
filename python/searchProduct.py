import json

with open('products.json') as data_file:
    data = json.load(data_file)


def searchProduct():
    product_name = input("What is the product name?")

    for product in data["products"]:
        if product_name.lower() == product["name"].lower():
            print("match")
            return
        else:
            print("ooops!!")
            return searchProduct()

searchProduct()
