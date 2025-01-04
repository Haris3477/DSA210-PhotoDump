import os
import random
from datetime import datetime, timedelta
from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd

# Path to the photos folder
PHOTO_FOLDER = "photos"
OUTPUT_CSV = "photo_metadata.csv"

# Function to generate a random timestamp
def generate_random_timestamp():
    start_date = datetime(2000, 1, 1)  # Earliest possible date
    end_date = datetime(2022, 12, 31)  # Latest possible date
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date.strftime("%Y:%m:%d %H:%M:%S")

# Function to extract photo metadata
def extract_photo_metadata(photo_folder):
    metadata_list = []

    for root, dirs, files in os.walk(photo_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):  # Add more extensions if needed
                photo_path = os.path.join(root, file)
                try:
                    image = Image.open(photo_path)
                    exif_data = image._getexif()

                    if exif_data:
                        metadata = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
                        timestamp = metadata.get("DateTime", None)
                    else:
                        timestamp = None

                    # Assign random timestamp if none is found
                    if not timestamp:
                        timestamp = generate_random_timestamp()

                    metadata_list.append({"Filename": file, "Timestamp": timestamp})
                except Exception as e:
                    print(f"Error reading {file}: {e}")
                    metadata_list.append({"Filename": file, "Timestamp": generate_random_timestamp()})

    return metadata_list

# Extract metadata
metadata = extract_photo_metadata(PHOTO_FOLDER)

# Save metadata to a CSV file
if metadata:
    df = pd.DataFrame(metadata)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nMetadata saved to '{OUTPUT_CSV}'.")
else:
    print("\nNo metadata extracted.")

# Print summary
print(f"\nProcessed {len(metadata)} photos.")