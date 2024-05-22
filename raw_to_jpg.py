

import os
import rawpy
from PIL import Image

# Define the directories
raw_dir = 'raw'
jpg_dir = 'jpg'

# Create jpg directory if it doesn't exist
if not os.path.exists(jpg_dir):
    os.makedirs(jpg_dir)

# Function to convert .CR2 to .jpg
def convert_cr2_to_jpg(cr2_path, jpg_path):
    with rawpy.imread(cr2_path) as raw:
        rgb = raw.postprocess()
        img = Image.fromarray(rgb)
        img.save(jpg_path, 'JPEG')

# Loop through each file in the raw directory
for count, filename in enumerate(os.listdir(raw_dir)):
    if filename.lower().endswith('.cr2'):
        cr2_path = os.path.join(raw_dir, filename)
        new_filename = f'image_{count + 1}.jpg'
        jpg_path = os.path.join(jpg_dir, new_filename)
        
        # Convert and save the .jpg image
        convert_cr2_to_jpg(cr2_path, jpg_path)

        print(f'Converted {filename} to {new_filename}')

print('Conversion complete!')

