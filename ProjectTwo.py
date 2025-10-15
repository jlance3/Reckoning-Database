import argparse
import pymongo
import pandas as pd

#Take two xlsx files and inserts data into two different collections in MongoDB
def insert_data_to_mongodb(file1, file2, db_name, collection1, collection2):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://lancestajimenez_db_user:wcHp8TWnJvdYi74Y@testcluster.vb9fgy4.mongodb.net/")
    db = client[db_name]

    # Read the first Excel file and insert into the first collection
    df1 = pd.read_excel(file1)
    records1 = df1.to_dict(orient='records')
    db[collection1].insert_many(records1)
    print(f"Inserted {len(records1)} records into {collection1}")

    # Read the second Excel file and insert into the second collection
    df2 = pd.read_excel(file2)
    records2 = df2.to_dict(orient='records')
    db[collection2].insert_many(records2)
    print(f"Inserted {len(records2)} records into {collection2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insert data from two Excel files into MongoDB collections.")
    parser.add_argument("file1", help="Path to the first Excel file")
    parser.add_argument("file2", help="Path to the second Excel file")
    parser.add_argument("db_name", help="Name of the MongoDB database")
    parser.add_argument("collection1", help="Name of the first MongoDB collection")
    parser.add_argument("collection2", help="Name of the second MongoDB collection")

    args = parser.parse_args()

    insert_data_to_mongodb(args.file1, args.file2, args.db_name, args.collection1, args.collection2)

#Creating methods to query the data from the two collections while excluding duplicate data
def query_collections(db_name, collection1, collection2):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://lancestajimenez_db_user:wcHp8TWnJvdYi74Y@testcluster.vb9fgy4.mongodb.net/")
    db = client[db_name]
    col1 = db[collection1]
    col2 = db[collection2]
    # Query the first collection
    results1 = list(col1.find())
    print(f"Records from {collection1}:")
    for record in results1:
        print(record)
    # Query the second collection
    results2 = list(col2.find())
    print(f"\nRecords from {collection2}:")
    for record in results2:
        print(record)