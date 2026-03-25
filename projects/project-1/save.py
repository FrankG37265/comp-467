        startRange = 0
        endRange = 0
        for frame in currentpath[1:]:
            if startRange == 0 and endRange == 0:
                startRange = frame
                endRange = frame
            elif int(frame) == int(endRange) + 1:
                endRange = frame
            else:
                if startRange == endRange:
                    print(f"{xytechmatch} {startRange}")
                else:
                    print(f"{xytechmatch} {startRange}-{endRange}")
                startRange = frame
                endRange = frame