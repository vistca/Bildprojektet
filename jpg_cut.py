import os
from PIL import Image

# Create output directory if it doesn't exist
output_dir = 'small_high_res'

# Path to the folder containing the jpg images
input_dir = 'jpg'

count = 1

# Loop through all files in the input directory
for filename in os.listdir(input_dir):

    print(f"image nr. {count}")
    count += 1

    if filename.lower().endswith('.jpg'):
        # Open the image
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        
        # Get image dimensions
        img_width, img_height = img.size
        
        # Compute number of 100x100 blocks
        x_blocks = img_width // 100
        y_blocks = img_height // 100
        
        # Generate 100x100 subsets
        for i in range(x_blocks):
            for j in range(y_blocks):
                left = i * 100
                upper = j * 100
                right = left + 100
                lower = upper + 100
                bbox = (left, upper, right, lower)
                
                # Crop the image
                subset = img.crop(bbox)
                
                # Save the subset image
                subset_filename = f'{filename[:-4]}_{i}_{j}.jpg'
                subset_path = os.path.join(output_dir, subset_filename)
                subset.save(subset_path)

print("All images have been processed and saved in the 'output' folder.")