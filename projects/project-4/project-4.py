import csv
import argparse
import ffmpeg
import sys
import os
import pymongo
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description="A script that something")
parser.add_argument("--baselight", type=str, help="Path to baselight file.")
parser.add_argument("--xytech", type=str, help="Path to xytech file.")
parser.add_argument("--process", type=str, help="Path to video file.")
args = parser.parse_args()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project4"]

def importxytech(xytechpath):
    folderlocation = []

    with open(xytechpath, "r") as xytech:
        data = xytech.read()
        lines = data.splitlines()

        for line in lines:
            if "/" in line:
                folderlocation.append(line)
    
    return folderlocation

def match(baselightpath, xytechpath):
    csvlist = [["Path", "Frames"]]

    folderlocation = importxytech(xytechpath)
    currentpath = ""

    with open(baselightpath, "r") as baselight:
        data = baselight.read()
        lines = data.splitlines()

        for line in lines:
            currentpath = line.split(" ")
            currentpath = [item for item in currentpath if item.strip()]
            querypath = currentpath[0].removeprefix("/baselightfilesystem1/")
            for folder in folderlocation:
                if querypath in folder:
                    xytechmatch = folder
                    break

            #frames
            individualframes = 0 #counter for amount of individual frames in a line
            framerange = 0 #counter for amount of frame ranges in a line
            startrange = 0
            endrange = 0
            for frame in currentpath[1:]:
                if startrange == 0 and endrange == 0:
                    startrange = frame
                    endrange = frame
                    continue
                if int(frame) == int(endrange) + 1:
                    endrange = frame
                    continue
                if startrange == endrange:
                    csvlist.append([xytechmatch, startrange])
                    individualframes += 1
                    startrange = frame
                    endrange = frame
                    continue

                csvlist.append([xytechmatch, f"{startrange}-{endrange}"])
                framerange += 1
                startrange = frame
                endrange = frame

            #check if there is a remaining range to print after the loop
            if startrange != 0 and endrange != 0:
                if startrange == endrange:
                    csvlist.append([xytechmatch, startrange])
                    individualframes += 1
                else:
                    csvlist.append([xytechmatch, f"{startrange}-{endrange}"])
                    framerange += 1

            print(f"{xytechmatch} Individual: {individualframes} Ranges: {framerange}")
    
    return csvlist

def exportfile(baselightpath, xytechpath):
    csvlist = match(baselightpath, xytechpath)

    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csvlist)

def probetimecode(video):
    probe = ffmpeg.probe(video)
    return probe.get('timecode')



#main
if not args.baselight or not args.xytech:
    print("Please input baselight and xytech file paths using argparse!")
    sys.exit(1)

#baselight database
datasample = pd.read_excel(args.baselight)
records = datasample.to_dict(orient="records")
mycol = mydb["baselight"]
x = mycol.insert_many(records)
print(f"Inserted {len(x.inserted_ids)} records from {args.baselight} into MongoDB collection {mycol.name}.")

#xytech database
datasample = pd.read_excel(args.xytech)
records = datasample.to_dict(orient="records")
mycol = mydb["xytech"]
x = mycol.insert_many(records)
print(f"Inserted {len(x.inserted_ids)} records from {args.xytech} into MongoDB collection {mycol.name}.")

#project 1
exportfile(args.baselight, args.xytech)