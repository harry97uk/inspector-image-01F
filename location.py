from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def convert_to_decimal(degrees, minutes, seconds):
    return degrees + minutes / 60.0 + seconds / 3600.0

def extract_gps_info(image_path):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Extract Exif data
        exif_data = img._getexif()

        if exif_data and 34853 in exif_data:  # Check if GPSInfo tag is available
            gps_info = exif_data[34853]  # GPSInfo tag value

            # Extract and convert GPS coordinates
            latitude = convert_to_decimal(*gps_info[2])
            longitude = convert_to_decimal(*gps_info[4])

            # Determine the direction (N/S, E/W)
            if gps_info[3] == 'S':
                latitude = -latitude

            if gps_info[1] == 'W':
                longitude = -longitude

            return latitude, longitude
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None