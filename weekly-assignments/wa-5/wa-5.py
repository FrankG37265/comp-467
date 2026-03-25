import argparse

parser = argparse.ArgumentParser(description="Count how many lines in a text file.")
parser.add_argument("file", metavar="FILE", type=str, help="The text file to count lines in.")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Print the lines in the file.")
args = parser.parse_args()

with open(args.file, "r") as f:
    lines = 0
    for line in f:
        if args.verbose:
            print(line.strip())
        lines += 1

print(f"\nNumber of lines in {args.file}: {lines}\n")