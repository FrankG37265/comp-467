import argparse
import ffmpeg
import sys

parser = argparse.ArgumentParser(description="A script that generates thumbnails from videos using ffmpeg.")
parser.add_argument("--input", type=str, required=True, help="The input video file.")

args = parser.parse_args()

def generate_thumbnail(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_thumbnail.jpg'
    (
        ffmpeg
        .input(input_file, ss=1)  # ss=1 is pull image from one second in
        .filter('scale', 320, -1)
        .output(output_file, vframes=1)
        .run()
    )
    print(f"Thumbnail generated and saved as {output_file}")

# Check for input
if not args.input:
    print("Please provide an input video file using the --input argument.")
    sys.exit(1)

generate_thumbnail(args.input)