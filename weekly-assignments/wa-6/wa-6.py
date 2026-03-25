import pymongo
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Insert a xlsx file into a MongoDB collection.")
parser.add_argument("file", metavar="FILE", type=str, help="The xlsx file to insert into MongoDB.")
args = parser.parse_args()

datasample = pd.read_excel(args.file)
records = datasample.to_dict(orient="records")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mlb"]
mycol = mydb["weeklysix"]

x = mycol.insert_many(records)
rizz = mycol.find_one(filter={"Test Owner": "The Rizzler"})

print(f"The Rizzler, Test: {rizz.get('Test #')} Case: {rizz.get('Test Case')}")