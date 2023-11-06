import os

# Replace 'your_folder_path' with the path to the folder containing the images.
folder_path = 'Arpan'

# Initialize the starting number for renaming
start_number = 401

# Loop through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        old_file_path = os.path.join(folder_path, filename)

        # Get the file extension (e.g., '.jpg')
        file_extension = os.path.splitext(filename)[1]

        new_filename = f"{start_number}{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

        start_number += 1

print("Image files renamed successfully.")
