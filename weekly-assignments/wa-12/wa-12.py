import vimeo
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ACCESS_TOKEN")
key = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")

client = vimeo.VimeoClient(
    token='{ACCESS_TOKEN}',
    key='{CLIENT_ID}',
    secret='{CLIENT_SECRET}'
)

video = "snow.MP4"
uri = client.upload(video, data={
    'name': 'Weekly Assignment 12',
    'description': 'Uploaded through python for weekly assignment 12.'
})

print(f"Video uploaded! URI: {uri}")