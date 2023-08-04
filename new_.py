import json
import os
import shutil

def extract_filenames_from_json(json_data, class_name):
    filenames = []
    for image_id, image_info in json_data['_via_img_metadata'].items():
        if image_info['file_attributes']['class'] == class_name:
            filename = image_info['filename']
            filenames.append(filename)
    return filenames

def separate_images_by_class(json_data, source_folder, destination_folder):
    genuine_filenames = extract_filenames_from_json(json_data, 'Geniunie')
    fraud_filenames = extract_filenames_from_json(json_data, 'fraud')

    for filename in genuine_filenames:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, 'Geniunie', filename)
        shutil.move(source_path, destination_path)

    for filename in fraud_filenames:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, 'fraud', filename)
        shutil.move(source_path, destination_path)

if __name__ == '__main__':
    # Load the JSON-like data
    json_data = json.loads('''YOUR_JSON_DATA_HERE''')

    # Set the source folder where the images are currently located
    source_folder = '/path/to/source/folder'

    # Set the destination folder where the images will be separated into genuine and fraud subfolders
    destination_folder = '/path/to/destination/folder'

    # Create subfolders for genuine and fraud images in the destination folder
    os.makedirs(os.path.join(destination_folder, 'Geniunie'), exist_ok=True)
    os.makedirs(os.path.join(destination_folder, 'fraud'), exist_ok=True)

    # Separate the images based on the classes
    separate_images_by_class(json_data, source_folder, destination_folder)
