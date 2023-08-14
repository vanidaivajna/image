import os
import matplotlib
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.filters import threshold_niblack, threshold_sauvola

# Set font size for matplotlib
matplotlib.rcParams['font.size'] = 9

# Define paths for input and output folders
input_folder = "input_images_folder"
output_niblack_folder = "output_niblack"
output_sauvola_folder = "output_sauvola"

# Create output folders if they don't exist
os.makedirs(output_niblack_folder, exist_ok=True)
os.makedirs(output_sauvola_folder, exist_ok=True)

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]

# Process each image
for image_file in image_files:
    # Read the input image
    image_path = os.path.join(input_folder, image_file)
    image = imread(image_path, as_gray=True)
    
    # Apply Niblack's thresholding method
    window_size = 25
    thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
    binary_niblack = image > thresh_niblack
    
    # Apply Sauvola's thresholding method
    thresh_sauvola = threshold_sauvola(image, window_size=window_size)
    binary_sauvola = image > thresh_sauvola
    
    # Save Niblack's thresholded image
    output_niblack_path = os.path.join(output_niblack_folder, image_file)
    imsave(output_niblack_path, binary_niblack.astype('uint8') * 255)
    
    # Save Sauvola's thresholded image
    output_sauvola_path = os.path.join(output_sauvola_folder, image_file)
    imsave(output_sauvola_path, binary_sauvola.astype('uint8') * 255)

print("Thresholding and saving complete.")
