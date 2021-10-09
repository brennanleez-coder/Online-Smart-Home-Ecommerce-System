import json

def initialiseMongoDB(client):
    # if db is not created, create db with collection.
    dblist = client.list_database_names()
    if "bt2102" not in dblist:
        with open('ItemAndProductData/items.json', 'r') as f:
            itemsData = json.load(f)

        with open('ItemAndProductData/products.json', 'r') as f:
            productsData = json.load(f)
        result = client.bt2102.items.insert_many(itemsData)
        result = client.bt2102.products.insert_many(productsData)