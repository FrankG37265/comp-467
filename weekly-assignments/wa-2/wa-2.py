counter = 0

with open("ingest_this.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()

    for line in lines:
        sixseven = line.count("67")
        counter += 1
        print(f"\nLine {counter} - 67, {sixseven} times")
    
