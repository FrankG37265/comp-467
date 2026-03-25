import csv

folderlocation = []
csvlist = [["Path", "Frames"]]

with open("Xytech_spring2026.txt", "r") as xytech:
    data = xytech.read()
    lines = data.splitlines()

    for line in lines:
        if "/" in line:
            folderlocation.append(line)


currentpath = ""

with open("Baselight_export_spring2026.txt", "r") as baselight:
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
        individualFrames = 0 #counter for amount of individual frames in a line
        frameRange = 0 #counter for amount of frame ranges in a line
        startRange = 0
        endRange = 0
        for frame in currentpath[1:]:
            if startRange == 0 and endRange == 0:
                startRange = frame
                endRange = frame
                continue
            if int(frame) == int(endRange) + 1:
                endRange = frame
                continue
            if startRange == endRange:
                csvlist.append([xytechmatch, startRange])
                individualFrames += 1
                startRange = frame
                endRange = frame
                continue

            csvlist.append([xytechmatch, f"{startRange}-{endRange}"])
            frameRange += 1
            startRange = frame
            endRange = frame

        #check if there is a remaining range to print after the loop
        if startRange != 0 and endRange != 0:
            if startRange == endRange:
                csvlist.append([xytechmatch, startRange])
                individualFrames += 1
            else:
                csvlist.append([xytechmatch, f"{startRange}-{endRange}"])
                frameRange += 1

        print(f"{xytechmatch} Individual: {individualFrames} Ranges: {frameRange}")

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvlist)