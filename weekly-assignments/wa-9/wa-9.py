import argparse
import ffmpeg
import sys

parser = argparse.ArgumentParser(description="A script that grabs metadata from videos using ffmpeg.")
parser.add_argument("--input", type=str, required=True, help="The input video file.")

args = parser.parse_args()

def grab_metadata(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_metadata.txt'
    (
        ffmpeg
        .input(input_file)
        .output(format='ffmetadata', filename=output_file)
        .run()
    )

# Check for input
if not args.input:
    print("Please provide an input video file using the --input argument.")
    sys.exit(1)

grab_metadata(args.input)