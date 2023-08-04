import os
import json
import shutil

def extract_image_names_per_class(json_data):
    image_names_per_class = {}
    for class_name, images in json_data.items():
        image_names = list(images.keys())
        image_names_per_class[class_name] = image_names
    return image_names_per_class

def move_images_to_class_folders(image_names_per_class, source_folder, destination_folder):
    for class_name, image_names in image_names_per_class.items():
        class_folder = os.path.join(destination_folder, class_name)
        os.makedirs(class_folder, exist_ok=True)
        for image_name in image_names:
            source_path = os.path.join(source_folder, image_name)
            destination_path = os.path.join(class_folder, image_name)
            shutil.move(source_path, destination_path)

# Replace 'your_vgg_json_file.json' with the actual file path of your JSON file.
file_path = 'your_vgg_json_file.json'
source_folder = 'path/to/source/folder'  # Replace with the path to the folder containing images.
destination_folder = 'path/to/destination/folder'  # Replace with the path where you want to create class subfolders.

try:
    with open(file_path, 'r') as f:
        json_data = json.load(f)
        image_names_per_class = extract_image_names_per_class(json_data)
        move_images_to_class_folders(image_names_per_class, source_folder, destination_folder)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Error parsing JSON data. Please check if the JSON file is in the correct format.")
except Exception as e:
    print(f"An error occurred: {e}")
