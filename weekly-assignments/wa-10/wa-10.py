import argparse
import ffmpeg
import sys

parser = argparse.ArgumentParser(description="A script that generates thumbnails 1/3 size from videos using ffmpeg.")
parser.add_argument("--input", type=str, required=True, help="The input video file.")

args = parser.parse_args()

def grab_dimensions(input_file):
    probe = ffmpeg.probe(input_file)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        raise ValueError("No video stream found in the input file.")
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    return width, height

def generate_thumbnail(input_file, width, height):
    output_file = input_file.rsplit('.', 1)[0] + '_proxy.jpg'
    (
        ffmpeg
        .input(input_file, ss=1)  # ss=1 is pull image from one second in
        .filter('scale', width, height)
        .output(output_file, vframes=1)
        .run()
    )
    print(f"\n\nThumbnail generated and saved as {output_file}")

# Check for input
if not args.input:
    print("Please provide an input video file using the --input argument.")
    sys.exit(1)

inwidth, inheight = grab_dimensions(args.input)
outwidth = inwidth // 3
outheight = inheight // 3
generate_thumbnail(args.input, outwidth, outheight)

print(f"Original dimensions: {inwidth}x{inheight} \nProxy dimensions: {outwidth}x{outheight}")