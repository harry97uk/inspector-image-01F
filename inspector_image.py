import argparse
from PIL import Image, ExifTags, JpegImagePlugin
from PIL.ExifTags import TAGS
from location import extract_gps_info

# Define the argparse configuration
parser = argparse.ArgumentParser(description="Inspector Image")

# Add options for full name, IP address, and username
parser.add_argument("-map", metavar="Location", type=str, help="Find image location data")
parser.add_argument("-steg", metavar="Steganography", type=str, help="Decode image data")

# Parse the command-line arguments
args = parser.parse_args()

if args.map:
    image_path = args.map
    gps_info = extract_gps_info(image_path)

    if gps_info:
        print(f"Latitude: {gps_info[0]}")
        print(f"Longitude: {gps_info[1]}")
    else:
        print("No GPS information found.")
elif args.steg:
    image_path = args.steg
    data = ""

    with open(image_path, "rb") as f:
        for chunk in iter(lambda: f.read(8), b''):
            data += chunk.decode('utf-8', errors="ignore")
            
    print("-----BEGIN PGP PUBLIC KEY BLOCK-----" + data.split("-----BEGIN PGP PUBLIC KEY BLOCK-----")[1])
else:
    print("No recognized option provided. Use -map or -steg.")
