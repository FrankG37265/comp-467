import re
import numpy as np

list = []

with open("fries.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()

    for line in lines:
        numbers = re.findall(r"\d+", line)
        lineresult = sum(int(x) for x in numbers)
        list.append(lineresult)

np.savetxt("output.csv", list, delimiter=",", fmt="%d")