import json
def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Stiven:Cdx1Jx9NTsvxrZnE@cluster0.f4ncljs.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['goods']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    dbname = get_database()

    # # Create the collection name
    # collection_name = "goods"

    # # Create a collection in the database
    # collection = dbname[collection_name]

    # # Create a dictionary. This is the data we want to enter into the database
    # post = json.loads(open('goods.json').read())

    # # Insert the data into a collection
    # # The database and collection, if they don't already exist, will be created at this point.
    # collection.insert_one(post)

class Goods():
    def __init__(self):
        self.db = get_database()
        self.collection = self.db['goods']
    
    def get(self):
        return self.collection.find_one()['items']

    def GetSorted(self, sort):
        return self.collection.find().sort(sort)

classs = Goods()

print(Goods().get())